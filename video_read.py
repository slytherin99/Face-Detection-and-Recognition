#Read a video stream from camera(frame by frame)
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	if ret == False:
		continue

	cv2.imshow("Video Frame", frame)
	
#Wait for user input -q, then stop the loop

	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break
	#'ord' tells us the ascii value of that symbol

cap.release()
cv2.destroyAllWindows()		