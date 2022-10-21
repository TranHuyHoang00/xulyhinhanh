from apps.face_recognition import face_recognition
from apps.noise_reduction import noise_reduction
from apps.identify_face import identify_face
from apps.identify_object import identify_object
import cv2
import matplotlib.pyplot as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image = cv2.imread('data/images/test.jpg')

    cv2.imshow('noise', noise_reduction(image))
    cv2.imshow('object', identify_object(image))

    cv2.waitKey(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
