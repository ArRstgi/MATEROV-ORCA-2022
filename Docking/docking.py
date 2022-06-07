from multiprocessing import Process
import time
from pymavlink import mavutil


master = mavutil.mavlink_connection('udpin:192.168.2.1:14550')
master.wait_heartbeat()

def forward():
    master.mav.manual_control_send(master.target_system, 1000, 0, 0, 0, 0)

def docking_start(): 
    
    p = Process(target=forward)
    p.start()
    time.sleep(10)
    p.terminate()

docking_start()
