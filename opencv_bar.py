import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


img = cv.imread('tarpits.jpg')

cv.namedWindow('Image')

cv.createTrackbar('CP', 'Image', 10, 400, nothing)

switch = 'color/gray'

cv.createTrackbar(switch, 'Image', 0, 1, nothing)

while (1):
    img = cv.imread('tarpits.jpg')
    pos = cv.getTrackbarPos('CP', 'Image')
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)
    k = cv.waitKey(1) & 0xFF
    if (k == 27):
        break

    s = cv.getTrackbarPos(switch, 'Image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('Image', img)

cv.destroyAllWindows()