import glob
import os
import cv2 as cv
from preprocess import preprocess_image
from thining import thinning


def read_images(path):
    output = {}
    for file_path in glob.glob(path):
        file_name = os.path.basename(file_path)
        image = cv.imread(file_path)
        output[file_name] = image
    return output


def repeat_for_all(images, forever=False):
    once = True
    while forever or once:
        for name, img in images.items():
            print('Processing: ', name)
            run_thining(name, img)
        once = False


def run_thining(name, img):
    output = preprocess_image(img, sharpen=True, gaussian_blur=True)
    first_step = thinning(output)

    cv.imshow('in', img)
    cv.imshow('out', output)
    # cv.imshow(name, first_step)

    cv.waitKey(0)


if __name__ == '__main__':

    thumbs = False

    if thumbs:
        input_dir = os.path.join('kciuki/**/', '*.bmp')
        images = read_images(input_dir)
        repeat_for_all(images, forever=True)
    else:
        input_dir = os.path.join('test', '*.*')
        images = read_images(input_dir)
        repeat_for_all(images)