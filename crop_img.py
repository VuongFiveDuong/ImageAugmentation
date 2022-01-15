import cv2
import numpy as np
import glob
import os
from name_handling import append_extension
from config import *


def crop_img(image):
    block_size = 71
    padding = int(block_size / 2)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 150, 200)
    thresh = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, block_size, int(255 / block_size))
    # cv2.imshow('Edge', edges)
    # cv2.imwrite('TestEdge.png', edges)
    # cv2.waitKey()
    # cv2.imshow('Thresh Edge', thresh)
    # cv2.imwrite('TestThresh.png', thresh)
    # cv2.waitKey()

    # Find bounding box and extract ROI
    x, y, w, h = cv2.boundingRect(thresh)
    ROI = image[y + padding:y + h - padding, x + padding:x + w - padding]
    ROI = cv2.resize(ROI, (SIZE_X, SIZE_Y))
    #cv2.imwrite('TestCrop.png', ROI)
    return ROI

# img_path = 'PKM_001F_132_194_RR_Chi.jpg'
# img = cv2.imread('OriginalImages/PKM_001F_132_194_RR_Chi.jpg')
#
# cropped_img_name = append_extension(img_path, '_cropped')
# cropped_img = crop_img(img)
# cv2.imshow('Cropped', cropped_img)
# cv2.waitKey()
#
# rotated_img_name = append_extension(img_path, '_rotated')
# rotated_img = rotate_img(cropped_img, 1)
# cv2.imshow('Rotated', rotated_img)
# cv2.waitKey()
#
# cv2.imwrite(cropped_img_name, cropped_img)
# cv2.imwrite(rotated_img_name, rotated_img)


for img_path in glob.glob(uncropped_images_dir + img_extension):
    img = cv2.imread(img_path)
    print(img_path)
    cropped_img_name = append_extension(img_path, '')
    cropped_img = crop_img(img)

    # rotated_img_name = append_extension(img_path, '_rotated')
    # rotated_img = rotate_img(cropped_img, 1)

    cv2.imwrite(os.path.join('CroppedImages/', cropped_img_name), cropped_img)
    # cv2.imwrite(os.path.join('testOriginal/rotated', rotated_img_name), rotated_img)

cv2.destroyAllWindows()
