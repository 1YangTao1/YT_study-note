import cv2 as cv
import numpy as np
#高斯模糊保留图像的基本特征
def clamp(pv):
    if pv>255:
        return 255
    elif pv<0:
        return 0
    else:
        return pv
    

def gaussian_noise(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            #生成高斯分布的概率密度随机数   0代表均值，20代表方差，3代表大小
            b = image[row,col,0] #blue
            g = image[row,col,1] #green
            r = image[row,col,2] #red
            image[row,col,0] = clamp(b+s[0])
            image[row,col,1] = clamp(g+s[1])
            image[row,col,2] = clamp(r+s[2])
    cv.imshow("noise",image)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
dst = cv.GaussianBlur(scr,(0,0),15)
cv.imshow('Gaussian Blue',dst)
'''t1 = cv.getTickCount()
gaussian_noise(scr
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print(time)'''
cv.waitKey(0)
cv.destroyAllWindows()