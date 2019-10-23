import cv2
import os
from Face_trainer import Face_trainer as ft

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
cap = cv2.VideoCapture(0)
color = (0, 0, 255)
stroke = 4
face_cascades = cv2.CascadeClassifier(os.path.join(
    PROJECT_ROOT, "cascades/data/haarcascade_frontalface_alt2.xml"))


class Sauron:
    def __init__(self):
        self.facetrain = ft(cv=cv2, cascade=face_cascades)

    def computer_vision(self):
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascades.detectMultiScale(
            gray, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)

            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        print("quitting computer VS")


    def train(self):
        self.facetrain.train()

        
    def recognize_face(self,frame):
        face_list = []
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        path = os.path.join(PROJECT_ROOT, "trainer.yml")
        recognizer.read(path)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascades.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            person, confidence = recognizer.predict(roi)
            #face_list.append((person, confidence, x,y,w,h))
            face_list.append(self.facetrain.get_names()[person])
        return face_list

    def read_face(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        return self.recognize_face(frame)    
