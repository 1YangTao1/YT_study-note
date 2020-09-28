import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def pyramid_demo(image):
    level = 1
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("py"+str(i),dst)
        temp = dst.copy()
    cv.imwrite("D:/opencvtupian/9.jpg",dst)
    return pyramid_images

'''def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)'''


scr = cv.imread("D:/opencvtupian/8.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
pyramid_demo(scr)
cv.waitKey(0)
cv.destroyAllWindows()