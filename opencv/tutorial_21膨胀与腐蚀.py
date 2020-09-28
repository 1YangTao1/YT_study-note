import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY  | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    #返回指定形状和尺寸的结构元素
    dst = cv.erode(binary,kernel)
    cv.imshow("erode",dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV  | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    #返回指定形状和尺寸的结构元素
    dst = cv.dilate(binary,kernel)
    cv.imshow("erode",dst)

scr = cv.imread("D:/opencvtupian/12.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
dilate_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()