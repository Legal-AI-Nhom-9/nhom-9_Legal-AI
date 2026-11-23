"""Vẽ các hình minh hoạ có nhân vật (dạng phẳng, không vẽ mặt, nhân vật hư cấu) cho trang và video.

Chạy từ thư mục gốc của kho:  python3 docs/tao-video/ve_canh.py
Tạo ra trong imgs/:
  nen-phien-toa.svg  — nền Mục 1: phòng xử án
  nen-luat-su.svg    — nền Mục 2: luật sư làm việc bên bàn
  canh-1-boi-canh.svg, canh-2-van-de.svg, canh-3-hoi.svg,
  canh-4-doi-chieu.svg, canh-5-luat-su.svg — các cảnh của video
Không dùng ảnh, khuôn mặt hay giọng nói của người thật.
"""
import os

NAVY, NAVY2, BLUE = "#0A1B2B", "#12293F", "#1A3C6E"
CAM, CAM_D, CAM_S = "#F4831F", "#C4640D", "#F8A85F"
KEM, SAND, SAND2, INK = "#F7F1E8", "#F1E7D8", "#E5D9C6", "#2B2620"
DA, TOC, GO, GO_D = "#E9B48C", "#2B2620", "#8A5A3B", "#6B432B"
FONT = 'font-family="Segoe UI,Arial,sans-serif"'
OUT = "imgs"


def svg(w, h, body, nen=None):
    bg = f'<rect width="{w}" height="{h}" fill="{nen}"/>' if nen else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {FONT}>{bg}{body}</svg>\n'


def tay(pts, mau, w=26):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    hx, hy = pts[-1]
    return (f'<path d="{d}" fill="none" stroke="{mau}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{hx}" cy="{hy}" r="{w*0.5}" fill="{DA}"/>')


def dau(cx, cy, toc="nu", r=40, huong=0):
    """Đầu không vẽ mặt. huong: -1 nhìn trái, 1 nhìn phải, 0 nhìn thẳng."""
    s = ""
    if toc == "nu":
        s += f'<path d="M{cx-r-8} {cy-6} Q{cx-r-10} {cy+r+60} {cx-r+6} {cy+r+70} L{cx+r-6} {cy+r+70} Q{cx+r+10} {cy+r+60} {cx+r+8} {cy-6} Z" fill="{TOC}"/>' if huong == 0 else \
             f'<path d="M{cx-huong*(r+10)} {cy-10} Q{cx-huong*(r+14)} {cy+r+50} {cx-huong*(r-14)} {cy+r+64} L{cx+huong*4} {cy+r+20} Z" fill="{TOC}"/>'
    s += f'<rect x="{cx-12}" y="{cy+r-8}" width="24" height="30" fill="{DA}"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{DA}"/>'
    if toc == "nu":
        s += f'<path d="M{cx-r-4} {cy+4} Q{cx-r} {cy-r-14} {cx} {cy-r-8} Q{cx+r} {cy-r-14} {cx+r+4} {cy+4} Q{cx+huong*14} {cy-r+18} {cx-r-4} {cy+4} Z" fill="{TOC}"/>'
    elif toc == "nam":
        s += f'<path d="M{cx-r-2} {cy} Q{cx-r} {cy-r-12} {cx} {cy-r-10} Q{cx+r} {cy-r-12} {cx+r+2} {cy} Q{cx+r-10} {cy-r+10} {cx} {cy-r+12} Q{cx-r+10} {cy-r+10} {cx-r-2} {cy} Z" fill="#8C8A86"/>'
    if huong:
        s += f'<path d="M{cx+huong*(r-2)} {cy+2} l{huong*10} 8 l{-huong*10} 4 Z" fill="{DA}"/>'
    return s


def dung(x, y, ao=CAM, quan=BLUE, toc="nu", tay_trai=None, tay_phai=None, vest=False):
    """Người đứng nhìn thẳng; (x, y) là điểm giữa hai bàn chân."""
    s = f'<rect x="{x-36}" y="{y-200}" width="32" height="196" rx="15" fill="{quan}"/>'
    s += f'<rect x="{x+4}" y="{y-200}" width="32" height="196" rx="15" fill="{quan}"/>'
    s += f'<ellipse cx="{x-24}" cy="{y}" rx="26" ry="11" fill="{INK}"/><ellipse cx="{x+24}" cy="{y}" rx="26" ry="11" fill="{INK}"/>'
    s += dau(x, y - 405, toc)
    s += f'<rect x="{x-62}" y="{y-350}" width="124" height="172" rx="44" fill="{ao}"/>'
    if vest:
        s += f'<path d="M{x-16} {y-350} L{x} {y-300} L{x+16} {y-350} Z" fill="#fff"/><path d="M{x-5} {y-330} L{x+5} {y-330} L{x+3} {y-280} L{x-3} {y-280} Z" fill="{CAM}"/>'
    tl = tay_trai or [(x - 58, y - 330), (x - 74, y - 250), (x - 70, y - 180)]
    tp = tay_phai or [(x + 58, y - 330), (x + 74, y - 250), (x + 70, y - 180)]
    return s + tay(tl, ao) + tay(tp, ao)


def ngoi(x, y, ao=CAM, quan=BLUE, toc="nu", tay_pts=None, tay2=None, huong=1, vest=False):
    """Người ngồi nhìn nghiêng; (x, y) là điểm hông trên mặt ghế; huong=1 quay phải, -1 quay trái."""
    h = huong
    s = f'<rect x="{x if h>0 else x-130}" y="{y-34}" width="130" height="42" rx="19" fill="{quan}"/>'
    s += f'<rect x="{x+h*100-17}" y="{y-20}" width="34" height="150" rx="15" fill="{quan}"/>'
    s += f'<ellipse cx="{x+h*118}" cy="{y+132}" rx="28" ry="11" fill="{INK}"/>'
    if tay2:
        s += tay(tay2, ao)
    s += f'<rect x="{x-38}" y="{y-178}" width="76" height="182" rx="32" fill="{ao}"/>'
    if vest:
        s += f'<path d="M{x+h*14} {y-176} L{x+h*36} {y-176} L{x+h*30} {y-120} Z" fill="#fff"/>'
    s += dau(x + h * 6, y - 222, toc, r=38, huong=h)
    s += tay(tay_pts or [(x + h * 8, y - 150), (x + h * 50, y - 80), (x + h * 120, y - 92)], ao)
    return s


def ghe(x, y, h=1):
    bx = x - h * 50
    return (f'<rect x="{bx-12}" y="{y-150}" width="24" height="160" rx="10" fill="{NAVY2}"/>'
            f'<rect x="{x-60}" y="{y+4}" width="120" height="20" rx="8" fill="{NAVY2}"/>'
            f'<rect x="{x-6}" y="{y+20}" width="12" height="120" fill="{NAVY2}"/>'
            f'<rect x="{x-50}" y="{y+136}" width="100" height="10" rx="5" fill="{NAVY2}"/>')


def ban(x, y, w, h=24, chan=True, mau=GO):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{mau}"/>'
    if chan:
        s += f'<rect x="{x+20}" y="{y+h}" width="18" height="{820-y-h}" fill="{GO_D}"/><rect x="{x+w-38}" y="{y+h}" width="18" height="{820-y-h}" fill="{GO_D}"/>'
    return s


def chu(x, y, t, size=28, mau=INK, w=400, anchor="start", it=False):
    st = ' font-style="italic"' if it else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{mau}" text-anchor="{anchor}"{st}>{t}</text>'


def bong(x, y, w, h, dong, mau=KEM, chu_mau=INK, duoi="trai", size=26, dam=False):
    tx = x + 40 if duoi == "trai" else x + w - 40
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="{mau}"/>'
    s += f'<path d="M{tx-16} {y+h-2} L{tx-30 if duoi=="trai" else tx+30} {y+h+34} L{tx+16} {y+h-2} Z" fill="{mau}"/>'
    for i, d in enumerate(dong):
        s += chu(x + 28, y + 46 + i * (size + 12), d, size, chu_mau, 700 if (dam and i == 0) else 400)
    return s


def tuong_san(mau_tuong=SAND, mau_san=SAND2, san_y=820):
    return f'<rect width="1600" height="1000" fill="{mau_tuong}"/><rect y="{san_y}" width="1600" height="{1000-san_y}" fill="{mau_san}"/>'


def can_can(cx, cy, k=1, mau=CAM, sw=6):
    return (f'<g fill="none" stroke="{mau}" stroke-width="{sw}" stroke-linecap="round">'
            f'<path d="M{cx} {cy} v{150*k} M{cx-90*k} {cy+20*k} h{180*k} M{cx-60*k} {cy+150*k} h{120*k}"/>'
            f'<path d="M{cx-90*k} {cy+20*k} l-34 {70*k} h68 Z M{cx+90*k} {cy+20*k} l-34 {70*k} h68 Z"/></g>'
            f'<circle cx="{cx}" cy="{cy}" r="{9*k}" fill="{mau}"/>')


def ke_sach(x, y, w, tang=4):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{tang*110+20}" fill="{GO_D}"/>'
    mau = [BLUE, "#7A2E2E", NAVY2, "#3E5C3A", CAM_D, "#4A4A6A"]
    for t in range(tang):
        yy = y + 14 + t * 110
        s += f'<rect x="{x+10}" y="{yy}" width="{w-20}" height="96" fill="#5A3826"/>'
        bx, i = x + 16, 0
        while bx < x + w - 40:
            bw = 22 + (i * 7) % 14
            bh = 70 + (i * 11) % 22
            s += f'<rect x="{bx}" y="{yy+96-bh}" width="{bw}" height="{bh}" rx="3" fill="{mau[(i+t)%len(mau)]}"/>'
            bx += bw + 4
            i += 1
    return s


def ghi(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)
    print("đã vẽ", name)


# ───────── Nền Mục 1: phòng xử án ─────────
b = '<rect width="1600" height="1000" fill="#E9DCC7"/>'
for cx in (140, 420, 1180, 1460):
    b += f'<rect x="{cx-46}" y="60" width="92" height="760" fill="#DCCBB0"/><rect x="{cx-62}" y="40" width="124" height="30" fill="#CDB896"/><rect x="{cx-62}" y="810" width="124" height="30" fill="#CDB896"/>'
    for k in range(-2, 3):
        b += f'<rect x="{cx+k*16-3}" y="80" width="6" height="720" fill="#CDB896"/>'
b += f'<rect x="560" y="70" width="480" height="340" rx="6" fill="#DCCBB0"/>' + can_can(800, 120, 1.1, CAM_D, 8)
for jx in (650, 800, 950):
    b += f'<rect x="{jx-60}" y="330" width="120" height="250" rx="16" fill="{GO_D}"/>'
    b += f'<circle cx="{jx}" cy="445" r="34" fill="{DA}"/><path d="M{jx-36} {445} Q{jx-34} {400} {jx} {404} Q{jx+34} {400} {jx+36} 445 Q{jx+20} 420 {jx-36} 445 Z" fill="#8C8A86"/>'
    b += f'<path d="M{jx-70} 600 Q{jx-66} 480 {jx} 476 Q{jx+66} 480 {jx+70} 600 Z" fill="{NAVY}"/><path d="M{jx-12} 478 L{jx} 520 L{jx+12} 478 Z" fill="#fff"/>'
b += f'<rect x="430" y="560" width="740" height="60" rx="6" fill="{GO}"/><rect x="460" y="620" width="680" height="200" fill="{GO_D}"/>'
b += f'<rect x="470" y="640" width="200" height="160" rx="6" fill="{GO}" opacity=".5"/><rect x="700" y="640" width="200" height="160" rx="6" fill="{GO}" opacity=".5"/><rect x="930" y="640" width="200" height="160" rx="6" fill="{GO}" opacity=".5"/>'
b += f'<rect x="1000" y="534" width="70" height="26" rx="6" fill="#5A3826"/><rect x="1010" y="500" width="90" height="22" rx="10" fill="#5A3826" transform="rotate(-20 1050 511)"/>'
b += f'<rect x="0" y="840" width="1600" height="160" fill="#CDB896"/>'
for px in (120, 1290):
    b += f'<rect x="{px}" y="700" width="200" height="40" rx="8" fill="{GO}"/><rect x="{px+20}" y="740" width="20" height="100" fill="{GO_D}"/><rect x="{px+160}" y="740" width="20" height="100" fill="{GO_D}"/>'
b += ngoi(230, 700, ao=NAVY, quan=NAVY2, toc="nam", huong=1, vest=True, tay_pts=[(238, 560), (290, 640), (330, 700)])
b += dung(1420, 840, ao=BLUE, quan=NAVY2, toc="nu", vest=True, tay_trai=[(1362, 510), (1320, 590), (1300, 650)], tay_phai=[(1478, 510), (1500, 600), (1480, 670)])
ghi("nen-phien-toa.svg", svg(1600, 1000, b))

# ───────── Nền Mục 2: luật sư làm việc ─────────
b = '<rect width="1600" height="1000" fill="#EFE5D6"/>'
b += ke_sach(80, 120, 520) + ke_sach(1000, 120, 520)
b += f'<rect x="640" y="140" width="320" height="220" rx="10" fill="#E2D3BC"/>' + can_can(800, 175, 0.9, CAM_D, 7)
b += dung(800, 820, ao=NAVY, quan=NAVY2, toc="nam", vest=True, tay_trai=[(742, 490), (700, 570), (720, 640)], tay_phai=[(858, 490), (900, 560), (880, 640)])
b += f'<rect x="300" y="640" width="1000" height="40" rx="8" fill="{GO}"/><rect x="330" y="680" width="940" height="160" fill="{GO_D}"/>'
b += f'<rect x="430" y="596" width="190" height="44" rx="4" fill="{BLUE}"/><rect x="440" y="560" width="170" height="36" rx="4" fill="#7A2E2E"/><rect x="450" y="528" width="150" height="32" rx="4" fill="{NAVY2}"/>'
b += f'<rect x="980" y="610" width="220" height="30" rx="4" fill="#fff" transform="rotate(-6 1090 625)"/><rect x="1000" y="602" width="200" height="6" fill="{SAND2}" transform="rotate(-6 1090 625)"/>'
b += f'<rect x="0" y="840" width="1600" height="160" fill="#D8C7AA"/>'
ghi("nen-luat-su.svg", svg(1600, 1000, b))

# ───────── Cảnh 1: bối cảnh — tối, phòng trọ, cầm hợp đồng ─────────
b = tuong_san()
b += f'<rect x="130" y="110" width="360" height="330" rx="8" fill="{NAVY}" stroke="#fff" stroke-width="14"/><path d="M310 110 V440 M130 275 H490" stroke="#fff" stroke-width="10"/>'
b += f'<circle cx="400" cy="190" r="34" fill="{KEM}"/><circle cx="384" cy="182" r="30" fill="{NAVY}"/>'
for sx, sy in ((180, 160), (240, 330), (420, 360), (200, 250)):
    b += f'<circle cx="{sx}" cy="{sy}" r="4" fill="{KEM}"/>'
b += chu(310, 500, "22:00", 34, INK, 700, "middle")
for bx, by, bw, bh in ((1120, 620, 240, 200), (1360, 660, 180, 160), (1180, 450, 190, 170)):
    b += f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#C9A47A"/><rect x="{bx+bw/2-14}" y="{by}" width="28" height="{bh}" fill="#B38C5F"/>'
b += chu(1240, 690, "CHUYỂN NHÀ", 22, "#7A5A36", 700, "middle")
b += f'<g transform="rotate(-6 560 440)"><rect x="480" y="350" width="170" height="210" rx="6" fill="#fff" stroke="{SAND2}" stroke-width="3"/>' + chu(565, 388, "HỢP ĐỒNG", 18, CAM_D, 800, "middle") + chu(565, 412, "THUÊ PHÒNG", 18, CAM_D, 800, "middle")
for i in range(6):
    b += f'<rect x="502" y="{432+i*18}" width="{126-(i%3)*18}" height="7" rx="3" fill="{SAND2}"/>'
b += '</g>'
b += dung(800, 820, ao=CAM, tay_trai=[(742, 470), (690, 540), (640, 500)], tay_phai=[(858, 470), (884, 560), (870, 640)])
b += bong(900, 140, 560, 150, ["Đã trả phòng, báo trước", "30 ngày… sao chưa trả cọc?"], KEM, INK, "trai", 32, True)
b += chu(1180, 340, "3.000.000đ", 46, CAM_D, 800, "middle")
ghi("canh-1-boi-canh.svg", svg(1600, 1000, b))

# ───────── Cảnh 2: vấn đề — tra mạng, mỗi nơi một kiểu ─────────
b = tuong_san("#E9DECB")
b += ban(250, 560, 520) + ghe(380, 600, 1)
b += f'<path d="M560 560 L600 430 L740 430 L720 560 Z" fill="#C8CDD6"/><rect x="520" y="552" width="230" height="10" rx="4" fill="#9AA3B2"/>'
b += ngoi(380, 600, ao=CAM, tay_pts=[(388, 450), (430, 380), (418, 330)], tay2=[(372, 460), (440, 530), (540, 548)])
for i, (tt, nd, x, y, r) in enumerate((("Diễn đàn", "“Chủ trọ được giữ cọc!”", 860, 110, -3),
                                       ("Bài viết cũ (2016)", "“Phải trả gấp đôi tiền cọc”", 990, 330, 2),
                                       ("Nhóm mạng xã hội", "“Tuỳ chủ nhà thôi bạn ơi”", 840, 560, -2))):
    b += f'<g transform="rotate({r} {x+280} {y+90})"><rect x="{x}" y="{y}" width="560" height="190" rx="14" fill="#fff" stroke="{SAND2}" stroke-width="3"/>'
    b += f'<rect x="{x}" y="{y}" width="560" height="46" rx="14" fill="{NAVY2}"/><rect x="{x}" y="{y+30}" width="560" height="16" fill="{NAVY2}"/>'
    b += ''.join(f'<circle cx="{x+26+k*22}" cy="{y+23}" r="7" fill="{c}"/>' for k, c in enumerate(("#E36B5B", "#E8B44B", "#6DB46D")))
    b += chu(x + 100, y + 32, tt, 22, KEM, 600) + chu(x + 30, y + 112, nd, 32, INK, 700)
    b += f'<rect x="{x+30}" y="{y+140}" width="380" height="10" rx="5" fill="{SAND2}"/></g>'
for qx, qy, qs in ((560, 260, 90), (700, 200, 64), (470, 190, 56)):
    b += chu(qx, qy, "?", qs, CAM, 800, "middle")
ghi("canh-2-van-de.svg", svg(1600, 1000, b))

# ───────── Cảnh 3: bước 1 — hỏi Legal AI trên điện thoại ─────────
b = tuong_san("#E9DECB")
b += dung(560, 820, ao=CAM, tay_trai=[(502, 470), (500, 570), (562, 585)], tay_phai=[(618, 470), (634, 560), (596, 566)])
b += f'<rect x="548" y="520" width="58" height="96" rx="10" fill="{NAVY}" transform="rotate(-8 577 568)"/><rect x="555" y="530" width="44" height="72" rx="5" fill="{BLUE}" transform="rotate(-8 577 568)"/>'
b += '<path d="M630 520 Q760 420 880 380" fill="none" stroke="#C9B89C" stroke-width="5" stroke-dasharray="4 14" stroke-linecap="round"/>'
b += f'<rect x="900" y="70" width="460" height="760" rx="52" fill="{NAVY}"/><rect x="920" y="90" width="420" height="720" rx="38" fill="{KEM}"/>'
b += f'<rect x="920" y="90" width="420" height="96" rx="38" fill="{NAVY2}"/><rect x="920" y="150" width="420" height="36" fill="{NAVY2}"/>'
b += f'<circle cx="976" cy="140" r="22" fill="{CAM}"/>' + chu(976, 148, "L", 22, NAVY, 800, "middle") + chu(1012, 136, "Legal AI", 24, KEM, 700) + chu(1012, 162, "Trợ lý pháp lý", 16, "#B9C3D0")
b += f'<rect x="980" y="230" width="336" height="150" rx="22" fill="{BLUE}"/>'
for i, d in enumerate(("Mình đã trả phòng, báo", "trước 30 ngày mà chủ trọ", "vẫn giữ tiền cọc. Vậy có", "đúng không?")):
    b += chu(1002, 270 + i * 30, d, 21, KEM)
b += f'<rect x="944" y="410" width="120" height="56" rx="22" fill="#fff"/>' + ''.join(f'<circle cx="{976+k*28}" cy="438" r="8" fill="#B9B0A2"/>' for k in range(3))
b += chu(944, 500, "Legal AI đang tra cứu văn bản…", 18, "#8A8174", 400, "start", True)
b += f'<rect x="944" y="730" width="372" height="56" rx="28" fill="#fff" stroke="{SAND2}" stroke-width="2"/>' + chu(972, 766, "Hỏi bằng tiếng Việt đời thường…", 18, "#9A9184")
ghi("canh-3-hoi.svg", svg(1600, 1000, b))

# ───────── Cảnh 4: bước 3 — đối chiếu văn bản gốc ─────────
b = tuong_san("#E9DECB")
b += ban(180, 560, 560) + ghe(300, 600, 1)
b += f'<path d="M470 560 L510 440 L650 440 L630 560 Z" fill="#C8CDD6"/><rect x="440" y="552" width="230" height="10" rx="4" fill="#9AA3B2"/>'
b += ngoi(300, 600, ao=CAM, tay_pts=[(308, 450), (360, 520), (450, 548)])
b += f'<rect x="820" y="80" width="660" height="560" rx="14" fill="#fff" stroke="{SAND2}" stroke-width="3"/>'
b += chu(1150, 140, "BỘ LUẬT DÂN SỰ 2015", 34, NAVY, 800, "middle") + chu(1150, 176, "Luật số 91/2015/QH13", 20, "#7A7062", 400, "middle")
b += chu(870, 240, "Điều 328. Đặt cọc", 30, INK, 800)
b += f'<rect x="860" y="270" width="580" height="160" rx="8" fill="{CAM}" fill-opacity=".18"/><rect x="860" y="270" width="6" height="160" fill="{CAM}"/>'
for i, d in enumerate(("2. Trường hợp hợp đồng được giao kết,", "thực hiện thì tài sản đặt cọc được trả", "lại cho bên đặt cọc hoặc được trừ để", "thực hiện nghĩa vụ trả tiền; …")):
    b += chu(884, 306 + i * 36, d, 24, INK)
for i in range(4):
    b += f'<rect x="870" y="{464+i*30}" width="{540-(i%2)*120}" height="10" rx="5" fill="{SAND2}"/>'
b += '<g fill="none" stroke="' + CAM + '" stroke-width="12" stroke-linecap="round"><circle cx="1360" cy="560" r="70"/><path d="M1410 610 L1480 680"/></g>'
b += f'<g transform="rotate(-5 990 760)"><rect x="840" y="690" width="320" height="150" rx="8" fill="#fff" stroke="{SAND2}" stroke-width="3"/>' + chu(864, 730, "Hợp đồng thuê phòng", 22, CAM_D, 800) + chu(864, 766, "Điều 3. Tiền cọc", 22, INK, 700) + f'<rect x="864" y="786" width="240" height="8" rx="4" fill="{SAND2}"/></g>'
b += f'<circle cx="1260" cy="770" r="40" fill="#3E8E5A"/><path d="M1240 770 l14 14 l26 -30" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>' + chu(1316, 780, "Đối chiếu", 30, "#3E8E5A", 800)
ghi("canh-4-doi-chieu.svg", svg(1600, 1000, b))

# ───────── Cảnh 5: bước 4 — gặp luật sư / trợ giúp pháp lý ─────────
b = tuong_san("#EDE2CF")
b += ke_sach(1080, 90, 440, 3) + f'<rect x="480" y="110" width="440" height="80" rx="8" fill="{NAVY2}"/>' + chu(700, 162, "LUẬT SƯ · TRỢ GIÚP PHÁP LÝ", 28, KEM, 700, "middle")
b += can_can(700, 230, 0.8, CAM_D, 6)
b += ghe(420, 600, 1) + ghe(1000, 600, -1)
b += ngoi(420, 600, ao=CAM, tay_pts=[(428, 450), (480, 520), (580, 548)])
b += ngoi(1000, 600, ao=NAVY, quan=NAVY2, toc="nam", huong=-1, vest=True, tay_pts=[(992, 450), (940, 520), (840, 548)])
b += ban(520, 556, 400)
b += f'<rect x="600" y="532" width="150" height="24" rx="3" fill="#fff"/><rect x="760" y="526" width="120" height="30" rx="3" fill="{BLUE}"/>'
b += bong(90, 200, 460, 124, ["Em đã báo trước 30 ngày", "nhưng chưa được trả cọc."], KEM, INK, "phai", 26)
b += bong(930, 200, 500, 124, ["Mình cùng xem lại hợp đồng", "và trao đổi với chủ trọ nhé."], NAVY2, KEM, "trai", 26)
ghi("canh-5-luat-su.svg", svg(1600, 1000, b))
