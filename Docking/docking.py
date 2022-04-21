from pymavlink import mavutil
from multiprocessing import Process
import time

from Manual.manual_control import forward, stop

def docking_start(): 
    
    p = Process(target=forward)
    p.start()
    time.sleep(1)
    p.terminate()

def docking_stop():

    p = Process(target=stop)
    p.start()
    time.sleep(1)
    p.terminate()