import cv2 as cv

img = cv.imread('data/pic1.jpg')
cv.imshow('pic1', img)

blur1 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
blur2 = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)

cv.imshow('pic1_blur1', blur1)
cv.imshow('pic1_blur2', blur2)

cv.waitKey(0)
