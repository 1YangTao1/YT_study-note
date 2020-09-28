import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#顶帽  原图像与开操作之间的差值图像
#黑帽  闭操纵与原图像之间的差值图像
#形态学梯度  基本梯度：用膨胀后的图像减去腐蚀后的图像得到差值图像
# 内部梯度：用原图像减去腐蚀之后的图像得到差值图像
# 外部梯度：图像膨胀之后减去原来的图像得到的差值图像

def top_nat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    dst = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100
    dst = cv.add(dst,cimage)
    cv.imshow("tophat",dst)

def black_nat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    dst = cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 50
    dst = cv.add(dst,cimage)
    cv.imshow("tophat",dst)

def gradient_nat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    dst = cv.morphologyEx(gray,cv.MORPH_GRADIENT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 50
    dst = cv.add(dst,cimage)
    cv.imshow("tophat",dst)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
#cv.imshow("input image",scr)
gradient_nat_demo(scr)
#top_nat_demo(scr)
#black_nat_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()