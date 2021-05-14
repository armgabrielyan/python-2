import cv2 as cv

img = cv.imread('data/pic2.jpg')
cv.imshow('Original', img)

cv.circle(img, (300, 300), 150, (0, 0, 255), thickness = cv.FILLED)
cv.imshow('Changed', img)

cv.waitKey(0)
