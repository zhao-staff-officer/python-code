import numpy as np
import cv2 as cv

def nothing(x):
    pass

def creat_brackbar():
    #创建何时图像窗口
    img = np.zeros((300,512,3),np.uint8)
    cv.namedWindow('image')
    #创建一个改变颜色的轨迹版
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)
    #创建开关来启用和关闭功能
    switch = '0 : OFF \n1 : ON'
    while(1):
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xff
        if k ==27:
            break
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        s = cv.getTrackbarPos(switch,'image')

        if s ==0:
            img[:] =0
        else:
            img[:] =[b,g,r]
    cv.destroyAllWindows()

if __name__ == '__main__':
    creat_brackbar()
