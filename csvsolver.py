import pandas as pd
import os
import xlsxwriter
from PIL import Image
from config import *
class sheet_writer():
    def __init__(self, name):
        self.book = xlsxwriter.Workbook(f"{name}.xlsx")
        self.sheet = self.book.add_worksheet("res")
        self.sheet.write("A1","Task description")
        self.sheet.write("B1","natrual language(optional)")
        self.sheet.write("C1","start scene")
        self.sheet.write("D1","intermediate scene 1")
        self.sheet.write("E1","interm 2")
        self.sheet.write("F1","interm 3")
        self.sheet.write("G1","end scene")
        self.sheet.write("H1","URL")

        self.image_width = 60
        self.cell_width = 15
        self.cell_height = 80
        self.sheet.set_column("A:H", self.cell_width)

    def run(self, row, name, URL, dir):
        self.sheet.set_row(row-1, self.cell_height)
        res_dir = os.path.join(RESULT_DIR, dir)
        list = os.listdir(res_dir)

        list.sort(key=lambda x:int(x.split('.')[0].removeprefix("frame")))
        
        for i in range(len(list)):
            #print("try to save",i,list[i])
            path = os.path.join(res_dir, list[i])
            im = Image.open(path)
            x_scale = self.image_width / im.size[0]
            y_scale = x_scale

            self.sheet.insert_image(
                chr(ord('C')+i)+str(row),
                path,
                {"x_scale": x_scale, "y_scale": y_scale},
            )
        self.sheet.write('A'+str(row), name)
        self.sheet.write('H'+str(row), URL)

    def close(self):
        self.book.close()