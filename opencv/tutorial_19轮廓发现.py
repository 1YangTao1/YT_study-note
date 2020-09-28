import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def contours_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    contours,hericahy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    #cloneImage:  contours:找到的轮廓，hericahy：层次的信息

    for i , contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
    cv.imshow("detect",image)


scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
contours_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()