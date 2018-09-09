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


        #Its deep learning time
        


        roi_gray = grayScaling[y:y+h, x:x+w] #(ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        img_item = "my_img.png"
        cv2.imwrite(img_item, roi_gray)

        #Draw a rectangle (?)
        color = (250, 0, 0) #Blue BGR ???
        stroke = 2
        end_cordx = x + w
        end_cordy = y + h
        cv2.rectangle(frame, (x, y), (end_cordx, end_cordy), color, stroke)

    #Display result
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

