import cv2 as c
import numpy as n

cap = c.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = c.cvtColor(frame, c.COLOR_BGR2HSV)
    #lower = n.array([352.5, 65.7, 91.4])
    #upper = n.array([352.6, 87.2, 73.3])

    upper = n.array([0, 0, 100])
    lower = n.array([0,0,0])


    mask = c.inRange(hsv, lower, upper)
    result = c.bitwise_and(frame, frame, mask=mask)

    c.imshow('frame', result)
    #c.imshow('mask', mask)

    if c.waitKey(1) == ord('x'):
        break

cap.release()
c.destroyAllWindows()

def linefollow():

    a = 1

def task2start():

    a = 1

def task2stop():

    a = 1