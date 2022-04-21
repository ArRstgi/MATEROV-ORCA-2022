from pymavlink import mavutil

master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
master.wait_heartbeat()

def forward():
    master.mav.manual_control_send(master.target_system, 500, 0, 0, 0, 0)

def stop():
    master.mav.command_long_send(master.target_system, master.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 0, 0, 0, 0, 0, 0)
    
    master.motors_disarmed_wait()

def up():
    master.mav.manual_control_send(master.target_system, 0, 0, 750, 0, 0)    

def down():
    master.mav.manual_control_send(master.target_system, 0, 0, 250, 0, 0)

def set_rc_channel_pwm(channel_id, pwm=1500):

    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(master.target_system, master.target_component, *rc_channel_values)

def right():

    set_rc_channel_pwm(6,1700)

def left():

    set_rc_channel_pwm(6,1300)







