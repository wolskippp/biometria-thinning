import glob
import os
import cv2 as cv

from k3m import k3m
from preprocess import preprocess_image
from kmm import kmm


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
    preprocessed = preprocess_image(img, sharpen=True, gaussian_blur=True)
    # thinned = kmm(preprocessed)
    thinned = k3m(preprocessed)
    rgb_image = prepare_to_print(thinned)
    cv.imshow('in', img)
    cv.imshow('out', rgb_image)


    cv.waitKey(0)


def prepare_to_print(img):
    shape = img.shape
    for row in range(shape[0]):
        for col in range(shape[1]):
            if img[row, col] != 0:
                img[row, col] = 255

    return img


if __name__ == '__main__':

    thumbs = False

    if thumbs:
        input_dir = os.path.join('kciuki/**/', '*.bmp')
        images = read_images(input_dir)
        repeat_for_all(images, forever=True)
    else:
        # input_dir = os.path.join('test', '*.*')
        input_dir = os.path.join('kciuki/**/', '*.bmp')

        images = read_images(input_dir)
        repeat_for_all(images)