import imgaug.augmenters as iaa


def shift_img(img, shift_x=0, shift_y=0, mode="wrap"):
    shift = iaa.Affine(translate_px={"x": shift_x, "y": shift_y},
                       # translate_percent={"x": args.shift_x_percent, "y": args.shift_y_percent},
                       mode=mode)
    augmented_img = shift(image=img)
    return augmented_img
