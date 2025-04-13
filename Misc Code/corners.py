import cv2 as cv
import numpy as np

pic = cv.imread('tarpits.jpg')
pic = cv.resize(pic, (0, 0), fx = 0.75, fy = 0.75)
gray = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(pic, (x, y), 5, (255, 0, 0), -1)

    for i in range(len(corners), ):
        for j in range(i + 1, len(corners)):
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size = 3)))
            cv.line(pic, corner1, corner2, color), 1




cv.imshow('Tar Pits', pic)
cv.waitKey(0)
cv.destroyAllWindows()




























