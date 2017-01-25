import cv2
import numpy as np


img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg') # load image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # conver to gray scale

template = cv2.imread('opencv-template-for-matching.jpg',0) # load template
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) # compare
threshold = 0.7 #set threshold
loc = np.where( res >= threshold)

# show all positions
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb) # output