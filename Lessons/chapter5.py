import cv2
import numpy as np

def empty(a):
    pass

path = 'data/vehicle.jpg'

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",680,280)
cv2.createTrackbar("HUE MIn", "TrackBars", 19, 179,empty)
cv2.createTrackbar("HUE MAX", "TrackBars", 126, 179,empty)
cv2.createTrackbar("SATURATION MIn", "TrackBars", 24, 255,empty)
cv2.createTrackbar("SATURATION MAX", "TrackBars", 207, 255,empty)
cv2.createTrackbar("VALUE MIn", "TrackBars", 118, 255,empty)
cv2.createTrackbar("VALUE MAX", "TrackBars", 243, 255,empty)

while True:
    img = cv2.imread(path)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE MIn", "TrackBars")
    h_max = cv2.getTrackbarPos("HUE MAX", "TrackBars")
    s_min = cv2.getTrackbarPos("SATURATION MIn", "TrackBars")
    s_max = cv2.getTrackbarPos("SATURATION MAX", "TrackBars")
    v_min = cv2.getTrackbarPos("VALUE MIn", "TrackBars")
    v_max = cv2.getTrackbarPos("VALUE MAX", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult =  cv2.bitwise_and(img, img, mask=mask)



    cv2.imshow("Original", img)
    cv2.imshow("HSV image", imgHSV)
    cv2.imshow("Mask Image", mask)
    cv2.imshow("Result mask", imgResult)
    cv2.waitKey(1)
