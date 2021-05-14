import cv2 as cv

img = cv.imread('data/pic2.jpg')
cv.imshow('Original', img)

cv.rectangle(img, (10, 10), (600, 600), (0, 165, 255), thickness = 2)
cv.imshow('Changed', img)

cv.waitKey(0)
