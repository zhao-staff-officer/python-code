import numpy as np
import cv2 as cv

def videWrite():
    cap = cv.VideoCapture(0)
    fourcc =cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('test.avi',fourcc,20.0,(640,480))
    while (cap.isOpened()):
        ret,frame = cap.read()
        if ret ==True:
            frame =cv.flip(frame,0)
            out.write(frame)
            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xff ==ord('q'):
                break
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    videWrite()
