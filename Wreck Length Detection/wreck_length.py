import cv2 as cv2
import numpy as np

kernel = np.ones((3,3), np.uint8)
cm_offset = 0
pixel_offset = 0

<<<<<<< HEAD

path = r'C:\Users\madha\Documents\Madhav Programming\MATEROV-ORCA-2022\Wreck Length Detection\1.jpg'
=======
path = r'/home/cerealkiller2527/Documents/Programming/MATEROV-ORCA-2022/Wreck Length Detection/1.jpg'
>>>>>>> 714443472a8621ffbb5a6234053aad22604e92d5
wreck = cv2.imread(path)

gray = cv2.cvtColor(wreck, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
img_erode = cv2.erode(thresh, kernel, iterations=1)

# Find bounding box
x,y,w,h = cv2.boundingRect(img_erode)
#length = (25*(w+(pixel_offset*(w/25)))/h) + cm_offset
length = ((25*w)/(h+pixel_offset)) + cm_offset
length = round(length,2)
cv2.rectangle(wreck, (x,y), (x+w, y+h), (36,255,12), 2)
cv2.putText(wreck, "length={} cm".format(length), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

cv2.imshow("Eroded", img_erode)
cv2.imshow("Thresholded", thresh)
cv2.imshow("Wreck", wreck)

cv2.waitKey()
cv2.destroyAllWindows()