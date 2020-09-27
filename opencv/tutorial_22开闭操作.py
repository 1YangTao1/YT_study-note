import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def open_demo(image):
#先腐蚀在膨胀
#开操作,与膨胀和腐蚀的区别不改变原有的结构元素，可以提取水平和竖直的直线，也可以消除
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    #不同结构元素的大小和形状的调整可以出现不同的效果
    binary = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open_demo",binary)

def close_demo(image):
#先膨胀在腐蚀
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    binary = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("open_demo",binary)

scr = cv.imread("D:/opencvtupian/12.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
open_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()