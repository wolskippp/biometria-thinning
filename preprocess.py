from global_processing import sharpening, average, grayscale, adaptive_equalization, otsu


def binarize(img):
    shape = img.shape
    output = img.copy()

    for row in range(shape[0]):
        for col in range(shape[1]):

            if img[row, col] == 0:
                continue

            output[row, col] = 1

    return output


def preprocess_image(img, sharpen=False, gaussian_blur=False):
    output = img.copy()
    if sharpen:
        output = sharpening(output)

    if gaussian_blur:
        output = average(output)

    output = grayscale(output)

    output = adaptive_equalization(output)

    output = otsu(output)

    # output = erosion(output)
    output = binarize(output)

    return output
