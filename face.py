#Import some library
import cv2
import numpy

#This is the cassade that we need
face_lib = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

#Capture is executeable
capture = cv2.VideoCapture(0)

#Set a loop
while(True):
    #Capture  frame-by-frame
    ret, frame = capture.read()

    #Convert the captured frame into gray "stuff"
    grayScaling = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Find faces
    faces = face_lib.detectMultiScale(grayScaling, scaleFactor=1.5, minNeighbors=5)

    #For loop
    for(x, y, w, h) in faces:
        print(x, y, w, h)

    #Display result
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

