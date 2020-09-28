import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    #降低噪声，边缘提取算法对噪声比较敏感
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    xgray = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygray = cv.Sobel(gray,cv.CV_16SC1,0,1)

    edge_output = cv.Canny(gray,50,150)
    cv.imshow('canny',edge_output)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
edge_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()