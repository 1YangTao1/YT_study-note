import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV  | cv.THRESH_OTSU)
    contours,hericahy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.imshow("binary image",binary)
    for i,contour in enumerate(contours):
        arae = cv.contourArea(contour)
        x,y,w,h = cv.boundingRect(contour)
        rate = min(w,h)/max(w,h)
        #print("rectang rate : %s"%rate)
        #输出宽高比
        #外接矩形的大小
        mm = cv.moments(contour)
        #求取几何矩
        print(type(mm))
        #是一个字典类型
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        #即可得到矩形的中芯位置
        #cv.circle(image,(np.int(cx),np.int(cy)),3,(0,255,255),-1)
        #cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        #绘制外接矩形
        #print("contour arae :%s"%arae)
        approxCurve = cv.approxPolyDP(contour,4,True)
        if approxCurve.shape[0] ==4:
            cv.drawContours(image,contours,i,(0,255,0),2)
    cv.imshow('measure',image)

scr = cv.imread("D:/opencvtupian/12.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
measure_object(scr)
cv.waitKey(0)
cv.destroyAllWindows()