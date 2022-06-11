from multiprocessing import Process
import cv2 as c
import numpy as n

def takeScreenshot(): 
    cap = c.VideoCapture(0) 
    cap.set(3,480)
    cap.set(4,360)

    while True:

        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
        
        elif c.waitKey(1) == ord('1'):
            c.imwrite('1.png',frame)

        elif c.waitKey(1) == ord('2'):
            c.imwrite('2.png',frame)
        
        elif c.waitKey(1) == ord('3'):
            c.imwrite('3.png',frame)
        
        elif c.waitKey(1) == ord('4'):
            c.imwrite('4.png',frame)
        
        elif c.waitKey(1) == ord('5'):
            c.imwrite('5.png',frame)
        
        elif c.waitKey(1) == ord('6'):
            c.imwrite('6.png',frame)

        elif c.waitKey(1) == ord('7'):
            c.imwrite('7.png',frame)
        
        elif c.waitKey(1) == ord('8'):
            c.imwrite('8.png',frame)

    cap.release()
    c.destroyAllWindows()

    return frame

takeScreenshot()
