import cv2
import numpy as np
# Load image, grayscale, Gaussian blur, Otsu's threshold
path = r'C:\Users\madha\Documents\Madhav Programming\MATEROV-ORCA-2022\Wreck Length Detection\1.jpg'
wreck = cv2.imread(path)
kernel = np.ones((5,5), np.uint8)
offset = 0

gray = cv2.cvtColor(wreck, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
img_erode = cv2.erode(thresh, kernel, iterations=1)

# Find bounding box
x,y,w,h = cv2.boundingRect(img_erode)
#length = (25*(w+(offset*w/25))/h)
length = ((25*w)/h) + offset
length = round(length,2)
cv2.rectangle(wreck, (x, y), (x + w, y + h), (36,255,12), 2)
cv2.putText(wreck, "length={} cm".format(length), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

cv2.imshow("Eroded", img_erode)
cv2.imshow("Wreck", wreck)

cv2.waitKey()
cv2.destroyAllWindows()