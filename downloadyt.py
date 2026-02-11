#  YouTube can sometimes reject pytube's internal API request due to the frequent changes in YouTube's APi. 

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/home/<username>/<folder>')

print("Download complete")



# Upgrade pytube in case of errors using this code: 
# pip install --upgrade pytube