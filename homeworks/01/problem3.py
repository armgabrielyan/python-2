import cv2 as cv

def rescaleFrame(frame, scale):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('data/pic1.jpg')

img_rescaled = rescaleFrame(img, 0.5)

cv.imshow('pic1', img)
cv.imshow('pic1_rescaled', img_rescaled)


cv.waitKey(0)


