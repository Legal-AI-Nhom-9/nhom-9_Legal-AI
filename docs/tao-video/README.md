# Dựng lại video

Chạy từ thư mục gốc của kho (cần Node.js + Playwright, Python + Pillow, ffmpeg):

```bash
node docs/tao-video/svg-sang-png.js
python3 docs/tao-video/make_video.py
```

Kết quả: `video/legal-ai-video.mp4` (88 giây) và `video/poster-video.jpg`.
