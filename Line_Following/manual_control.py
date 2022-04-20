from pymavlink import mavutil
from multiprocessing import Process
import time
import cv2 as c
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



def task1start(): 
    
    #Moves forwards for 1 second

    p = Process(target=forward)
    p.start()
    time.sleep(1)
    p.terminate()

def task1stop():

    #Makes the robot stop moving

    p = Process(target=stop)
    p.start()
    time.sleep(1)
    p.terminate()

# Create a function to send RC values
# More information about Joystick channels
# here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.

def right():
    set_rc_channel_pwm(6,1700)

def left():
    set_rc_channel_pwm(6,1300)






