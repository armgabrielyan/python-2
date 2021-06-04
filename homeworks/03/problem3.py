import cv2 as cv

img = cv.imread('data/pic2.jpg')
cv.imshow('pic2', img)

average = cv.blur(img, (5, 5))
cv.imshow('average blur', average)

# It looks quite similar to the original image with small values of parameters.
bilateral1 = cv.bilateralFilter(img, 5, 10, 20)
cv.imshow('bilateral1', bilateral1)

# It looks blurred with large values of parameters.
# Yet, it is not as distoreted as in the case of average blur.
bilateral2 = cv.bilateralFilter(img, 50, 100, 200)
cv.imshow('bilateral2', bilateral2)

cv.waitKey(0)
