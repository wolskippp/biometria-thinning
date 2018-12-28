import cv2 as cv
import numpy as np


def treshold(img, min=90, max=255):
    ret, th1 = cv.threshold(img, min, max, cv.THRESH_BINARY)
    th1 = cv.bitwise_not(th1)
    return th1


def otsu(img):
    ret, th1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    th1 = cv.bitwise_not(th1)
    return th1


def grayscale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def adaptive_equalization(img):
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(img)


def equalize(img):
    return cv.equalizeHist(img)


def canny(img):
    return cv.Canny(img, 100, 200)


def average(img):
    return cv.GaussianBlur(img, (3, 3), 0)


def sharpening(img):
    kernel = 4 * np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
    return cv.filter2D(img, -1, kernel)
