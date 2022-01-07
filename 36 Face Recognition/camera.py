import cv2

cam = cv2.VideoCapture(0)

model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
	ret, frame =  cam.read()

	if ret == False:
		continue


	faces = model.detectMultiScale(frame, 1.1, 5)


	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 4)

	cv2.imshow("My video", frame)

	key_pressed = cv2.waitKey(1) & 0xFF

	if key_pressed == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()