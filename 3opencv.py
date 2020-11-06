import cv2
import numpy as np


img = cv2.imread("responsive/bg-masthead.jpg")

print(img.shape)

imgresize = cv2.resize(img,(300,200))

imgcrop= img[0:200,200:500]


cv2.imshow("image",img)
cv2.imshow("image rewsize",imgresize)
cv2.imshow("image cropped",imgcrop)


cv2.waitKey(0)