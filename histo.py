import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/tarpits.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Masked Tar Pits', masked)
cv.waitKey(0)