from re import L
import cv2 as c
import numpy as n
import pickle

#from Manual.manual_control import down, left, right, stop, up

def linefollowing():

    x_crop = 250
    y_crop = 0
    calib_result_pickle = pickle.load(open("camera_calib_pickle.p", "rb" ))
    mtx = calib_result_pickle["mtx"]
    optimal_camera_matrix = calib_result_pickle["optimal_camera_matrix"]
    dist = calib_result_pickle["dist"]
    roi = calib_result_pickle["roi"]

    cap = c.VideoCapture(1)

    while True:

        ret, frame = cap.read()
        '''
        undistorted_img = c.undistort(frame, mtx, dist, None, optimal_camera_matrix)

        x, y, w, h = roi
        frame = undistorted_img[y:y+h, x:x+w]

        y_2, x_2 ,z_2 = frame.shape
        img_crop_y = y_2-y_crop
        img_crop_x = x_2-x_crop
        frame = frame[y_crop:img_crop_y, x_crop:img_crop_x]
        '''
        hsv = c.cvtColor(frame, c.COLOR_BGR2HSV)
        #lower = n.array([354, 3.9, 99.6])
        #upper = n.array([348, 83.3, 2.4])

        upper = n.array([0, 0, 50])
        lower = n.array([0,0,0])

        mask = c.inRange(hsv, lower, upper)

        contours, hierarchy = c.findContours(mask, 1,c.CHAIN_APPROX_NONE)
        c.drawContours(frame, contours, -1, (0,255,0), 1)
        '''
        if len(contours) > 0:
            cont = max(contours,key = c.contourArea)
            momnts = c.moments(cont)

            if momnts["m00"] !=0:
                cont_x = int(momnts['m10']/momnts['m00'])
                cont_y = int(momnts['m01']/momnts['m00'])
                c.circle(frame, (cont_x,cont_y), 5, (255,255,255), -1)

                if cont_y >= 190:
                    up()
                
                if cont_y <= 170:
                    down()

                if cont_y < 190 and cont_y > 170 and cont_x > 240:
                    right()

                if cont_x < 190 and cont_y > 170 and cont_x < 240:
                    left()

                if cont_x < 230 and cont_x > 250 and cont_y > 180:
                    down()
        '''
        c.imshow('frame', frame)
        c.imshow('mask', mask)

        if c.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    c.destroyAllWindows()

linefollowing()



