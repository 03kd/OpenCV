import cv2
import numpy as np

img = cv2.imread('data/mic.jpeg')
print(img.shape)

imgResize = cv2.resize(img, (300,300))
# image croping without using cv because image is generallt metrice. so,
imgCrop = img[0:100, 106:273]

cv2.imshow("Mic",img)
# cv2.imshow("Mix Resize", imgResize)
cv2.imshow("Crop image", imgCrop)
cv2.waitKey(0)