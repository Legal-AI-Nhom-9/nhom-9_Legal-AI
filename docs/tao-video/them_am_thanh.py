"""Thêm lời dẫn (giọng đọc tổng hợp tiếng Việt) và nhạc nền tự tạo vào video.

Chạy từ thư mục gốc của kho:
    python3 docs/tao-video/them_am_thanh.py [video_vao] [video_ra] [thu_muc_mo_hinh]
Cần: ffmpeg, numpy, piper-tts (pip install piper-tts) và mô hình giọng
vits-piper-vi_VN-vais1000-medium (tải từ trang phát hành tts-models của k2-fsa/sherpa-onnx).

Giọng đọc: mô hình Piper "vi_VN-vais1000-medium", huấn luyện trên bộ dữ liệu VAIS-1000
(giấy phép CC BY 4.0). Đây là giọng máy tổng hợp, không mô phỏng một người cụ thể.
Nhạc nền do mã tự sinh (hợp âm sóng sin), không dùng bản nhạc có bản quyền.
"""
import os, subprocess, sys, wave
import numpy as np

VAO = sys.argv[1] if len(sys.argv) > 1 else "video/legal-ai-video.mp4"
RA = sys.argv[2] if len(sys.argv) > 2 else "video/legal-ai-video-co-tieng.mp4"
MO_HINH = sys.argv[3] if len(sys.argv) > 3 else "build_video/vits-piper-vi_VN-vais1000-medium"
TMP = "build_video/audio"
os.makedirs(TMP, exist_ok=True)
SR = 22050

# (giây bắt đầu cảnh, thời lượng cảnh, lời dẫn)
CANH = [
    # "Legal AI" viết theo âm tiếng Việt "Lê gồ Ây Ai" để giọng đọc phát âm đúng;
    # dùng dấu phẩy thay dấu chấm giữa câu vì giọng này hay nuốt chữ cuối trước dấu chấm.
    (0, 7, "Chín mươi giây, để hiểu Lê gồ Ây Ai."),
    (7, 9, "Lan chuyển nhà trọ, đã báo trước một tháng, nhưng ba triệu tiền cọc vẫn chưa được trả lại."),
    (16, 10, "Hỏi trên mạng, mỗi nơi nói một kiểu, còn thuê luật sư cho ba triệu, thì ít ai nghĩ tới."),
    (26, 10, "Lan mở Lê gồ Ây Ai, hỏi bằng tiếng Việt, như nhắn tin cho bạn."),
    (36, 10, "Câu trả lời ngắn, kèm tên văn bản, số điều, và đường dẫn tới văn bản gốc để tự kiểm tra."),
    (46, 10, "Lan tự đọc Điều ba trăm hai mươi tám, Bộ luật Dân sự, về tiền đặt cọc."),
    (56, 8, "Nếu còn tranh chấp, Lê gồ Ây Ai chỉ Lan tới luật sư, hoặc trợ giúp pháp lý nhà nước."),
    (64, 8, "Thuê nhà trọ, hợp đồng lao động, và mua bán trên mạng."),
    (72, 8, "Hỏi bằng tiếng Việt, đọc văn bản gốc, và biết khi nào cần luật sư."),
    (80, 8, "Lê gồ Ây Ai, hỏi luật dễ như nhắn tin."),
]
TONG = 88


def doc_wav(p):
    with wave.open(p) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        return x, w.getframerate()


def doi_tan_so(x, sr):
    if sr == SR:
        return x
    t = np.arange(0, len(x) * SR // sr) * sr / SR
    return np.interp(t, np.arange(len(x)), x)


from piper import PiperVoice, SynthesisConfig
giong = PiperVoice.load(f"{MO_HINH}/vi_VN-vais1000-medium.onnx",
                        config_path=f"{MO_HINH}/vi_VN-vais1000-medium.onnx.json")


def doc(cau, length_scale):
    cfg = SynthesisConfig(length_scale=length_scale, noise_scale=0.6, noise_w_scale=0.7)
    phan = list(giong.synthesize(cau, syn_config=cfg))
    x = np.concatenate([c.audio_float_array for c in phan]).astype(np.float32)
    return doi_tan_so(x, phan[0].sample_rate)


loi = np.zeros(TONG * SR, dtype=np.float32)
for i, (bd, dai, cau) in enumerate(CANH):
    toc_do = 1.45  # length_scale: lớn hơn 1 là đọc chậm hơn, rõ hơn
    while True:
        x = doc(cau, toc_do)
        if len(x) / SR <= dai - 1.0 or toc_do <= 0.9:
            break
        toc_do = round(toc_do - 0.05, 2)
    x = x / max(1e-6, np.abs(x).max()) * 0.8
    vt = int((bd + 0.5) * SR)
    loi[vt:vt + len(x)] += x[: len(loi) - vt]
    print(f"cảnh {i + 1}: {len(x) / SR:.1f}s / {dai}s (tốc độ {toc_do})")

# nhạc nền: bốn hợp âm nhẹ lặp lại, tự sinh bằng sóng sin
t = np.arange(TONG * SR) / SR
HOP_AM = [[220.0, 277.18, 329.63], [196.0, 246.94, 293.66], [174.61, 220.0, 261.63], [196.0, 246.94, 329.63]]
nhac = np.zeros_like(t)
for k in range(int(TONG / 4) + 1):
    a, b = int(k * 4 * SR), int(min((k + 1) * 4, TONG) * SR)
    if a >= b:
        break
    tt = t[a:b] - t[a]
    vo = np.minimum(1, tt / 0.8) * np.minimum(1, (tt[-1] - tt) / 0.8 + 0.05)
    for f in HOP_AM[k % 4]:
        nhac[a:b] += np.sin(2 * np.pi * f * tt) * vo * 0.05 + np.sin(2 * np.pi * f * 2 * tt) * vo * 0.012
nhac *= np.minimum(1, t / 2) * np.minimum(1, (TONG - t) / 3)
# hạ nhạc khi có lời
co_loi = np.convolve(np.abs(loi) > 0.02, np.ones(SR // 2) / (SR // 2), mode="same")
nhac *= 1 - 0.6 * np.clip(co_loi * 3, 0, 1)

tron = loi + nhac
tron /= max(1e-6, np.abs(tron).max()) / 0.85
with wave.open(f"{TMP}/tron.wav", "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((tron * 32767).astype(np.int16).tobytes())

subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", VAO, "-i", f"{TMP}/tron.wav", "-map", "0:v", "-map", "1:a",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", RA], check=True)
print("xong:", RA)
