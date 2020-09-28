import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def template_demo():
    tpl = cv.imread("D:/opencvtupian/6.jpg")
    target = cv.imread("D:/opencvtupian/123.jpg")
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    #TM_SQDIFF_NORMED该方法使用归一化的平方差进行匹配，最佳匹配也在结果为0处。
    #TM_CCORR_NORMED：归一化的相关性匹配方法，与相关性匹配方法类似，最佳匹配位置也是在值最大处
    #TM_CCOEFF：相关性系数匹配方法，该方法使用源图像与其均值的差、模板与其均值的差二者之间的相关性进行匹配，
    # 最佳匹配结果在值等于1处，最差匹配结果在值等于-1处，值等于0直接表示二者不相关
    th,tw = tpl.shape[:2]
    for md in methods:
        result = cv.matchTemplate(target,tpl,md)
        #第一个参数是源图像，第二个参数是模板图像，第三个参数是用于指定比较的方法。
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        #寻找矩阵中最小值和最大值的位置
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)
        cv.rectangle(target,tl,br,(0,0,255),2)
        #绘制简单、指定粗细或者带填充的 矩形
        cv.imshow("123"+np.str(md),target)
        #cv.imshow("123"+np.str(md),result)


scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
