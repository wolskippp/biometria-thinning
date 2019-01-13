from termcolor import colored


def print_each_pixel(img):
    shape = img.shape
    for row in range(shape[0]):
        print('')
        for col in range(shape[1]):
            if img[row, col] == 0:
                print(colored(img[row, col], 'red'), end=" ")
            else:
                print(colored(img[row, col], 'white'), end=" ")



def are_neighbours_sticking(original_list):
    no_zeros_in_sides_list = remove_zeros_from_both_sides(original_list)

    if 0 in no_zeros_in_sides_list:
        no_numbers_on_sides_list = remove_numbers_from_both_sides(original_list)
        if sum(no_numbers_on_sides_list) == 0:
            return True
        else:
            return False
    return True


def remove_zeros_from_both_sides(dirs):
    start_remove = remove_zeros_from_left(dirs)
    reversed_list = start_remove[::-1]
    return remove_zeros_from_left(reversed_list)


def remove_numbers_from_both_sides(dirs):
    start_remove = remove_numbers_from_left(dirs)
    reversed_list = start_remove[::-1]
    return remove_numbers_from_left(reversed_list)


def remove_numbers_from_left(dirs):
    back_idx = 0
    for idx, dir in enumerate(dirs):
        if dir == 0:
            back_idx = idx
            break

    return dirs[back_idx:]


def remove_zeros_from_left(dirs):
    back_idx = 0
    for idx, dir in enumerate(dirs):
        if dir != 0:
            back_idx = idx
            break

    return dirs[back_idx:]




def get_pixel(img, row, col):
    row_max, col_max = img.shape
    if row_max <= row or row < 0:
        return 0

    if col_max <= col or col < 0:
        return 0

    return img[row, col]



def get_pixels_clockwise_around(img, row, col):
    all_pos = [(-1, -1),
               (-1, 0),
               (-1, 1),
               (0, 1),
               (1, 1),
               (1, 0),
               (1, -1),
               (0, -1)]

    neighbour = []
    for x, y in all_pos:
        pixel = get_pixel(img, row + x, col + y)
        neighbour.append(pixel)

    return neighbour
