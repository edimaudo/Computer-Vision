import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
plt.plot(122),plt.imshow(erosion),plt.title('Eroded image')
plt.xticks([]), plt.yticks([])
plt.show()

