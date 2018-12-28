import cv2 as cv



def nothing(x):
    pass



def sliders(img,algorithm):
    cv.namedWindow('image')

    cv.createTrackbar('treshold', 'image', 0, 255, nothing)

    while 1:

        k = cv.waitKey(1) & 0xFF

        if k == 27:
            break

        r = cv.getTrackbarPos('treshold', 'image')
        out = algorithm(img, r)
        cv.imshow('original', img)
        cv.imshow('image', out)


    cv.destroyAllWindows()