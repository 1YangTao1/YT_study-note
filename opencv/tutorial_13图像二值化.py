import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def threashold_demo(image):
#全局阈值
    gary = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret , binary = cv.threshold(gary,0,255,cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    #ret 阈值  binary 二值化的图像  单个波峰用TRIANGLE
    cv.imshow("bin",binary)
    #cv.imwrite("D:/opencvtupian/二值化.jpg",binary)

def local_threshold(image):
#局部阈值，即先模糊在进行二值化
    gary = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gary,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    cv.imshow("bin2",binary)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
#threashold_demo(scr)
local_threshold(scr)
cv.waitKey(0)
cv.destroyAllWindows()
