import numpy as np
import cv2 as cv

#创建窗口加载图片，保存图片
def writeImage():
    cv.namedWindow("test",cv.WINDOW_NORMAL)
    image = cv.imread('F:\\self-platform\\python-code\\OpenCV_\\Source\\E05EV8.jpg',1)
    cv.imshow("test",image)
    key = cv.waitKey(0)
    if key ==27:
        cv.destroyAllWindows()
    elif key ==ord('s'):
        cv.imwrite('F:\\self-platform\\python-code\\OpenCV_\\Source\\imageWrite.png',image)
        cv.destroyAllWindows()

if __name__ == '__main__':
    writeImage()
