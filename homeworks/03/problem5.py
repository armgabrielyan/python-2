import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), dtype = 'uint8')

gray_rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (170, 170, 170), -1)
gray_circle = cv.circle(blank.copy(), (200, 200), 200, (170, 170, 170), -1)

pink_rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (133, 21, 200), -1)
pink_circle = cv.circle(blank.copy(), (200, 200), 200, (133, 21, 200), -1)

image1 = cv.bitwise_xor(gray_rectangle, gray_circle)
cv.imshow('image1', image1)

image2 = cv.bitwise_or(gray_rectangle, gray_circle)
cv.imshow('image2', image2)

image3 = cv.bitwise_xor(pink_rectangle, pink_circle)
cv.imshow('image3', image3)

cv.waitKey(0)
