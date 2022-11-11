import random
import cv2 as cv


img = cv.imread('tarpits.jpg', -1)
for i in range(1024):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv.imshow('Pixelated Tar Pits', img)
cv.waitKey(0)
cv.destroyAllWindows()