# reading and writing images
import cv2

image = cv2.imread('messi1.png')
cv2.imwrite('messi1.jpg', image)


grayImage = cv2.imread('messi1.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('messi1.jpg', grayImage)