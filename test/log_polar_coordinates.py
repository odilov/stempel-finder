import cv2
import numpy as np
import math

img = cv2.imread('path')
#img = cv2.medianBlur(img,5)
#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

maxRadius = math.sqrt(math.pow(img.shape[0], 2) + math.pow(img.shape[1], 2)) / 2
magnitude = img.shape[0] / math.log(maxRadius)
center = (img.shape[0] / 2, img.shape[1] / 2)
polar = cv2.logPolar(img, center, magnitude, cv2.INTER_AREA)

cv2.imshow('detected circles',polar)
cv2.waitKey(0)
cv2.destroyAllWindows()