# Import mavutil
import multiprocessing
from pymavlink import mavutil
from multiprocessing import Process
import time
# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Send a positive x value, negative y, negative z,
# positive rotation and no button.
# https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
# Warning: Because of some legacy workaround, z will work between [0-1000]
# where 0 is full reverse, 500 is no output and 1000 is full throttle.
# x,y and r will be between [-1000 and 1000].

def forward():
    master.mav.manual_control_send(

        # The values correspond to forward/backwards, roll of bot,
        # up/down of a bot, right/left turning 
        # and buttons used (usually 0) respectively

        master.target_system,
        500,
        0,
        0,
        0,
        0)

def stop():
    master.mav.manual_control_send(

        # The values correspond to forward/backwards, roll of bot,
        # up/down of a bot, right/left turning 
        # and buttons used (usually 0) respectively
        
        master.target_system,
        0,
        0,
        0,
        0,
        0)

def up():
    master.mav.manual_control_send(

        # The values correspond to forward/backwards, roll of bot,
        # up/down of a bot, right/left turning 
        # and buttons used (usually 0) respectively
        
        master.target_system,
        0,
        0,
        750,
        0,
        0)    

def down():
    master.mav.manual_control_send(

        # The values correspond to forward/backwards, roll of bot,
        # up/down of a bot, right/left turning 
        # and buttons used (usually 0) respectively
        
        master.target_system,
        0,
        0,
        250,
        0,
        0)

if __name__ == '__main__':

    def task1start(): 
    
        p = multiprocessing.Process(target=forward)
        p.start()
        time.sleep(1)
        p.terminate()
    
    def task1stop():

        p = multiprocessing.Process(target=stop)
        p.start()
        time.sleep(1)
        p.terminate()







