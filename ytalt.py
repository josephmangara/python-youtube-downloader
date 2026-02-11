import sys
from yt_dlp import YoutubeDL

link = sys.argv[1]

ydl_opts = {
    "format": "bestvideo+bestaudio/best",

    # Update the download path to match your pc's file structure. 
    "outtmpl": "/home/mangara/H/%(title)s.%(ext)s", 

    "writesubtitles": False,
    "writeautomaticsub": False,
    "writethumbnail": False,
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=True)
    print("Title:", info.get("title"))
    print("Resolution:", info.get("resolution"))