import numpy as np
import cv2 as cv

#创建窗口加载图片
def createWind():
    cv.namedWindow('image',cv.WINDOW_NORMAL)
    image = cv.imread('F:\\self-platform\\python-code\\OpenCV_\\Source\\E05EV8.jpg',0)
    cv.imshow('image',image)
    key = cv.waitKey(0)
    print("key:{}",key)
    cv.destroyAllWindows()


if __name__ == '__main__':
    createWind()
