import cv2
import numpy as np

pic = cv2.imread('./opency-logo-white.jpg')
hsv_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# 二值化HSV图片，来获取蓝色
mask = cv2.inRange(hsv_pic, lower_blue, upper_blue)

result_pic = cv2.bitwise_and(pic, pic, mask=mask)

cv2.imshow('original', pic)
cv2.imshow('threshold mask', mask)
cv2.imshow('result pic', result_pic)
cv2.waitKey(0)
cv2.destroyAllWindows()