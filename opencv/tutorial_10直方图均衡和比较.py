import cv2 as cv
import numpy as np

def equalHist_demo(image):
#直方图均衡化，增强对比度
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("euq",dst)

def clahe_demo(image):
#局部均衡化，可自由控制图像的对比度
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    chahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = chahe.apply(gray)
    cv.imshow('che',dst)

def creat_rgb_hist(image):
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row,col,2]
            index = np.int(b/bsize)*16*16+np.int(g/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0]+=1
    return rgbHist

def hits_compare(image1,image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    #巴氏距离比较
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)
    #相关性比较
    print("巴氏：%s,相关性：%s"%(match1,match2))
    #巴氏越小相似度越高，相关性越大相似度越低

scr1 = cv.imread("D:/opencvtupian/1.jpg")
scr2 = cv.imread("D:/opencvtupian/2.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
#cv.imshow("input image",scr)
#equalHist_demo(scr)
#clahe_demo(scr)
hits_compare(scr1,scr2)
cv.waitKey(0)
cv.destroyAllWindows()