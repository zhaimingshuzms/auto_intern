import cv2
import os
from config import *

class video2frame:
    
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(VIDEO_DIR, name)
        self.stride = 8
        # self.lim = 1600
        print(self.path)

    def run(self):
        vidcap = cv2.VideoCapture(self.path)
        success,image = vidcap.read()
        total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.stride = max(total_frames // 200 + 1,4)
        print("total_frames:",total_frames,"stride",self.stride)
        count = 0
        while success:
            path  = os.path.join(FRAME_DIR, "frame%d.jpg" % (count//self.stride))
            if count % self.stride == 0:
                cv2.imwrite(path, image)     # save frame as JPEG file      
            success, image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1
            # if count >= self.lim:
            #     break
        # print("count: ",count)
    
if __name__ == "__main__":
    print("Enter video name:")
    name = input()
    video2frame(name).run()