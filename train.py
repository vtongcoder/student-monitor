import os
#The base dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#The image dir
img_dir = os.path.join(BASE_DIR, "image")

for root, dirs, files in os.walk(img_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            print(path)
