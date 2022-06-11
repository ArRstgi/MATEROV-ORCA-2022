from re import L
import cv2
import numpy as np
import pickle

#from Manual.manual_control import down, left, right, stop, up

def linefollowing():

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

    while True:


        
        ret, frame = cap.read()
        
        undistorted_img = cv2.undistort(frame, mtx, dist, None, optimal_camera_matrix)

        x, y, w, h = roi
        frame = undistorted_img[y:y+h, x:x+w]

        y_2, x_2 ,z_2 = frame.shape
        img_crop_y = y_2-y_crop
        img_crop_x = x_2-x_crop
        frame = frame[y_crop:img_crop_y, x_crop:img_crop_x]
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        '''
        #lower = np.array([175,50,20])
        #upper = np.array([180,255,255])

        #upper = np.array([0, 0, 50])
        #lower = np.array([0,0,0])

        #mask = cv2.inRange(hsv, lower, upper)
        '''
        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1 = cv2.inRange(hsv, (5,50,20), (5,255,255))
        mask2 = cv2.inRange(hsv, (175,50,20), (180,255,255))

        ## Merge the mask and crop the red regions
        mask = cv2.bitwise_or(mask1, mask2 )
        croped = cv2.bitwise_and(frame, frame, mask=mask)
        
        print(y_2)
        print(x_2)
        print(z_2)
        
        
        if ret == True: 

            fish = frame.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, blur_coefficient, 0)
            mask = cv2.threshold(blur, 167, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        contours, hierarchy = cv2.findContours(mask, 1,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame, contours, -1, (0,255,0), 1)
        '''
        if len(contours) > 0:
            cont = max(contours,key = c.contourArea)
            momnts = c.moments(cont)

            if momnts["m00"] !=0:3
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
        cv2.imshow('frame', frame)
        cv2.imshow('croped', croped)
        cv2.imshow('mask', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

linefollowing()



