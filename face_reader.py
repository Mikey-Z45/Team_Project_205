#webscraper.py
#11/20/2017
#Danial Sahuri, Jessica Ubaldo
#Description: Takes images from images/ directory and iterates them through a face detection program and saves them
#to a new directory faceimages/
import os
import numpy as np
import cv2
from pprint import pprint
from PIL import Image


#defines some objects to use the xml files needed for face recognition
casc_class = "haarcascade_frontalface_default.xml"
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print("file didn't load")
else:
    print("finding faces...")

face = 1
for file in os.listdir("images"):
    if file.endswith(".jpg"):
        img = cv2.imread("images/"+ file )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255) ,2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

        #pprint(eyes)
        cv2.imwrite('faceimages/'+ str(face)+'.jpg', img)
        face += 1
