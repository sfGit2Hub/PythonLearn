import cv2
from PIL import Image

img_path = './lena.jpg'
image = cv2.imread(filename=img_path)

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
            