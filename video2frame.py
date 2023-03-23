import cv2
import os
from config import *

class video2frame:
    
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(VIDEO_DIR, name)
        self.stride = 8
        print(self.path)

    def run(self):
        vidcap = cv2.VideoCapture(self.path)
        success,image = vidcap.read()
        count = 0
        while success:
            path  = os.path.join(FRAME_DIR, "frame%d.jpg" % count)
            if count % self.stride == 0:
                cv2.imwrite(path, image)     # save frame as JPEG file      
            success, image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1
        print("count: ",count)
    
if __name__ == "__main__":
    print("Enter video name:")
    name = input()
    video2frame(name).run()