import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cap = cv2.VideoCapture('video.mp4')
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h , x:x+w]
		roi_color = frame[y:y+h , x:x+w]
		img_item1 = 'my-img-gray.png'
		#img_item2 = 'my-img-color.png'
		cv2.imwrite(img_item1,roi_gray)
		#cv2.imwrite(img_item2,roi_color)
		cv2.rectangle(frame,(x,y), (x+w, y+h), (255,0,255),1)
		l=30
		color = (255,0,255)
		th = 3
		x1 = x+w
		y1 = y+h

		#top left
		cv2.line(frame,(x,y),(x+l,y),color,th)
		cv2.line(frame,(x,y),(x,y+l),color,th)
		#top right
		cv2.line(frame,(x1,y),(x1-l,y),color,th)
		cv2.line(frame,(x1,y),(x1,y+l),color,th)
		#bottom left
		cv2.line(frame,(x,y1),(x+l,y1),color,th)
		cv2.line(frame,(x,y1),(x,y1-l),color,th)
		#bottom left
		cv2.line(frame,(x1,y1),(x1-l,y1),color,th)
		cv2.line(frame,(x1,y1),(x1,y1-l),color,th)





	cv2.imshow('output',frame)

	if cv2.waitKey(10) == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
