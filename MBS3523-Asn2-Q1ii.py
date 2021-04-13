# Save the code in Part (ii) on your Github as MBS3523-Asn2-Q1ii.py
import cv2
import face_recognition
import numpy as np
import os
print(cv2.__version__)
print(face_recognition.__version__)

encodes = []
names = []

image_dir = 'Images_Known'  # Insert ChanPangLei.jpg & recognition in Image_Unknown Directory
for root, dirs, files in os.walk(image_dir):
    print(files)
    for file in files:
        fullPath = os.path.join(root, file)
        print(fullPath)
        name = os.path.splitext(file)[0]
        print(name)
        imgKnown = face_recognition.load_image_file(fullPath)
        encodeKnown = face_recognition.face_encodings(imgKnown)[0]
        encodes.append(encodeKnown)
        names.append(name)
print(names)

capture = cv2.VideoCapture(1)
capture.set(3, 640)
capture.set(4, 480)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # From webcam, read and find unknown images, encode, and compare to known faces
    faceLocsCam = face_recognition.face_locations(imgRGB)
    encodesCam = face_recognition.face_encodings(imgRGB, faceLocsCam)

    # Compare faces in webcam to encoded face
    for (top, right, bottom, left), encodeCam in zip(faceLocsCam, encodesCam):
        name = "unknown person"
        results = face_recognition.compare_faces(encodes, encodeCam)
        faceDist = face_recognition.face_distance(encodes, encodeCam)
        print(faceDist)
        match_index = np.argmin(faceDist)
        if results[match_index]:
            name = names[match_index]
        cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.rectangle(img, (left, top), (right, top-30), (255, 0, 0), -1)
        cv2.putText(img, name, (left, top-10), font, .75, (0, 255, 255), 2)

    cv2.imshow('Face Recognition Frame', img)
    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
