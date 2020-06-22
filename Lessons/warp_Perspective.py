import  cv2
import numpy as np

img = cv2.imread('data/sparrow.jpg')
width, height = 700,1000
pts1 = np.float32([[459,209],[836,209],[459,527],[836,501]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Warp Image", imgOutput)
cv2.waitKey(0)