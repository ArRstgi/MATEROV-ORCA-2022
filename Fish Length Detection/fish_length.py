import cv2

import numpy as np

<<<<<<< HEAD

=======
>>>>>>> 714443472a8621ffbb5a6234053aad22604e92d5
kernel = np.ones((7,7), np.uint8)
cm_offset = 0
pixel_offset = 0
fish_ref = 11

<<<<<<< HEAD
path = r'C:\Users\madha\Documents\Madhav Programming\MATEROV-ORCA-2022\Fish Length Detection\1.jpg'
img_orig = cv2.imread(path)
fish = img_orig.copy()
gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
img_erode = cv2.erode(thresh, kernel, iterations=1)
=======
# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name
>>>>>>> 714443472a8621ffbb5a6234053aad22604e92d5

cap = cv2.VideoCapture(0)

 

# Check if camera opened successfully

if (cap.isOpened()== False):

  print("Error opening video stream or file")

 

# Read until video is completed

while(cap.isOpened()):

  # Capture frame-by-frame

  ret, img_orig = cap.read()
  img_orig = cv2.undistort(img_orig, mtx, dist, None, optimal_camera_matrix)

  if ret == True:

 

    # Display the resulting frame


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

 

    # Press Q on keyboard to  exit

    if cv2.waitKey(25) & 0xFF == ord('q'):

      break

 
  # Break the loop

  else:

    break

 

# When everything done, release the video capture object

cap.release()
# Closes all the frames
cv2.destroyAllWindows()
