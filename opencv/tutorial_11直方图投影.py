import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def back_projection_demo():
    sample = cv.imread("D:/opencvtupian/5.jpg")
    target = cv.imread("D:/opencvtupian/123.jpg")

    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    #cv.imshow("sam",sample)
    #cv.imshow('tar',target)

    roiHist = cv.calcHist([roi_hsv] , [0,1] , None , [32,32] , [0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    #归一化数据。该函数分为范围归一化与数据值归一化
    #src               输入数组；
    #dst               输出数组，数组的大小和原数组一致；
    #alpha           1,用来规范值，2.规范范围，并且是下限；
    #beta             只用来规范范围并且是上限；
    #norm_type   归一化选择的数学公式类型；
    #dtype           当为负，输出在大小深度通道数都等于输入，当为正，输出只在深度与输如不同，不同的地方游dtype决定；
    #mark            掩码。选择感兴趣区域，选定后只能对该区域进行操作。
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow("dst",dst)
    cv.imwrite("D:/opencvtupian/5.jpg",dst)


def hist2d_demo(image):
#产生一个2维hsv直方图
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
    plt.imshow(hist,interpolation='nearest')
    plt.show()
    

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
#cv.imshow("input image",scr)
#hist2d_demo(scr)
back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()
