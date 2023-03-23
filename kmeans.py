import torch
import os
from config import *
from sklearn.cluster import KMeans
import numpy as np

class K_means_solver:
    
    def __init__(self):
        self.path = os.path.join(FEATURE_DIR, FEATURE_FNAME)
        self.x = torch.load(self.path, map_location=torch.device("cpu"))
        assert self.x.ndim == 2
        self.kmeans = KMeans(n_clusters=5).fit(self.x)

    def run(self):
        distance = self.kmeans.transform(self.x)
        category = self.kmeans.labels_
        # for i in range(len(distance)):
        #     print(i*8,distance[i],category[i])
        dict = {}
        out = {}
        for ind in range(self.x.size(0)):
            catg = category[ind]
            if dict.get(catg):
                dict[catg] = min(dict[catg],distance[ind][catg])
                out[catg] = ind
            else:
                dict[catg] = distance[ind][catg]
                out[catg] = ind
        return out
    
    def timelist(self):
        out = self.run()
        ret = [int(self.x[i][-1]) for i in out.values()]
        return ret
        
if __name__ == "__main__":
    print(K_means_solver().timelist())

