import cv2
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier

face_data = []

dic = {
	0: 'amit',
	1: 'mohit'
}

labels = []

idx = 0
for file in os.listdir("data"):
	data = np.load(f"./data/{file}")
	face_data.append(data)

	l = [idx for i in range(data.shape[0])]
	labels.extend(l)

	idx+=1


X = np.concatenate(face_data, axis=0)
Y = np.array(labels).reshape(-1, 1)



print(X.shape, Y.shape)

print(Y)



knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X, Y)



##### PREDICTION/EVALUATION

cam = cv2.VideoCapture(0)

model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
	ret, frame =  cam.read()


	if ret == False:
		continue

	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = model.detectMultiScale(gray_frame, 1.1, 5)

	if len(faces)==0:
		continue

	

	for face in faces:

		x,y,w,h = face
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 4)

		offset = 5
		face_section = gray_frame[y-offset :y+h +offset , x -offset: x+w +offset]
		face_section = cv2.resize(face_section, (100,100))

		query = face_section.reshape(1, 10000)
		# Prediction from knn model

		pred = knn.predict(query)[0]
		print(pred)
		name = dic[int(pred)]

		cv2.putText(frame, name, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
	
		cv2.imshow("My video", frame)

	key_pressed = cv2.waitKey(1) & 0xFF

	if key_pressed == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()






