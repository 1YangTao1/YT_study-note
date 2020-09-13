import cv2 as cv
import numpy as np

def access_pixels(image):
#访问各个像素点，并将各个像素点改变使图像灰度化
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row][col][c]
                image[row][col][c] = 255-pv
    cv.imshow("123",image)

def create_image():
#利用np创建图像
    img = np.zeros([400,300,3],np.uint8)
    #np.zeros返回来一个给定形状和类型的用0填充的数组
    img[:,:,0] = np.ones([400,300])*255

    cv.imshow("456",img)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
t1 = cv.getTickCount()
#用于返回从操作系统启动到当前所经的计时周期数
#access_pixels(scr)
create_image()
t2 = cv.getTickCount()
time = ((t2-t1)/cv.getTickFrequency())*1000
print("time : %s ms"% time)
#getTickFrequency()：用于返回CPU的频率
cv.waitKey(0)
cv.destroyAllWindows()
