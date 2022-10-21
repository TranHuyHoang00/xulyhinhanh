# library
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv2

def identify_object(image):
    # nhan dien object
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    face_data = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml')
    eye_data = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
    body_data = cv2.CascadeClassifier('haarcascade/haarcascade_fullbody.xml')

    found = face_data.detectMultiScale(img_gray, minSize =(20, 20))
    
    found2 = eye_data.detectMultiScale(img_gray, minSize =(20, 20))

    found3 = body_data.detectMultiScale(img_gray, minSize =(20, 20))

    amount_found = len(found)
    amount_found2 = len(found2)
    amount_found3 = len(found3)

    if amount_found != 0:
        for (x, y, width, height) in found:
            cv2.rectangle(image, (x, y), 
                        (x + height, y + width), 
                        (0, 255, 0), 5)
    if amount_found2 != 0:
        for (x, y, width, height) in found2:
            cv2.rectangle(image, (x, y), 
                        (x + height, y + width), 
                        (0, 255, 0), 5)
    if amount_found3 != 0:
        for (x, y, width, height) in found2:
            cv2.rectangle(image, (x, y), 
                        (x + height, y + width), 
                        (0, 255, 0), 5)

    return image