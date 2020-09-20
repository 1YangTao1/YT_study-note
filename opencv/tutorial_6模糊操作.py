import cv2 as cv
import numpy as np

def blur_demo(image):
    dst = cv.blur(image,(5,5))
    #卷积图像均值模糊,基于平均值
    cv.imshow("blur",dst)

def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    #中值模糊，应用场景：椒盐噪声
    cv.imshow("med",dst)

def custom_blur_demo(image):
#自定义卷积核，自定义模糊
    #kernel = np.ones([5,5],np.float32)/25
    #自定义卷积核，总和等于1或等于0.         等于1：增强工作        等于0：做边缘梯度
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    dst = cv.medianBlur(image,5)
    #中值模糊，应用场景：椒盐噪声
    cv.imshow("med",dst)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
#blur_demo(scr)
custom_blur_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()