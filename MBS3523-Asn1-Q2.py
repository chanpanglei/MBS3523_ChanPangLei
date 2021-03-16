# Requirement:
# Save the file on your Github as MBS3523-Asn1-Q2.py
# Print the code and attach to this paper
# One screen capture with your face shown
# The box can be of any color and thickness you like

import cv2

capture = cv2.VideoCapture(1)

capture.set(3,640)
capture.set(4,480)

x = 0
dx = 1
y=0
dy = 1
# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.rectangle(img, (x+100, y), (x , y+100), (255, 0, 0), 3)
    ball=dy,dx
    y = y + dy
    x = x + dx
    if y >= 450 or y <= 0:
        dy = dy * (-1)
        dx = dx * (1)
    if x >= 500 or x <= 0:
        dy = dy * (1)
        dx = dx * (-1)



    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()