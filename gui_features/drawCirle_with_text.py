import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)