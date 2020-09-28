import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''基于距离的分水岭分割流程：
输入图像->灰度->二值->距离变换->寻找种子->生成marker->分水岭变换->输出图像'''
def watershed_demo():
    blurred = cv.pyrMeanShiftFiltering(scr,10,100)
    #均值模糊
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary',binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mb = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    #开操作，interation=2操作的次数两次
    sure_bg = cv.dilate(mb,kernel,iterations=3)
    #cv.imshow('mor—opt',sure_bg)
    dist = cv.distanceTransform(mb,cv.DIST_L2,3)
    #距离变换，
    dist_output = cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    #归一化数据。该函数分为范围归一化与数据值归一化,更好的显示距离变换的结果
    cv.imshow("distance",dist_output*100)
    #最亮的地方几位mask
    ret,surface = cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    cv.imshow("surface",surface)
    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg,surface_fg)
    #计算两个数组或数组和标量之间的每个元素差。也就是图像的相减操作
    ret,markers = cv.connectedComponents(surface_fg)
    #计算二值图像的连通域标记图像
    print(ret)
    #下面完成分水岭变换
    markers = markers + 1
    markers[unknown==255] = 0
    markers = cv.watershed(scr,markers=markers)
    scr[markers==-1] = [0,0,255]
    cv.imshow("result",scr)


scr = cv.imread("D:/opencvtupian/13.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
watershed_demo()
cv.waitKey(0)
cv.destroyAllWindows()