import string
import cv2, os, random, glob
from crop_img import crop_img
from config import *

def defects(x):
    return {
        '0': "/NoDefect",
        '1': "/Defects/Surface",
        '2': "/Defects/Corner",
        '3': "/Defects/Edge",
        '4': "/Defects/Centerning",
    }[x]

if __name__ == '__main__':
    import argparse
    import glob

    parser = argparse.ArgumentParser()
    parser.add_argument('batch', type=str,
                        help="batch file name")
    args = parser.parse_args()
    
    batch_name = args.batch
    defect_type = batch_name[7]
    language = batch_name[8:10]
    side = batch_name[13]
    des_path = defects(defect_type)
    batch_path = './Batches/'+batch_name+'.jpg'

    for i in range(4):
        for j in range(4):
            index = len(glob.glob1("./OriginalImages"+des_path, img_extension))
            img = cv2.imread(batch_path)
            cropped_img = img[y[i]:y[i]+h, x[j]:x[j]+w]         #crop
            cropped_img = crop_img(cropped_img)                 #reshape
            cv2.imwrite('./OriginalImages'+des_path+'/PKM_'+str(index).zfill(3)+side+'_'+language+'.jpg', cropped_img)
            print('PKM_'+str(index).zfill(3)+side+'_'+language+'.jpg saved to '+'OriginalImages'+des_path)

