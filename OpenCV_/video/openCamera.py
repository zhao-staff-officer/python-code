import numpy as np
import cv2 as cv

#打开摄像头
def openCamera():
    #创建video对象
    cap = cv.VideoCapture(0)
    while(True):
        #一帧一帧捕捉，返回bool值
        ret,frame = cap.read()
        hight = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        width=cap.get(cv.CAP_PROP_FRAME_WIDTH)
        print("vide,hight:{},width:{}",hight,width)
        #设置视频颜色
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #显示
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    openCamera()
