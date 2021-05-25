import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#使用matplotlib

def matplotlibtest():
    img = cv.imread('F:\\self-platform\\python-code\\OpenCV_\\static\\E05EV8.jpg', 0)
    plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]),plt.yticks([])
    plt.show()


if __name__ == '__main__':
    matplotlibtest()
