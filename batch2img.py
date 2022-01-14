import string
import numpy as np
import cv2, os, random, glob
from matplotlib import pyplot as plt
from collections import Counter



if __name__ == '__main__':
    import argparse
    import glob

    parser = argparse.ArgumentParser()

    parser.add_argument('--batch_name', type=str, default="batch_en",
                        help="batch file name")
    parser.add_argument('--side', type=str, default="F",
                        help="frontside(F)/backside(B)")
    parser.add_argument('--language', type=str, default="en",
                        help="language of the batch")

    args = parser.parse_args()
    batch_name = args.batch_name
    side = args.side
    language = args.language
    batch_path = './Batch/'+batch_name+'.jpg'
    x = [100, 1800, 3500, 5200]
    y = [200, 2600, 5000, 7400]
    h = 2300
    w = 1700

    for i in range(4):
        for j in range(4):
            index = len(glob.glob1("./OriginalImages","*.jpg"))
            img = cv2.imread(batch_path)
            crop_img = img[y[i]:y[i]+h, x[j]:x[j]+w] #crop
            cv2.imwrite('./OriginalImages/PKM_'+str(index).zfill(3)+side+'_'+language+'.jpg', crop_img)

