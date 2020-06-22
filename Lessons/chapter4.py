import cv2
import numpy as np

img = np.zeros((521,521,3), np.uint8)
#black screen into blue color
# img[:] = 254,0,0

# draw a line on image
cv2.line(img,(0,0),(img.shape[1], img.shape[0]), (0,0,255),3)
cv2.rectangle(img, (100,100), (200,200),(0,255,0),cv2.FILLED)
cv2.circle(img, (450,150), 40, (255,255,0), cv2.FILLED)

# put text on img
cv2.putText(img, " OPENCV KD ",(40,400), cv2.FONT_HERSHEY_COMPLEX,1, (245, 66, 200),2)

cv2.imshow("Image",img)
cv2.waitKey(0)