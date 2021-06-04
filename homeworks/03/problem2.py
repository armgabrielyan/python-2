import cv2 as cv
import numpy as np

img = cv.imread('data/pic1.jpg')
cv.imshow('pic1', img)

b, g, r = cv.split(img)

cv.imshow('blue grayscale', b)
cv.imshow('green grayscale', g)
cv.imshow('red grayscale', r)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)
