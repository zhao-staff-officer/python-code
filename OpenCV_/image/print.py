import numpy as np
import cv2 as cv


def printLine():
    image =cv.imread('F:\\self-platform\\python-code\\OpenCV_\\static\\imageWrite.png',1)
    # img = np.zeros((512,512,3),np.uint8)
    #画线
    cv.line(image,(0,0),(511,511),(255,0,0),5)
    #画矩形
    cv.rectangle(image,(100,0),(200,100),(0,255,0),3)
    #画圆
    cv.circle(image,(150,50), 50, (0,0,255), -1)
    #画椭圆
    cv.ellipse(image,(256,256),(100,50),0,0,180,255,-1)
    #多边形
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.polylines(image,[pts],True,(0,255,255))
    cv.imshow('printline',image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    printLine()
