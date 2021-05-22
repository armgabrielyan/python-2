import cv2 as cv

img = cv.imread('data/pic2.jpg')

cv.imshow('pic2', img)

width = 2 * img.shape[1]
height = img.shape[0]
dim = (width, height)

resize1 = cv.resize(img, dim, interpolation = cv.INTER_AREA)
cv.imshow('Resize1', resize1)

width = img.shape[1]
height = img.shape[0] // 2
dim = (width, height)

resize2 = cv.resize(img, dim, interpolation = cv.INTER_CUBIC)
cv.imshow('Resize2', resize2)

cv.waitKey(0)
