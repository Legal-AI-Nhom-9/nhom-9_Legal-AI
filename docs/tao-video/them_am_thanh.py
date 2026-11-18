"""Thêm lời dẫn (giọng đọc tổng hợp espeak-ng, tiếng Việt) và nhạc nền tự tạo vào video.

Chạy từ thư mục gốc của kho:
    python3 docs/tao-video/them_am_thanh.py [video_vao] [video_ra]
Cần: espeak-ng, ffmpeg, numpy.
Giọng đọc là giọng máy tổng hợp, không phải giọng người thật; nhạc nền do mã tự sinh (hợp âm),
không dùng bản nhạc có bản quyền.
"""
import os, subprocess, sys, wave
import numpy as np

VAO = sys.argv[1] if len(sys.argv) > 1 else "video/legal-ai-video.mp4"
RA = sys.argv[2] if len(sys.argv) > 2 else "video/legal-ai-video-co-tieng.mp4"
TMP = "build_video/audio"
os.makedirs(TMP, exist_ok=True)
SR = 22050

# (giây bắt đầu cảnh, thời lượng cảnh, lời dẫn)
CANH = [
    (0, 7, "Chín mươi giây để hiểu Legal AI."),
    (7, 9, "Lan chuyển trọ. Đã báo trước một tháng, nhưng ba triệu tiền cọc vẫn chưa được trả."),
    (16, 10, "Hỏi trên mạng, mỗi nơi nói một kiểu. Thuê luật sư cho ba triệu thì ít ai nghĩ tới."),
    (26, 10, "Lan mở Legal AI, hỏi bằng tiếng Việt, như nhắn tin cho bạn."),
    (36, 10, "Câu trả lời ngắn, kèm tên văn bản, số điều, và đường dẫn tới văn bản gốc."),
    (46, 10, "Lan tự đọc Điều ba trăm hai mươi tám, Bộ luật Dân sự, về đặt cọc."),
    (56, 8, "Còn tranh chấp, Legal AI chỉ Lan tới luật sư, hoặc trợ giúp pháp lý."),
    (64, 8, "Thuê trọ, lao động, mua bán online."),
    (72, 8, "Hỏi bằng tiếng Việt. Đọc luật gốc. Biết khi nào cần luật sư."),
    (80, 8, "Legal AI. Hỏi luật dễ như nhắn tin."),
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


loi = np.zeros(TONG * SR, dtype=np.float32)
for i, (bd, dai, cau) in enumerate(CANH):
    toc_do = 150
    while True:
        p = f"{TMP}/c{i}.wav"
        subprocess.run(["espeak-ng", "-v", "vi", "-s", str(toc_do), "-p", "45", "-g", "4", "-w", p, cau], check=True)
        x, sr = doc_wav(p)
        x = doi_tan_so(x, sr)
        if len(x) / SR <= dai - 1.2 or toc_do >= 210:
            break
        toc_do += 10
    vt = int((bd + 0.6) * SR)
    loi[vt:vt + len(x)] += x[: len(loi) - vt] * 0.9
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
