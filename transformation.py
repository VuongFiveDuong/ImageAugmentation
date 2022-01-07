import numpy as np
import cv2
from config import *


# def np_ffill(arr, axis):
#     idx_shape = tuple([slice(None)] + [np.newaxis] * (len(arr.shape) - axis - 1))
#     idx = np.where(~np.isnan(arr), np.arange(arr.shape[axis])[idx_shape], 0)
#     np.maximum.accumulate(idx, axis=axis, out=idx)
#     slc = [np.arange(k)[tuple([slice(None) if dim==i else np.newaxis
#                                            for dim in range(len(arr.shape))])]
#                                            for i, k in enumerate(arr.shape)]
#     slc[axis] = idx
#     return arr[tuple(slc)]


def rotate_img(img, angle=0, row=SIZE_Y, col=SIZE_X, padding=PADDING):
    start_row = padding
    end_row = row - padding
    start_col = padding
    end_col = col - padding

    mid_row = int((start_col + end_col) / 2)
    mid_col = int((start_row + end_row) / 2)

    # inner_region = my_img[start_row:end_row, start_col:end_col]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nan_mask = np.zeros(gray_img.shape)
    # print(nan_mask.shape)
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
    # out_put = np_ffill(out_put, 0)

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


def shift_img(img, shift_x=0, shift_y=0, row=SIZE_Y, col=SIZE_X, padding=PADDING):
    start_row = padding
    end_row = row - padding
    start_col = padding
    end_col = col - padding

    # inner_region = my_img[start_row:end_row, start_col:end_col]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nan_mask = np.zeros(gray_img.shape)
    # print(nan_mask.shape)
    nan_mask[start_row:end_row, start_col:end_col] = np.ones((end_row - start_row, end_col - start_col))

    # angle = 1
    matrix = np.float32([
             [1, 0, shift_x],
             [0, 1, shift_y]
    ])
    # print(matrix)

    out_mask = cv2.warpAffine(nan_mask, matrix, (img.shape[1], img.shape[0]))
    out_im = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

    out_put = img.astype("float")
    out_put[start_row:end_row, start_col:end_col] = np.full((end_row - start_row, end_col - start_col, 3), np.nan)
    nan_mask = np.isnan(out_put)
    out_put[nan_mask] = np.interp(np.flatnonzero(nan_mask), np.flatnonzero(~nan_mask), out_put[~nan_mask])
    # out_put = np_ffill(out_put, 0)

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