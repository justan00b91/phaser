import cv2
import numpy as np
import os
from os.path import isfile, join
from moviepy.editor import *

def slice_vid(vid):
    cap = cv2.VideoCapture(vid)
    try:
        if not os.path.exists('data/frames'):
            os.makedirs('data/frames')
    except OSError:
        print('Error: Creating Frames')
    currentFrame = 0
    while(True):
        ret, frames = cap.read()
        name = './data/frames/f' + str(currentFrame) + '.png'
        print('Creating...' + name)
        cv2.imwrite(name, frames)
        currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()

def rem_audio(vid):
    if not os.path.exists('data/audio'):
        os.makedirs('data/audio')
    videoclip=VideoFileClip(vid)
    audioclip=videoclip.audio
    audioclip.write_audiofile("./data/audio/audio.mp3")
    audioclip.close()
    videoclip.close()

def conf2v(cdir, fps, time):
    path = cdir+'/'
    odir = 'data/'+'video.mp4'
    frame_array=[]
    files=[f for f in os.listdir(path)if isfile(join(path,f))]
    for i in range (0,len(files)):
        filename=path+'f'+str(i)+'.png'
        print(filename)
        img=cv2.imread(filename)
        height, width, layers = img.shape
        size=(width, height)

        for j in range(int(time)):
            frame_array.append(img)
    out=cv2.VideoWriter(odir, cv2.VideoWriter_fourcc(*'mp4v'),fps,size)
    for i in range(len(frame_array[i])):
        out.write(frame_array[i])
    out.release()

a = input(f"Choose Convertion Option: \n1)Video to Frames \n2)Video to Sound \n3)Frames to Video \n4)Audio to Video\n>>>")
if (a == '1'):
    vid = input(f"\nEnter file name\n>>>")
    slice_vid(vid)
elif (a == '2'):
    vid = input(f"\nEnter file name\n>>>")
    rem_audio(vid)
elif (a == '3'):
    cdir = input(f"Enter directory name(one with frames)\n>>>")
    fps = int(input(f"FPS\n>>>"))
    time = input(f"Time\n>>>")
    conf2v(cdir, fps, time)
else:
    print(f"ERROR!\n")
