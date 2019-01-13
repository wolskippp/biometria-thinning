import numpy as np
import cv2 as cv

from Utils import are_neighbours_sticking, get_pixels_clockwise_around, get_pixel

remove_sums = [3, 5, 7, 12, 13, 14, 15, 20,
               21, 22, 23, 28, 29, 30, 31, 48,
               52, 53, 54, 55, 56, 60, 61, 62,
               63, 65, 67, 69, 71, 77, 79, 80,
               81, 83, 84, 85, 86, 87, 88, 89,
               91, 92, 93, 94, 95, 97, 99, 101,
               103, 109, 111, 112, 113, 115, 116, 117,
               118, 119, 120, 121, 123, 124, 125, 126,
               127, 131, 133, 135, 141, 143, 149, 151,
               157, 159, 181, 183, 189, 191, 192, 193,
               195, 197, 199, 205, 207, 208, 209, 211,
               212, 213, 214, 215, 216, 217, 219, 220,
               221, 222, 223, 224, 225, 227, 229, 231,
               237, 239, 240, 241, 243, 244, 245, 246,
               247, 248, 249, 251, 252, 253, 254, 255]

weight_matrix = np.array([128, 1, 2, 4, 8, 16, 32, 64])


def kmm(img):
    output = img.copy()
    change = 1
    counter = 1
    max_counter = 1000
    after = cv.countNonZero(output)
    while change != 0 and counter != max_counter:
        before = after

        output = twos_and_threes_contour(output)
        output = mark_fours(output)
        output = remove_based_on_sum(output)
        after = cv.countNonZero(output)
        change = before - after
        counter = counter + 1
        print('iteration: ', counter)
        print('white changed to black: ', change)

    return output


def remove_fours(img):
    shape = img.shape
    for row in range(shape[0]):
        for col in range(shape[1]):
            if img[row, col] == 4:
                img[row, col] = 0

    return img


def twos_and_threes_contour(img):
    shape = img.shape
    output = img.copy()

    for row in range(shape[0]):
        for col in range(shape[1]):

            if img[row, col] == 0:
                continue

            if should_be_2(img, row, col):
                output[row, col] = 2
            elif should_be_3(img, row, col):
                output[row, col] = 3

    return output


def mark_fours(img):
    shape = img.shape
    output = img.copy()

    for row in range(shape[0]):
        for col in range(shape[1]):

            if img[row, col] != 2:
                continue

            # we remove the four's
            if should_be_4(img, row, col):
                output[row, col] = 4

    return output


def remove_based_on_sum(img):
    shape = img.shape
    output = img.copy()

    for row in range(shape[0]):
        for col in range(shape[1]):

            if img[row, col] != 4:
                continue

            neighbours = get_pixels_clockwise_around(img, row, col)

            sum = 0
            for weight, neighbour in zip(weight_matrix, neighbours):
                if neighbour == 0:
                    continue

                sum = sum + weight

            if sum in remove_sums:
                output[row, col] = 0
            else:
                output[row, col] = 1

    return output


def should_be_4(img, row, col):
    original_list = get_pixels_clockwise_around(img, row, col)
    num_of_neighours = sum(list(map(lambda x: x != 0, original_list)))
    correct_num_of_neighbours = num_of_neighours == 2 or num_of_neighours == 3 or num_of_neighours == 4

    if not correct_num_of_neighbours:
        return False

    return are_neighbours_sticking(original_list)


def get_basic_directions(img, row, col):
    positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbour = []
    for x, y in positions:
        val = get_pixel(img, row + x, col + y)
        neighbour.append(val)
    return neighbour


def get_diagonals(img, row, col):
    positions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    neighbour = []
    for x, y in positions:
        neighbour.append(get_pixel(img, row + x, col + y))
    return neighbour


def should_be_2(img, row, col):
    basic_dirs = get_basic_directions(img, row, col)
    return not all(basic_dirs)


def should_be_3(img, row, col):
    diagonal_dirs = get_diagonals(img, row, col)
    return not all(diagonal_dirs)
