import numpy as np
import cv2 as cv

def closing(img):
    kernel = np.ones((2, 2), np.uint8)
    return cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)


def opening(img):
    kernel = np.ones((2, 2), np.uint8)
    return cv.morphologyEx(img, cv.MORPH_OPEN, kernel)


def erosion(img):
    kernel = np.ones((2, 2), np.uint8)
    return cv.erode(img, kernel, iterations=1)


def dilation(img):
    kernel = np.ones((2, 2), np.uint8)
    return cv.dilate(img, kernel, iterations=1)

