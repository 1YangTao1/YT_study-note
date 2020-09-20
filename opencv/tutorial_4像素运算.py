import cv2 as cv
import numpy as np

def operation_demo(m1,m2):
    dst = cv.add(m1,m2)
    #两张图片相加
    cv.imshow("add",dst)

    dst = cv.subtract(m1,m2)
    #图片相减
    cv.imshow("cdd",dst)

    dst = cv.divide(m1,m2)
    #图片相除
    cv.imshow("divide",dst)

    dst = cv.multiply(m1,m2)
    #图片相乘
    cv.imshow("mul",dst)


def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow('not',dst)
    #bitwise_###  逻辑运算

def contast_brightness_demo(image,c,b):
#c对比度，b亮度
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow('bri',dst)


scr1 = cv.imread("D:/opencvtupian/1.jpg")
scr2 = cv.imread("D:/opencvtupian/2.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("1_image",scr1)
#cv.imshow("2_image",scr2)
#operation_demo(scr1,scr2)
#logic_demo(scr1,scr2)
contast_brightness_demo(scr1,1,0)
cv.waitKey(0)
cv.destroyAllWindows()
