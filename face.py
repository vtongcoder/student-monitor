#Import some library
import cv2
import numpy

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

