from config import *
from crawler import video_crawler
from video2frame import video2frame
from feature_extractor import generate
from kmeans import K_means_solver
from utils import delete_files_in_dir
import os
import cv2

def save_results(res):
    for i in res:
        fname = f'frame{i}{os.path.splitext(os.listdir(FRAME_DIR)[0])[-1]}'
        read_path = os.path.join(FRAME_DIR, fname)
        im = cv2.imread(read_path)
        write_path = os.path.join(RESULT_DIR, fname)
        cv2.imwrite(write_path, im)

def clear():
    delete_files_in_dir(VIDEO_DIR)
    delete_files_in_dir(FRAME_DIR)
    delete_files_in_dir(FEATURE_DIR)
    delete_files_in_dir(RESULT_DIR)

if __name__ == "__main__":
    print("Enter URL: ")
    url = input()
    clear()
    crawler = video_crawler(url).run()
    video2frame(crawler.video_name).run()
    generate()
    res = K_means_solver().timelist()
    print(res)
    save_results(res)