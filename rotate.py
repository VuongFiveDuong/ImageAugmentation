import numpy as np
import cv2


def rotate_img(img, angle=0):
    start_row = 50
    end_row = 2050
    start_col = 50
    end_col = 1500

    mid_row = int((start_col + end_col) / 2)
    mid_col = int((start_row + end_row) / 2)

    # inner_region = my_img[start_row:end_row, start_col:end_col]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nan_mask = np.zeros(gray_img.shape)
    print(nan_mask.shape)
    nan_mask[start_row:end_row, start_col:end_col] = np.ones((end_row - start_row, end_col - start_col))

    # imS = cv2.resize(nan_mask, (200, 270))
    # cv2.imshow("output", imS)
    # cv2.waitKey(0)

    rotate_center = (mid_row, mid_col)
    # angle = 1
    matrix = cv2.getRotationMatrix2D(rotate_center, angle, 1)

    out_mask = cv2.warpAffine(nan_mask, matrix, (img.shape[1], img.shape[0]))
    out_im = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

    out_put = img.astype("float")
    out_put[start_row:end_row, start_col:end_col] = np.full((end_row - start_row, end_col - start_col, 3), np.nan)
    nan_mask = np.isnan(out_put)
    out_put[nan_mask] = np.interp(np.flatnonzero(nan_mask), np.flatnonzero(~nan_mask), out_put[~nan_mask])
    out_put = out_put.astype("uint8")

    # imS = cv2.resize(out_put, (200, 270))
    # cv2.imshow("The background", imS)
    # cv2.waitKey(0)

    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if out_mask[row][col] > 0:
                out_put[row][col] = out_im[row][col]

    # print(out_put.shape)
    # imS = cv2.resize(out_put, (200, 270))
    # cv2.imshow("output", imS)
    # cv2.waitKey(0)
    return out_put
