from pytube import YouTube
from config import *
import os

class video_crawler:
    def __init__(self, url):
        self.yt = YouTube(url)
        self.video_path = None
        self.video_name = None
    
    def run(self):
        self.video_path = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(VIDEO_DIR)
        self.video_name = os.path.basename(self.video_path)
        # print("Save to ",self.video_path)
        # print(self.video_name)
        return self

if __name__ == "__main__":
    print("Enter URL: ")
    url = input()
    video_crawler(url).run()