import sys
from yt_dlp import YoutubeDL

link = sys.argv[1]

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "/home/mangara/H/%(title)s.%(ext)s",
    "writesubtitles": False,
    "writeautomaticsub": False,
    "writethumbnail": False,
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=True)
    print("Title:", info.get("title"))
    print("Resolution:", info.get("resolution"))