import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
cv.waitKey(0)
cv.destroyAllWindows()
