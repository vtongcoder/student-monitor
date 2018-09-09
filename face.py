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
    
    #Display result
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

