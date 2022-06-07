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
            c.imwrite('1.jpg',frame)

        elif c.waitKey(1) == ord('2'):
            c.imwrite('2.jpg',frame)
        
        elif c.waitKey(1) == ord('3'):
            c.imwrite('3.jpg',frame)
        
        elif c.waitKey(1) == ord('4'):
            c.imwrite('4.jpg',frame)
        
        elif c.waitKey(1) == ord('5'):
            c.imwrite('5.jpg',frame)
        
        elif c.waitKey(1) == ord('6'):
            c.imwrite('6.jpg',frame)

        elif c.waitKey(1) == ord('7'):
            c.imwrite('7.jpg',frame)
        
        elif c.waitKey(1) == ord('8'):
            c.imwrite('8.jpg',frame)

    cap.release()
    c.destroyAllWindows()

    return frame

def makemosaic():
    
    i1 = c.imread('A1.jpg')
    i2 = c.imread('A2.jpg')
    i3 = c.imread('A3.jpg')
    i4 = c.imread('A4.jpg')
    i5 = c.imread('A5.jpg')
    i6 = c.imread('A6.jpg')
    i7 = c.imread('A7.jpg')
    i8 = c.imread('A8.jpg')

    '''
    i1 = c.resize(i1, (100,100))
    i2 = c.resize(i2, (100,100))
    i3 = c.resize(i3, (100,100))
    i4 = c.resize(i4, (100,100))
    i5 = c.resize(i5, (100,100))
    i6 = c.resize(i6, (100,100))
    i7 = c.resize(i7, (100,100))
    i8 = c.resize(i8, (100,100))
    '''
    photomosaic_hor1 = n.hstack([i1,i2,i3,i4])
    photomosaic_hor2 = n.hstack([i5,i6,i7,i8])

    photomosaic_final = n.vstack([photomosaic_hor1,photomosaic_hor2])

    #image = c.imread(photomosaic_final)

    c.imshow("photomosaic",photomosaic_final)

    c.waitKey(0)
    c.destroyAllWindows()

makemosaic()

