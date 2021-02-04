import pafy
import ffmpeg
url=input(":")
video=pafy.new(url)
audiostreams=video.audiostreams
#we get a list of audiostreams
for i in audiostreams:
    print("bitrate: %s,ext: %s,size: %0.2fMb" %(i.bitrate,i.exxtensions,i.get_filesize()/1024/1024))
    
