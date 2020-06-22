from cv2 import cv2


# upload the image
'''
img = cv2.imread("known_faces/kd.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)

cap = cv2.VideoCapture('data/baarish.mp4')

while True:
    success, img = cap.read()

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
'''
# upload the webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
