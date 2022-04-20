from multiprocessing import Process
import cv2 as c
import numpy as n

def ss1():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('0.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss2():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('1.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss3():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('2.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss4():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('3.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss5():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('4.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss6():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('5.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss7():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('6.png',frame)
        
    cap.release()
    c.destroyAllWindows()

def ss8():

    cap = c.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,360)

    while True:
        ret, frame = cap.read()

        c.imshow('frame', frame)

        if c.waitKey(1) == ord('q'):
            break
                       
        c.imwrite('7.png',frame)
        
    cap.release()
    c.destroyAllWindows()



def makemosaic():
    
    i1 = c.imread('0.png')
    i2 = c.imread('1.png')
    i3 = c.imread('2.png')
    i4 = c.imread('3.png')
    i5 = c.imread('4.png')
    i6 = c.imread('5.png')
    i7 = c.imread('6.png')
    i8 = c.imread('7.png')

    i1 = c.resize(i1, (100,100))
    i2 = c.resize(i2, (100,100))
    i3 = c.resize(i3, (100,100))
    i4 = c.resize(i4, (100,100))
    i5 = c.resize(i5, (100,100))
    i6 = c.resize(i6, (100,100))
    i7 = c.resize(i7, (100,100))
    i8 = c.resize(i8, (100,100))

    photomosaic_hor1 = n.hstack([i1,i2,i3,i4])
    photomosaic_hor2 = n.hstack([i5,i6,i7,i8])

    photomosaic_final = n.vstack([photomosaic_hor1,photomosaic_hor2])

    c.imshow("photomosaic",photomosaic_final)

    c.waitKey(0)
    c.destroyAllWindows()


def task3stop():
        p1 = Process(target=makemosaic)
        p1.terminate()



