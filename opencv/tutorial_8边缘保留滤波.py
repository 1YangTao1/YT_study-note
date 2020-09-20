import cv2 as cv
import numpy as np

def bi_demo(image):
#更好的模糊化相当于阵容滤镜,高斯双边
    dst = cv.bilateralFilter(image,0,80,15)
    #sigmacolor颜色差异   sigmaspace空间差异 
    cv.imshow("bi_deme",dst)

def shift_demo(image):
#均值迁移，近似于油画模糊
    dst = cv.pyrMeanShiftFiltering(image,5,50)
    cv.imshow('shift',dst)

scr = cv.imread("D:/opencvtupian/123.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
#bi_demo(scr)
shift_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()