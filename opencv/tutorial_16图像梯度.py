import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#图像的一阶导数和二阶导数
def lapalian_demo(image):
#拉普拉斯算子
    #kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    dst = cv.Laplacian(image,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lap',lpls)

def soble_demow(image):
#soble算子
    grad_x = cv.Sobel(image,cv.CV_32F,1,0)
    grad_y = cv.Sobel(image,cv.CV_32F,0,1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x",gradx)
    cv.imshow("y",grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    #0.5代表权重
    cv.imshow("xy",gradxy)
scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
#soble_demow(scr)
lapalian_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()