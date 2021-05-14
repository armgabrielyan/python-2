import cv2 as cv

img = cv.imread('data/pic1.jpg')
cv.imshow('Original', img)

print(img.shape)

cv.line(img, (0, 400), (1024, 0), (0, 0, 255), thickness = 2)
cv.imshow('Changed', img)

cv.waitKey(0)
