import cv2 as cv
import numpy as np

def video_demo():
#通过电脑摄像头进行读取,即加载视频
    capture = cv.VideoCapture(0)
    #0代表USB摄像头
    while True:
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        #视频镜像调换
        cv.imshow("video",frame)
        #显示
        c = cv.waitKey(50)
        if c==27:
            break

def get_image_info(image):
#输出图片的各个信息
    print(type(image))
    print(image.shape)
    #打印图像高 宽 通道数目
    print(image.size)
    #打印图像大小
    print(image.dtype)
    #字节位数占多少
    pixel_data = np.array(image)
    #print(pixel_data)

scr = cv.imread("D:/opencvtupian/abc.jpg")
#读取一张图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#创建GUI显示图片
cv.imshow("input image",scr)
get_image_info(scr)
#cv.imwrite("D:/opencvtupian/123.jpg",scr)
#保存图片
#video_demo()
cv.waitKey(0)
cv.destroyAllWindows()

