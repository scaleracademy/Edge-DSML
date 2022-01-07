import cv2
import numpy as np

cam = cv2.VideoCapture(0)

model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


face_data = []

skip = 0

name = input("Enter your name: ")

while True:
	ret, frame =  cam.read()


	if ret == False:
		continue

	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = model.detectMultiScale(gray_frame, 1.1, 5)

	if len(faces)==0:
		continue

	faces = sorted(faces, key= lambda f: f[2]*f[3])

	
	x,y,w,h = faces[-1]
	cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 4)

	offset = 5
	face_section = gray_frame[y-offset :y+h +offset , x -offset: x+w +offset]
	face_section = cv2.resize(face_section, (100,100))


	skip += 1
	if skip%10==0:
		face_data.append(face_section)
		print(len(face_data))



	cv2.imshow("Face section", face_section)
	cv2.imshow("My video", frame)

	key_pressed = cv2.waitKey(1) & 0xFF

	if key_pressed == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()



# convert list of faces to numpy array
face_data = np.array(face_data)
print(face_data.shape)
face_data = face_data.reshape((face_data.shape[0], -1))


np.save(f"./data/{name}.npy", face_data)
print("Data saved successfully.")








