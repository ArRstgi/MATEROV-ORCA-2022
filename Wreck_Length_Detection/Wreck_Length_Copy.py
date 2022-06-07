import cv2
import numpy as np
import pickle

def detectWreckLength():

wreck = img_orig.copy()

gray = cv2.cvtColor(wreck, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, blur_coefficient, 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
img_erode = cv2.erode(thresh, kernel, iterations=1)

x,y,w,h = cv2.boundingRect(img_erode)
#length = (25*(w+(pixel_offset*(w/25)))/h)+cm_offset
length = ((25*w)/(h+pixel_offset))+cm_offset
length = round(length,2)
cv2.rectangle(wreck, (x,y), (x+w, y+h), (36,255,12), 2)
cv2.putText(wreck, "length={} cm".format(length), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

cv2.imshow("Wreck", wreck)
#cv2.imshow("Thresholded", thresh)
#cv2.imshow("Eroded", img_erode)
#cv2.imshow("Blurred", blur)
cv2.destroyAllWindows()
  