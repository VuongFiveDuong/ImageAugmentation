import cv2
import numpy as np
import os
from transformation import rotate_img
from transformation import shift_img
from name_handling import append_extension
from name_handling import make_file_extension
from config import *
s

if __name__ == '__main__':
    import argparse
    import glob

    parser = argparse.ArgumentParser()

    parser.add_argument('--rotate', type=int, default=0,
                        help="Rotation in degrees (NOT radians), i.e. expected value range is around [-360, 360]")
    parser.add_argument('--shift_x_px', type=int, default=0,
                        help="move to E by pixel.")
    parser.add_argument('--shift_y_px', type=int, default=0,
                        help="move to S by pixel.")
    # parser.add_argument('--shift_x_percent', type=float, default=0,
    #                     help="0 denotes “no change” and 0.5 denotes “half of the axis size” to E.")
    # parser.add_argument('--shift_y_percent', type=float, default=0,
    #                     help=" denotes “no change” and 0.5 denotes “half of the axis size” to S.")
    # parser.add_argument('--suffix', type=str,
    #                       help="The suffix of saved images, e.g. suffix='rotate10'", default="augmented")
    parser.add_argument('--mode', type=str, help="The method to use when filling newly created pixels", default="wrap")

    args = parser.parse_args()
    rotate = args.rotate
    shift_x = args.shift_x_px
    shift_y = args.shift_y_px

    file_extension = make_file_extension(rotate, shift_x, shift_y)

    scale_percent = 25  # for reviewing
    # Loop through each of original image
    for img_path in glob.glob(nodefect2decenter_dir + img_extension):
        # print(img_path)
        img = cv2.imread(img_path)
        # augmented_imgs = augmentation(images=[img])
        rotated_img = rotate_img(img, rotate)

        augmented_img = shift_img(rotated_img, shift_x, shift_y)

        augmented_img_name = append_extension(img_path, file_extension)
        cv2.imwrite(os.path.join(augmented_images_dir, augmented_img_name), augmented_img)
        print(os.path.join(augmented_images_dir, augmented_img_name))

        # width = int(augmented_img.shape[1] * scale_percent / 100)
        # height = int(augmented_img.shape[0] * scale_percent / 100)
        # dim = (width, height)

        # resize image
        # small_img = cv2.resize(augmented_img, dim, interpolation=cv2.INTER_AREA)
        # cv2.imshow("Augmented image", small_img)
        # cv2.waitKey(0)

    cv2.destroyAllWindows()

