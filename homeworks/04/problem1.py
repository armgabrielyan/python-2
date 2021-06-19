import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv.imread('data/pic1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256]) 
gray_hist = [i[0] for i in gray_hist]

mpl.use('tkagg')
x = np.arange(256)
plt.plot(x, gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

# Open the image pic1.jpg and display it with the name pic1
# cv.imshow('pic1', img)
# cv.waitKey(0)
