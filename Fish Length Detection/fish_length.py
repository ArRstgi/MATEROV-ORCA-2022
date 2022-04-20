import cv2
import numpy as np
import pickle

kernel = np.ones((7,7), np.uint8)
blur_coefficient = (5,5)
cm_offset = 0
pixel_offset = 0
fish_ref = 11
x_crop = 250
y_crop = 0

calib_result_pickle = pickle.load(open("camera_calib_pickle.p", "rb" ))
mtx = calib_result_pickle["mtx"]
optimal_camera_matrix = calib_result_pickle["optimal_camera_matrix"]
dist = calib_result_pickle["dist"]
roi = calib_result_pickle["roi"]

cap = cv2.VideoCapture(0)

if (cap.isOpened()== False):

  print("Error opening video stream or file")

while(cap.isOpened()):

  ret, img_orig = cap.read()
  undistorted_img = cv2.undistort(img_orig, mtx, dist, None, optimal_camera_matrix)

  x, y, w, h = roi
  rand_img = undistorted_img[y:y+h, x:x+w]
  img_dimensions = rand_img.shape
  img_crop_x = img_dimensions[1]-x_crop
  img_crop_y = img_dimensions[2]-y_crop
  img_orig = rand_img[x_crop:img_crop_x, y_crop:img_crop_y]

  if ret == True:

    fish = img_orig.copy()

    gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, blur_coefficient, 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img_erode = cv2.erode(thresh, kernel, iterations=1)

    x,y,w,h = cv2.boundingRect(img_erode)
    #length = (fish_ref*(w+(offset*w/25))/h)
    length = ((fish_ref*w)/(h+pixel_offset))+cm_offset
    length = round(length,2)
    cv2.rectangle(fish, (x,y), (x+w,y+h), (237, 59, 59), 2)
    cv2.putText(fish, "length={} cm".format(length), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

    cv2.imshow("Fish", fish)
    #cv2.imshow("Thresholded", thresh)
    #cv2.imshow("Eroded", img_erode)
    #cv2.imshow("Blurred", blur)

    if cv2.waitKey(25) & 0xFF == ord('q'):

      break

  else:

    break
  
cap.release()
cv2.destroyAllWindows()
