# library
import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt

def noise_reduction(image):    
    dst = cv2.fastNlMeansDenoisingColored(image, None, 11, 6, 7, 21)

    return dst
