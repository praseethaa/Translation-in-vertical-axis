import cv2
import numpy
import imutils


img=cv2.imread("sasuke.jpg")
img_translate=imutils.translate(img, 0, -250)
img_show=cv2.imshow("TRANSLATED_IMAGE", img_translate)
cv2.waitKey(0)
