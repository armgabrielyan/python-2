import cv2 as cv

pic1 = cv.imread('data/pic1.jpg')
pic2 = cv.imread('data/pic2.jpg')
pic3 = cv.imread('data/pic3.jpg')

cv.imshow('pic1', pic1) 
cv.imshow('pic2', pic2) 
cv.imshow('pic3', pic3) 

cv.waitKey(0)
