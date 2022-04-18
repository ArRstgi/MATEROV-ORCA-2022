import cv2
import numpy as np


kernel = np.ones((7,7), np.uint8)
cm_offset = 0
pixel_offset = 0
fish_ref = 11

path = r'/home/cerealkiller2527/Documents/Programming/MATEROV-ORCA-2022/Fish Length Detection/1.jpg'
img_orig = cv2.imread(path)
fish = img_orig.copy()

gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
img_erode = cv2.erode(thresh, kernel, iterations=1)

x,y,w,h = cv2.boundingRect(img_erode)
#length = (fish_ref*(w+(offset*w/25))/h)
length = ((fish_ref*w)/(h+pixel_offset)) + cm_offset
length = round(length,2)
cv2.rectangle(fish, (x,y), (x+w,y+h), (237, 59, 59), 2)
cv2.putText(fish, "length={} cm".format(length), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

cv2.imshow("Fish", fish)
cv2.imshow("Thresholded", thresh)
cv2.imshow("Eroded", img_erode)

cv2.waitKey()
cv2.destroyAllWindows()