##from pytube import YouTube
##
##yt = YouTube(str(input("Enter the video link: ")))
##videos = yt.get_videos()
##
##s = 1
##for v in videos:
##    print(str(s)+". "+str(v))
##    s += 1
##
##n = int(input("Enter the number of the video: "))
##vid = videos[n-1]
##
##destination = str(input("Enter the destination: "))
##vid.download(destination)
##
##print(yt.filename+"\nHas been successfully downloaded")

##THIS WORKS!!!!!!!!!!!!!!!!!!!!
from pytube import YouTube
url = input("Enter the video link: ")
yt=YouTube(url)
print(yt.title)
t=yt.streams.filter(only_audio=True)
t[0].download(".\songs")
