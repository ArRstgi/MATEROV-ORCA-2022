import cv2 as c
import numpy as n

from manual_control import down, stop, up

def linefollower():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        frame = cap.read()

        hsv = c.cvtColor(frame, c.COLOR_BGR2HSV)
        lower = n.array([352.5, 65.7, 91.4])
        upper = n.array([352.6, 87.2, 73.3])

        #upper = n.array([0, 0, 100])
        #lower = n.array([0,0,0])

        mask = c.inRange(hsv, lower, upper)
    
        contours = c.findContours(mask, 1,c.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            cont = max(contours,key = c.contourArea)
            momnts = c.moments(c)

            if momnts["m00"] !=0:
                cont_x = int(momnts['m10']/momnts['m00'])
                cont_y = int(momnts['m01']/momnts['m00'])

                if cont_y >= 190:
                    up()
                
                if cont_y <= 170:
                    down()

                if cont_y < 190 and cont_y > 170 and cont_x > 240:
                    (print("go right"))

                if cont_x < 190 and cont_y > 170 and cont_x < 240:
                    (print("go left"))

                if cont_x < 230 and cont_x > 250 and cont_y > 180:
                    down()


        c.imshow('frame', frame)
        c.imshow('mask', mask)

        if c.waitKey(1) == ord('x'):
            break

    cap.release()
    c.destroyAllWindows()

def task2start():

    linefollower()

def task2stop():

    stop()