from pathlib import Path


def append_extension(filename, extension):
    path = Path(filename)
    return "{0}{1}{2}".format(path.stem, extension, path.suffix)


def make_file_extension(rotate, shift_x, shift_y):
    # if shift_x == 0:
    #     shifting_x_extension = ''
    # elif shift_x > 0:
    #     shifting_x_extension = '_E_' + str(shift_x)
    # else:
    #     shifting_x_extension = '_W_' + str(-shift_x)
    shifting_x_extension = '_E_' + str(shift_x)

    # if shift_y == 0:
    #     shifting_y_extension = ''
    # elif shift_y > 0:
    #     shifting_y_extension = '_S_' + str(shift_y)
    # else:
    #     shifting_y_extension = '_N_' + str(-shift_y)
    shifting_y_extension = '_S_' + str(shift_y)

    rotation_extension = '_R_' + str(rotate)
    return rotation_extension + shifting_x_extension + shifting_y_extension

