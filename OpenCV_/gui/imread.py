import numpy as np
import cv2 as cv


#加载图片
def loadImage():
    #加载图片
    image = cv.imread('F:\\self-platform\\python-code\\OpenCV_\\static\\E05EV8.jpg', -1)
    #创建窗口显示图片
    cv.imshow('carLicense',image)
    #绑定键盘
    cv.waitKey(0)
    #销毁窗口
    cv.destroyAllWindows()

if __name__ == '__main__':
    loadImage()





