# Requirement:
# Save the file on your Github as MBS3523-Asn1-Q3.py
# Save the video to your Github as MBS3523-Asn1-Q3video.py
# Print the code and attach to this paper
# The boxes should be shown in random color
# Hint: get the car.xml from internet
# Result will be similar as below:

import cv2
import numpy as np
# import turtle
from turtle import *
# import random
from random import randint
print(cv2.__version__)


faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
cars_cascade = cv2.CascadeClassifier('Resources/haarcascade_car.xml')
eyeCascade = cv2.CascadeClassifier('Resources/haarcascade_eye.xml')

capture = cv2.VideoCapture('Resources/MBS3523-Asn1-Q3video.mp4')
# capture = cv2.VideoCapture(0)


while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h),  color=(randint(-500, 500), randint(-300, 270)), thickness=1)
    cars = cars_cascade.detectMultiScale(img, 1.15, 8)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w,y+h), color=(randint(-500, 500), randint(-300, 270)), thickness=1)

    cv2.imshow('Frame', img)
    #cv2.moveWindow('Frame', 100,20)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()