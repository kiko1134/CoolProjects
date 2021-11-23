from pytube import YouTube

path = "/Users/kristianyodanov/Downloads/"
link = input("enter Youtube URL: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("enter the desired option to download the format")
dn_option = int(input("enter the option: "))

dn_video = videos[dn_option]

try:
    dn_video.download(path)
except :
    print("Error downloading video")
print("dowloaded successfully")