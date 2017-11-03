import cv2
from PIL import Image

img_path = './lena.jpg'
image = cv2.imread(filename=img_path)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray_img)

#   固定阙值二值化
#   cv2.threshold(src, thresh, maxval, type[, dst]) 
#   src 为输入图像；
#   thresh 为阈值；
#   maxval 为输出图像的最大值；
#   type 为阈值的类型；
#   dst 为目标图像
retval, im_at_fixed = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY) 
cv2.imshow('fxied binary image', im_at_fixed)

#   自适应二值化
#   cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
#   src 为输入图像；
#   maxval 为输出图像的最大值；
#   adaptiveMethod 设置为cv2.ADAPTIVE_THRESH_MEAN_C表示利用算术均值法，设置为cv2.ADAPTIVE_THRESH_GAUSSIAN_C表示用高斯权重均值法；
#   thresholdType: 阈值的类型；
#   blockSize: b的值(必须为单数)；
#   C 为从均值中减去的常数，用于得到阈值；
#   dst 为目标图像
im_at_mean = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 5)
cv2.imshow('adaptive binary image', im_at_mean)

#   获取图片尺寸
img_hight = image.shape[0]
img_width = image.shape[1]

#   定义方法，改变图像亮度
def chage_image_light(image, light_percent):
    for i in range(img_hight):
        for j in range(img_width):
            image[i, j, 0] = image[i, j, 0] * light_percent #blue
            image[i, j, 1] = image[i, j, 1] * light_percent #green
            image[i, j, 2] = image[i, j, 2] * light_percent #red
    return image

#   对图像进行复制
bright_img = image.copy()
black_img = image.copy()

bright_img = chage_image_light(bright_img, 1.5)
black_img = chage_image_light(black_img, 0.5)

#cv2.imshow('show bright image', bright_img)
#cv2.imshow('show black image',black_img)

#   在图像上增加文字
cv2.putText(image, 'Add Text!', (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (255,2555,255))
#   在图像上画圆
cv2.circle(image, (100, 200), 5, (255,255,255), -1, 8)
#cv2.imshow('Frame', image)

del image, bright_img, black_img
img_1 = cv2.imread(img_path)
img_2 = cv2.imread('./man-face.jpg')
#   图片缩放
img_2 = cv2.resize(img_2, (img_hight, img_width))
#   图片融合，图片高宽和格式需要相同
dst = cv2.addWeighted(img_1, 0.7, img_2, 0.3, 0)
cv2.imshow('图片融合', dst)

cv2.waitKey(0)
            