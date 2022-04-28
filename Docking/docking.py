from multiprocessing import Process
import time
from pymavlink import mavutil


master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
master.wait_heartbeat()

def forward():
    master.mav.manual_control_send(master.target_system, 500, 0, 0, 0, 0)

def docking_start(): 
    
    p = Process(target=forward)
    p.start()
    time.sleep(1)
    p.terminate()

docking_start()
