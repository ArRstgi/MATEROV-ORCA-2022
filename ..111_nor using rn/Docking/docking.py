from multiprocessing import Process
import time
from pymavlink import mavutil


master = mavutil.mavlink_connection('udpin:192.168.2.1:14770')
master.wait_heartbeat()

# Arm
# master.arducopter_arm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# wait until arming confirmed (can manually check with master.motors_armed())
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

def forward():
    master.mav.manual_control_send(master.target_system, 1000, 0, 0, 0, 0)

def docking_start(): 
    
    p = Process(target=forward)
    p.start()
    time.sleep(10)
    p.terminate()

docking_start()
