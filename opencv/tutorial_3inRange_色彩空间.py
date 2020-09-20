import cv2 as cv
import numpy as np

def extrace_object_demo():
    capture = cv.VideoCapture("D:/opencvtupian/a.mp4")
    while True:
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        dst = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)
        cv.imshow("mask",dst)
        c = cv.waitKey(40)
        if c == 27:
            break

def color_space_demo(imgae):
    gray = cv.cvtColor(imgae,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(imgae,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(imgae,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    ycrcb = cv.cvtColor(imgae,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb",ycrcb)


scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
b , g , r = cv.split(scr)
#通道分离
'''cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)'''

scr[:,:,2] = 0
#cv.imshow("chenageimage",scr)
#修改单通道值
#scr = cv.merge(b,g,r)
#合并通道

#color_space_demo(scr)
extrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()