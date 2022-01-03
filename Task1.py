import cv2
import numpy as np
import imgaug.augmenters as iaa

big_img = cv2.imread('img_test.jpg')

# cv2.imshow('Original Image', my_img)
# cv2.waitKey(0)

scale_percent = 25  # percent of original size
width = int(big_img.shape[1] * scale_percent / 100)
height = int(big_img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
my_img = cv2.resize(big_img, dim, interpolation=cv2.INTER_AREA)


img = [my_img]

cv2.imshow("Resized image", my_img)
cv2.waitKey(0)

augmentation = iaa.Sequential([
    iaa.Rotate((-30, 30))
])

augmented_img = augmentation(images = img)

cv2.imshow("Rotated image", augmented_img[0])
cv2.waitKey(0)

cv2.destroyAllWindows()
