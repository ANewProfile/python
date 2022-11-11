import cv2 as cv
import random

pic = cv.imread('tarpits.jpg')
img = cv.imread('tarpits.jpg', -1)
# color = cv.cvtColor([pic], cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(pic, (7, 7), cv.BORDER_DEFAULT)
# cropping = pic[1:400, 1:400]
# canny = cv.Canny(pic, 125, 175)
# dilated = cv.dilate(pic, (7, 7), iterations=3)
# erode = cv.erode(pic, (7, 7), iterations=10)
# upside_down = cv.flip(pic, -1)
# side = cv.flip(pic, 45)
tag = img[400:600, 500:800]
img[50:250, 500:850] = tag



# cv.imshow('Tar Pits', img)
cv.imshow('Tar Pits Modified', img)
cv.waitKey(0)



















#
# capture = cv.VideoCapture('job_interview.mp4')
#
#
# while True:
#     isTrue, frame = capture.read()
#     if isTrue:
#         cv.imshow('A Job Interview With A Millennial', frame)
#
#         if cv.waitKey(0) & 0xFF == ord('d'):
#             break
#         else:
#             break
# capture.release()
# cv.destroyAllWindows()