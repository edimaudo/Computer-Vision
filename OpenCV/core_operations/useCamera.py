import numpy as np
import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default');
cam = cv2.VideoCapture(0)

while(True):
	ret, img = cam.read();
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#classifier needs grayscale image
	faces = faceDetect.detectMultiScale(gray,1.3,5);
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow("face", img);
	if cv2.waitKey(1) == ord('q'):#if letter q is press camera is released
		break;


cam.release()
cv2.destroyAllWindows()



