import cv2 #Import opencv
import os
import sys
image = sys.argv[1]
face = os.path.abspath("face_detect.xml")
imagePath = os.path.abspath(image)