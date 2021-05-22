import cv2 as cv
import numpy as np

img = cv.imread('data/pic2.jpg')

cv.imshow('pic2', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 50, 200)
    
cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint = None):
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(translated, 50)

cv.imshow('Rotated', rotated)

flip = cv.flip(rotated, -1)

cv.imshow('Flipped', flip)

cv.waitKey(0)
