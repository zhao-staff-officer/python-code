import cv2 as cv

def printPoint():
    event = [i for  i in dir(cv) if 'EVENT' in i]
    print(event)

if __name__ == '__main__':
    printPoint()
