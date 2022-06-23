import imageio
from moviepy.editor import *

limit=13  # Time in sec for each video
sTime=1
etime=0
count=0
looper=True
while looper:
    orignal = VideoFileClip(r"C:\Users\Mouad\Videos\123.mp4") # video with audio

 #  orignal1=VideoFileClip(r"C:\Users\Mouad\Videos\123.mp4")  # video without audio
 #  orignal = orignal1.without_audio()  # video without audio
    if etime <  orignal.duration-limit:
        etime=sTime+limit
    else :
        etime=orignal.duration
        looper=False
    fi=orignal.subclip(sTime,etime)
    stre="video{}.mp4"

    res=stre.format(count)
    count=count+1
    print(res)
    fi.write_videofile(res)
    fi.close()
    sTime=etime
    if sTime==orignal.duration:
        break


print("finish")
