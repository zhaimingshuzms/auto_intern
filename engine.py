from config import *
from crawler import video_crawler
from video2frame import video2frame
from feature_extractor import generate
from kmeans import K_means_solver
from utils import delete_files_in_dir
from csvsolver import sheet_writer
from URL import urls
from tqdm import tqdm
import os
import cv2

def save_results(res, dir):
    res_dir = os.path.join(RESULT_DIR, dir)
    os.makedirs(res_dir)
    for i in res:
        fname = f'frame{i}{os.path.splitext(os.listdir(FRAME_DIR)[0])[-1]}'
        read_path = os.path.join(FRAME_DIR, fname)
        im = cv2.imread(read_path)
        write_path = os.path.join(res_dir, fname)
        cv2.imwrite(write_path, im)

def clear():
    delete_files_in_dir(VIDEO_DIR)
    delete_files_in_dir(FRAME_DIR)
    delete_files_in_dir(FEATURE_DIR)

def one_action(url, dir):
    clear()
    crawler = video_crawler(url).run()
    video2frame(crawler.video_name).run()
    generate()
    res = K_means_solver().timelist()
    print(res)
    save_results(res, dir)
    return crawler.video_name

def run():
    s = sheet_writer()
    for i in tqdm(range(len(urls))):
        name = one_action(urls[i], str(i))
        s.run(i+2, name, urls[i], str(i))
    s.close()

if __name__ == "__main__":
    run()