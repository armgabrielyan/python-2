import cv2 as cv

img = cv.imread('data/pic1.jpg')
cv.imshow('pic1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('pic1_gray', gray)

cv.waitKey(0)
