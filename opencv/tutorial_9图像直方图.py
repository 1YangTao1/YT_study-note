import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    #.ravel 将多维数组转化为一维
    plt.show("123")

def image_hist(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        # 直方图是对图像像素的统计分布，它统计了每个像素（0到L-1）的数量。
        #一、images（输入图像）参数必须用方括号括起来。
        #二、计算直方图的通道。
        #三、Mask（掩膜），一般用None，表示处理整幅图像。
        #四、histSize，表示这个直方图分成多少份（即多少个直方柱）。
        #五、range，直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素
        plt.plot(hist,color = color)
        plt.xlim([0,256])
    plt.show()

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
#lot_demo(scr)
image_hist(scr)
cv.waitKey(0)
cv.destroyAllWindows()