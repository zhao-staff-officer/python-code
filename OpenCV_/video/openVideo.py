import numpy as np
import cv2 as cv

#打开视频
def openVideo():
    cap =cv.VideoCapture('F:\\self-platform\\python-code\\OpenCV_\\static\\test2.mp4')
    while(cap.isOpened()):
        print("isOpen:{}",cap.isOpened())
        ret,frame = cap.read()
        print("ret:{}",ret)
        gray =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',gray)
        if cv.waitKey(1) & 0xff ==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    openVideo()
