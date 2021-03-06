from pymavlink import mavutil

master = mavutil.mavlink_connection('udpin:192.168.2.1:14770')
master.wait_heartbeat()

def forward():
    master.mav.manual_control_send(master.target_system, 1000, 0, 0, 0, 0)

def stop():
    master.mav.manual_control_send(master.target_system,  0, 0, 0, 0, 0)
    

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

forward()



