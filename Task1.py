import cv2
import numpy as np
import imgaug.augmenters as iaa
import os
from pathlib import Path


def append_extension(filename, extension):
    path = Path(filename)
    return "{0}_{1}{2}".format(path.stem, extension, path.suffix)


if __name__ == '__main__':

    import argparse
    import glob

    parser = argparse.ArgumentParser()

    parser.add_argument('--rotate', type=int, default=0,
                        help="Rotation in degrees (NOT radians), i.e. expected value range is around [-360, 360]. Rotation happens around the center of the image, not the top left corner as in some other frameworks.")
    parser.add_argument('--translate', type=str, default="0,0",
                        help="Translation as a fraction of the image height/width of form: x-translation, y-translation, where 0 denotes “no change” and 0.5 denotes “half of the axis size”." )
    parser.add_argument('--suffix', type=str, help="The suffix of saved images, e.g. suffix='rotate10'", default="augmented")
    parser.add_argument('--mode', type=str, help="The method to use when filling newly created pixels", default="wrap")

    args = parser.parse_args()

    file_extension = args.suffix
    rotate_degree = args.rotate
    translation_percent = [float(i) for i in args.translate.split(",")]

    img_extension = "*.jpg"
    original_images_dir = 'OriginalImages/'
    augmented_images_dir = 'AugmentedImages/'

    # Define the augmentation
    aug = iaa.Affine(rotate=rotate_degree, translate_percent=translation_percent, mode=args.mode)

    print(rotate_degree, translation_percent)

    # Loop through each of original image
    for img_path in glob.glob(original_images_dir + img_extension):
        img = cv2.imread(img_path)
        # augmented_imgs = augmentation(images=[img])

        augmented_img = aug(image=img)

        augmented_img_name = append_extension(img_path, file_extension)
        cv2.imwrite(os.path.join(augmented_images_dir, augmented_img_name), augmented_img)

        cv2.imshow("Augmented image", augmented_img)
        cv2.waitKey(0)
    '''
    big_img = img
    
    # cv2.imshow('Original Image', my_img)
    # cv2.waitKey(0)
    
    scale_percent = 25  # percent of original size
    width = int(big_img.shape[1] * scale_percent / 100)
    height = int(big_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    my_img = cv2.resize(big_img, dim, interpolation=cv2.INTER_AREA)
    
    
    img = [my_img]
    '''

    cv2.destroyAllWindows()

