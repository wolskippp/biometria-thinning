from global_processing import sharpening, average, grayscale, adaptive_equalization, otsu
from morphology import erosion





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

    return output
