import numpy as np
import  cv2 as cv

def draw_circle(event,x,y,flag,param):
    if event ==cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(0,0,0),-1)

if __name__ == '__main__':

    img = np.zeros((512,512,3),np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('img',draw_circle)
    while(1):
        cv.imshow('image',img)
        if cv.waitKey(20) & 0xff == ord('q'):
            break
    cv.destroyAllWindows()
