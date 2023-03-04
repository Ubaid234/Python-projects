from pytube import Playlist

py = Playlist("ww.youtube.com/playlist?list=PLu0W_9lII9ahwLNzab_rVfZ06ZCZYEcNs")

print(f'Downloading : {py.title}')

for video in py.videos: 
    video.streams.first().download()
 