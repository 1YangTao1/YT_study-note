import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def big_image_binary(image):
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:cw+col]
            dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            gray[row,row+ch,col:col+cw] = dst
    cv.imshow('bigpicture',gray)

scr = cv.imread("D:/opencvtupian/7.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
print(scr.shape)
cv.waitKey(0)
cv.destroyAllWindows()