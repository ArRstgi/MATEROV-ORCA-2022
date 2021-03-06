import cv2
import numpy as np
import pickle

def detectWreckLength():

  kernel = np.ones((3,3), np.uint8)
  blur_coefficient = (5,5)
  cm_offset = 0
  pixel_offset = 0
  x_crop = 250
  y_crop = 0

  calib_result_pickle = pickle.load(open("camera_calib_pickle.p", "rb" ))
  mtx = calib_result_pickle["mtx"]
  optimal_camera_matrix = calib_result_pickle["optimal_camera_matrix"]
  dist = calib_result_pickle["dist"]
  roi = calib_result_pickle["roi"]

  cap = cv2.VideoCapture(2)
  #cap.set(3,480)
  #cap.set(4,360)

  if (cap.isOpened()== False):

    print("Error opening video stream or file")

  while(cap.isOpened()):

    ret, img_orig = cap.read()
    undistorted_img = cv2.undistort(img_orig, mtx, dist, None, optimal_camera_matrix)

    y_2, x_2 ,z_2 = undistorted_img.shape
    '''
    print(y_2)
    print(x_2)
    print(z_2)
    '''
    img_crop_y = y_2-y_crop
    img_crop_x = x_2-x_crop
    img_orig = undistorted_img[y_crop:img_crop_y, x_crop:img_crop_x]

    if ret == True:

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

      if cv2.waitKey(25) & 0xFF == ord('q'):

        break

    else:

      break
    
  cap.release()
  cv2.destroyAllWindows()
  


detectWreckLength()
