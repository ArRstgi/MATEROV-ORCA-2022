from multiprocessing import Process
import cv2 as c
import numpy as n


def makemosaic():
    
    i1 = c.imread('F1.png')
    i2 = c.imread('F2.png')
    i3 = c.imread('F3.png')
    i4 = c.imread('F4.png')
    i5 = c.imread('F5.png')
    i6 = c.imread('F6.png')
    i7 = c.imread('F7.png')
    i8 = c.imread('F8.png')

    
    i1 = c.resize(i1, (400,400))
    i2 = c.resize(i2, (400,400))
    i3 = c.resize(i3, (400,400))
    i4 = c.resize(i4, (400,400))
    i5 = c.resize(i5, (400,400))
    i6 = c.resize(i6, (400,400))
    i7 = c.resize(i7, (400,400))
    i8 = c.resize(i8, (400,400))
    
    photomosaic_hor1 = n.hstack([i7,i4,i3,i6])
    photomosaic_hor2 = n.hstack([i1,i2,i8,i5])

    photomosaic_final = n.vstack([photomosaic_hor1,photomosaic_hor2])

    #image = c.imread(photomosaic_final)

    c.imshow("photomosaic",photomosaic_final)

    c.waitKey(0)
    c.destroyAllWindows()


makemosaic()