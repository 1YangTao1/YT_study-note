import cv2 as cv
import numpy as np

def fill_binary():
    image = np.zeros([400,400,3], np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill_binary",image)

    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow('1',image)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()