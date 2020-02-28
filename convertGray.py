import cv2
import os

def convertGray(newpath, path):

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    os.chdir(path)

    count = 0 
    for filename in os.listdir(path):
        os.chdir(path)
        img = cv2.imread(filename) 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        file_name = 'image_' + str(count) + '.jpg'
        os.chdir(newpath) 
        cv2.imwrite(file_name, gray)
        count += 1
