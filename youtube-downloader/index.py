from pytube import YouTube

link = "https://www.youtube.com/watch?v=EAYlckSaviI&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=12"

youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_audio=True) 
vid = list(enumerate(videos))

for i in vid:
    print(i)
print()

strm = int(input("enter: "))
videos[strm].download()
print("Successfully Downloaded")

