import os, subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

IMG = "build_video/png"  # PNG chuyển từ imgs/*.svg bằng svg-sang-png.js
OUT = "build_video"
os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080
NAVY = (10, 27, 43); CREAM = (247, 241, 232); CAM = (244, 131, 31); SAND = (241, 231, 216); INK = (43, 38, 32)
F = "/usr/share/fonts/truetype/dejavu/"
def font(sz, bold=False): return ImageFont.truetype(F + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), sz)

def ai_tag(d, dark=True):
    t = "Nội dung có sử dụng AI tạo sinh"
    f = font(26)
    w = d.textlength(t, font=f)
    d.rounded_rectangle((W - w - 90, 40, W - 40, 92), 8, outline=CAM, width=2, fill=NAVY if dark else CREAM)
    d.text((W - w - 65, 50), t, font=f, fill=CAM)

def subtitle(d, text):
    f = font(46)
    lines = textwrap.wrap(text, 56)
    lh = 62; h = lh * len(lines) + 40
    y0 = H - h - 50
    d.rectangle((0, y0, W, H - 50 + 0), fill=(10, 27, 43))
    for i, ln in enumerate(lines):
        w = d.textlength(ln, font=f)
        d.text(((W - w) / 2, y0 + 20 + i * lh), ln, font=f, fill=CREAM)

def fit(path, bg):
    im = Image.open(path).convert("RGB")
    c = Image.new("RGB", (W, H), bg)
    blur = im.resize((W, int(W * im.height / im.width))).filter(ImageFilter.GaussianBlur(40))
    c.paste(blur, (0, (H - blur.height) // 2))
    s = min(W / im.width, (H - 40) / im.height)
    im = im.resize((int(im.width * s), int(im.height * s)))
    c.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
    return c

def card(kicker, title, body=None, bg=NAVY, fg=CREAM):
    c = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(c)
    d.text((160, 300), kicker.upper(), font=font(30), fill=CAM)
    y = 360
    for ln in textwrap.wrap(title, 30):
        d.text((160, y), ln, font=font(84, True), fill=fg); y += 104
    if body:
        y += 30
        for ln in textwrap.wrap(body, 62):
            d.text((160, y), ln, font=font(40), fill=fg); y += 58
    d.text((160, H - 120), "§  LEGAL AI", font=font(30, True), fill=CAM)
    return c

scenes = []  # (image, seconds)
c = card("Đồ án AI ứng dụng · Video minh hoạ", "Chín mươi giây để hiểu Legal AI", "Nhân vật Lan là nhân vật hư cấu. Video chỉ dùng hình minh hoạ, không dùng hình hay giọng người thật.")
scenes.append((c, 7))
c = card("Cuối tháng · Khu trọ gần trường", "Báo trước 30 ngày, vẫn bị giữ cọc", "Lan chuyển trọ. Bạn đã báo chủ trọ trước một tháng, nhưng ba triệu tiền cọc vẫn chưa được trả lại.")
scenes.append((c, 9))
c = card("Vấn đề", "Hỏi trên mạng: mỗi nơi nói một kiểu", "Thuê luật sư cho khoản cọc ba triệu thì ít ai nghĩ tới. Còn tự đọc luật thì văn bản dài, khó hiểu và hay được sửa đổi.")
scenes.append((c, 10))
c = fit(f"{IMG}/frame.png", NAVY); d = ImageDraw.Draw(c)
subtitle(d, "Lan mở Legal AI và hỏi bằng tiếng Việt đời thường, như nhắn tin cho bạn.")
scenes.append((c, 10))
c = fit(f"{IMG}/hero.png", NAVY); d = ImageDraw.Draw(c)
subtitle(d, "Câu trả lời ngắn, dễ hiểu, kèm tên văn bản, số điều và đường dẫn tới văn bản gốc.")
scenes.append((c, 10))
c = card("Tự kiểm tra", "Đặt cọc: Điều 328 Bộ luật Dân sự 2015", "Lan bấm vào, tự đọc quy định về đặt cọc và đối chiếu với điều khoản tiền cọc trong chính hợp đồng thuê của mình.", bg=SAND, fg=INK)
scenes.append((c, 10))
c = card("Khi nào cần luật sư", "Còn tranh chấp? Legal AI nói thẳng", "Ứng dụng chỉ Lan tới luật sư hoặc Trung tâm trợ giúp pháp lý nhà nước, thay vì đoán thay.")
scenes.append((c, 8))
c = fit(f"{IMG}/iris.png", NAVY); d = ImageDraw.Draw(c)
subtitle(d, "Ba việc quen thuộc của người trẻ: thuê trọ, hợp đồng lao động, mua bán online.")
scenes.append((c, 8))
c = fit(f"{IMG}/poster.png", CREAM); d = ImageDraw.Draw(c)
subtitle(d, "Hỏi bằng tiếng Việt · Đọc điều luật gốc · Biết khi nào cần luật sư.")
scenes.append((c, 8))
c = fit(f"{IMG}/chu-de.png", NAVY); d = ImageDraw.Draw(c)
subtitle(d, "Legal AI · Hỏi luật dễ như nhắn tin. Thông tin tham khảo, không thay thế tư vấn của luật sư.")
scenes.append((c, 8))

clips = []
for i, (im, sec) in enumerate(scenes):
    d = ImageDraw.Draw(im); ai_tag(d, dark=True)
    p = f"{OUT}/s{i}.png"; im.save(p)
    out = f"{OUT}/c{i}.mp4"; fr = sec * 30
    vf = (f"scale=2880:-2,zoompan=z='1+0.04*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1280x720:fps=30,"
          f"fade=t=in:st=0:d=0.6,fade=t=out:st={sec-0.6}:d=0.6,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", p, "-t", str(sec), "-vf", vf,
                    "-c:v", "libx264", "-crf", "24", "-preset", "medium", out], check=True)
    clips.append(out)
with open(f"{OUT}/list.txt", "w") as f:
    f.writelines(f"file '{c}'\n" for c in clips)
final = "video/legal-ai-video.mp4"
os.makedirs(os.path.dirname(final), exist_ok=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
                "-f", "lavfi", "-t", str(sum(s for _, s in scenes)), "-i", "anullsrc=r=44100:cl=stereo",
                "-c:v", "copy", "-c:a", "aac", "-shortest", "-movflags", "+faststart", final], check=True)
# poster frame
Image.open(f"{OUT}/s0.png").resize((1280, 720)).save("video/poster-video.jpg", quality=85)
print("total", sum(s for _, s in scenes))
