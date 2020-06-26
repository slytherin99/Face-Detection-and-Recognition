import cv2
#read a video stream from camera (frame by frame)
cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:

	ret,frame=cap.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	if ret==False:
		continue


	faces=face_cascade.detectMultiScale(gray,1.3,5)

	for x,y,w,h in faces:
		cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)

	cv2.imshow('video frame',frame)


	key_pressed=cv2.waitKey(1) & 0xFF

	if key_pressed==ord('a'):
		break

cap.release()

cv2.destroyAllWindows()

## 1.3 i.e 30% is scale factor which specifies how much image size is reduced at each image scale
# 5 (ideal 3-6) is no. of neighbours which each candidate rectangle should have to retain it.
#Wait for user input a then you will stop the loop
