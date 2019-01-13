import numpy as np
import cv2 as cv

from Utils import are_neighbours_sticking, get_pixels_clockwise_around, print_each_pixel

weight_matrix = np.array([128, 1, 2, 4, 8, 16, 32, 64])

A0 = [3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56, 60,
      62, 63, 96, 112, 120, 124, 126, 127, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223, 224,
      225, 227, 231, 239, 240, 241, 243, 247, 248, 249,
      251, 252, 253, 254]

A1 = [7, 14, 28, 56, 112, 131, 193, 224]

A2 = [7, 14, 15, 28, 30, 56, 60, 112, 120, 131, 135,
      193, 195, 224, 225, 240]

A3 = [7, 14, 15, 28, 30, 31, 56, 60, 62, 112, 120,
      124, 131, 135, 143, 193, 195, 199, 224, 225, 227,
      240, 241, 248]

A4 = [7, 14, 15, 28, 30, 31, 56, 60, 62, 63, 112, 120,
      124, 126, 131, 135, 143, 159, 193, 195, 199, 207,
      224, 225, 227, 231, 240, 241, 243, 248, 249, 252]

A5 = [7, 14, 15, 28, 30, 31, 56, 60, 62, 63, 112, 120,
      124, 126, 131, 135, 143, 159, 191, 193, 195, 199,
      207, 224, 225, 227, 231, 239, 240, 241, 243, 248,
      249, 251, 252, 254]

A1pix = [3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56,
         60, 62, 63, 96, 112, 120, 124, 126, 127, 129, 131,
         135, 143, 159, 191, 192, 193, 195, 199, 207, 223,
         224, 225, 227, 231, 239, 240, 241, 243, 247, 248,
         249, 251, 252, 253, 254]

phases = [A0, A1, A2, A3, A4, A5, A1pix]


def k3m(img):
    output = img.copy()

    joined_neighbours_num = {1: [3],
                             2: [3, 4],
                             3: [3, 4, 5],
                             4: [3, 4, 5, 6],
                             5: [3, 4, 5, 6, 7]
                             }

    change = 1
    counter = 1
    max_counter = 1000
    after = cv.countNonZero(output)
    while change != 0 and counter != max_counter:
        before = after
        output = prepare_border(output)
        for phase in range(1, 6):
            output = later_phases(output, phase, joined_neighbours_num[phase])

        after = cv.countNonZero(output)
        change = before - after
        counter = counter + 1
        print('iteration: ', counter)
        print('white changed to black: ', change)

    return output


def later_phases(img, phase, numbers):
    shape = img.shape
    output = img.copy()
    for row in range(shape[0]):
        for col in range(shape[1]):
            if img[row][col] != 2:
                continue

            satisfy_conditions = check_neighbour_condition(img, row, col, numbers)

            if satisfy_conditions:
                weights_sum = calc_sum_of_pixel(img, row, col)
                if weights_sum in phases[phase]:
                    output[row, col] = 0

    return output


def check_neighbour_condition(img, row, col, numbers):
    original_list = get_pixels_clockwise_around(img, row, col)
    num_of_neighours = sum(list(map(lambda x: x != 0, original_list)))
    correct_num_of_neighbours = num_of_neighours in numbers

    if not correct_num_of_neighbours:
        return False

    return are_neighbours_sticking(original_list)


def calc_sum_of_pixel(img, row, col):
    neighbours = get_pixels_clockwise_around(img, row, col)

    weights = 0
    for weight, neighbour in zip(weight_matrix, neighbours):
        if neighbour == 0:
            continue

        weights = weights + weight

    return weights


def prepare_border(img, phase=0):
    shape = img.shape
    output = img.copy()
    for row in range(shape[0]):
        for col in range(shape[1]):
            if img[row][col] !=1:
                continue
            summed_up = calc_sum_of_pixel(img, row, col)
            if summed_up in phases[phase]:
                output[row, col] = 2
    return output
