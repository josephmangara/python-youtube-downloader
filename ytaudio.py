import sys
from yt_dlp import YoutubeDL

link = sys.argv[1]

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "/home/mangara/H/%(title)s.%(ext)s",
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=True)
    print("Title:", info.get("title"))