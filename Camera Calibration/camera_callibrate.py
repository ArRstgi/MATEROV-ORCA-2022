import cv2
import numpy as np
import glob
import pickle
number_of_squares_X = 10
number_of_squares_Y = 7
nX = number_of_squares_X - 1
nY = number_of_squares_Y - 1
square_size = 0.023

path = r'C:\Users\madha\Documents\Programming\MATEROV-ORCA-2022\Camera Calibration\images\*.png'
images = glob.glob(path)

object_points = []
image_points = []

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
object_points_3D = np.zeros((nX * nY, 3), np.float32)                                               
object_points_3D[:,:2] = np.mgrid[0:nY, 0:nX].T.reshape(-1, 2) 
object_points_3D = object_points_3D * square_size
 
for image in images:

    image = cv2.imread(image)  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    success, corners = cv2.findChessboardCorners(gray, (nY, nX), None)
     
    if success == True:

        object_points.append(object_points_3D)
        corners_2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)       
        image_points.append(corners_2)
        cv2.drawChessboardCorners(image, (nY, nX), corners_2, success)

        cv2.imshow("Image", image) 
        cv2.imwrite("hmm.jpg", image)
        cv2.waitKey(200)
        cv2.destroyAllWindows

for image_2 in images:

    distorted_image = cv2.imread(image_2)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, gray.shape[::-1], None, None)
    height, width = distorted_image.shape[:2]
    optimal_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (width,height), 1, (width,height))
    undistorted_image = cv2.undistort(distorted_image, mtx, dist, None, optimal_camera_matrix)

    x, y, w, h = roi
    undistorted_image = undistorted_image[y:y+h, x:x+w]

    cv2.imshow("undistorted", undistorted_image) 
    cv2.waitKey(150)

calib_result_pickle = {}
calib_result_pickle["mtx"] = mtx
calib_result_pickle["optimal_camera_matrix"] = optimal_camera_matrix
calib_result_pickle["roi"] = roi
calib_result_pickle["dist"] = dist
calib_result_pickle["rvecs"] = rvecs
calib_result_pickle["tvecs"] = tvecs
pickle.dump(calib_result_pickle, open("camera_calib_pickle.p", "wb" )) 

cv2.destroyAllWindows() 