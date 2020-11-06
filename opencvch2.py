import cv2
import numpy as np


img = cv2.imread("responsive/bg-masthead.jpg")

kernel =np.ones((5,5),np.uint8)

imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgGray,(7,7),0)
imgcanny = cv2.Canny(img,150,200)
imgdialation = cv2.dilate(imgcanny,kernel,iterations=1)
imgeroded = cv2.erode(imgdialation,kernel,iterations=1)


# cv2.imshow("Gray",imgGray)
# cv2.imshow("blur nimage",imgblur)
cv2.imshow("CANNY IMAGE",imgcanny)
cv2.imshow("dialation IMAGE",imgdialation)
cv2.imshow("eroded IMAGE",imgeroded)
cv2.waitKey(0)