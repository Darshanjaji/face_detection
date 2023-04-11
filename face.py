import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True :
    ret,frame = cap.read()
    if ret :
        faces = classifier.detectMultiScale(frame)
        for face in faces:
            x, y, w, h = face
            rect = cv2.rectangle(frame, (x, y), (x + w,y + h), (255,255 ,255),4)
            cv2.imshow("my image",rect)

    key =cv2.waitKey(1)

    if key == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()