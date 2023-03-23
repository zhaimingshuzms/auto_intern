import torch
import clip
import torch.nn as nn
from config import *
import os
from PIL import Image
import numpy as np

class clip_extractor(nn.Module):
    def __init__(self, model = 'vit14'):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        super().__init__()
        if model == 'vit14':
            self.model, self.preprocess = clip.load('ViT-L/14', self.device)
        elif model == 'vit16':
            self.model, self.preprocess = clip.load('ViT-B/16', self.device)
        elif model == 'vit32':
            self.model, self.preprocess = clip.load('ViT-B/32', self.device)
        else:
            raise Exception('Invalid model name: {}'.format(model))
    
    def preprocess(self, im):
        return self.preprocess(im).unsqueeze(0).to(self.device)

    def generate_feature(self, im):
        with torch.no_grad():

            target_feature = self.model.encode_image(im)
            target_feature = target_feature / \
                target_feature.norm(dim=1, keepdim=True)
            return target_feature
    
    def forward(self, im):
        return self.generate_feature(im)

def generate():
    model = clip_extractor()
    rgbs = []
    timelist = []
    for name in os.listdir(FRAME_DIR):
        path = os.path.join(FRAME_DIR, name)
        rgb = Image.open(path).convert('RGB')
        rgbs.append(model.preprocess(rgb))
        timelist.append(int(os.path.splitext(name)[0].removeprefix("frame")))
    ret = model(torch.tensor(np.stack(rgbs)).to(model.device)) # risk of CUDA out of memory
    ret = torch.cat((ret, torch.tensor(timelist).to(model.device).unsqueeze(1)), dim = 1)
    # print(ret.shape)
    path = os.path.join(FEATURE_DIR, FEATURE_FNAME)
    torch.save(ret, path)

if __name__ == "__main__":
    generate()