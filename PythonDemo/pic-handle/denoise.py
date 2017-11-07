import numpy as np
import cv2
from matplotlib import pyplot as plot

cap = cv2.VideoCapture('vtest.avi')

img = [cap.read()[1] for i in range(5)]

gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]

gray = [np.float64(i) for i in gray]

noise = np.random.randn(*gray[1].shape)*10

noisy = [i+noise for i in gray]

noisy = [np.uint8(np.clip(i, 0, 255)) for i in noisy]

dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)

plot.subplot(131), plot.imshow(gray[2], 'orignal_gray')
plot.subplot(132), plot.imshow(noisy[2], 'noisy_gray')
plot.subplot(133), plot.imshow(dst, 'denois_gray')