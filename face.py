import cv2 #Import opencv
import os
import sys
image = sys.argv[1]
face_db = os.path.abspath("face_detect.xml")
imagePath = os.path.abspath(image)
print(imagePath)
print(face_db)
