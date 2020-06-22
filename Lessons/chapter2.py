from cv2 import cv2
import numpy as np

img = cv2.imread('data/smile.jpeg')
kernel = np.ones((5,5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# For blur we use gaussian
imgBlur = cv2.GaussianBlur(imgGrey, (7,7),0)
# For edge detection
imgCanny = cv2.Canny(img, 150,200)
# for thickness that edge
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# For thinner image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# cv2.imshow("Gray images", imgGrey)
# cv2.imshow("Blur image", imgBlur)
cv2.imshow("Edge image", imgCanny)
cv2.imshow("Thick image", imgDialation)
cv2.imshow("Erod image", imgEroded)
cv2.waitKey(0)