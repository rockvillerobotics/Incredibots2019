from wallaby import *
import constants as c
import movement as m
import sensors as s

#---------------------------------------------States-------------------------------------------

def left_pressed():
    return(left_button() == 1)

def not_left_pressed():
    return(left_button() == 0)

def right_pressed():
    return(right_button() == 1)

def not_right_pressed():
    return(right_button() == 0)

#---------------------------------------------Functions-------------------------------------------

def setup():
    print "Starting setup()"
    create_disconnect()
    msleep(10)
    create_connect()
    msleep(20)
    enable_servo(c.ARM_SERVO)
    print "Servo enabled = %d\n" % get_servo_enabled(c.ARM_SERVO)
    set_servo_position(c.ARM_SERVO, c.ARM_START_POS)
    print "Setup complete\n"    


def calibrate():
    max_sensor_value_rcliff = 0
    min_sensor_value_rcliff = 90000
    max_sensor_value_lcliff = 0
    min_sensor_value_lcliff = 90000
    max_sensor_value_lfcliff = 0
    min_sensor_value_lfcliff = 90000
    max_sensor_value_rfcliff = 0
    min_sensor_value_rfcliff = 90000
    sec = seconds() + 9
    print "Running calibrate()"
    m.activate_motors(-1, int(c.BASE_LM_POWER / 2), int(c.BASE_RM_POWER / 2))
    print str(int(c.BASE_LM_POWER / 2))
    print str(int(c.BASE_RM_POWER / 2))
    while seconds() < sec:
        if get_create_rcliff_amt() > max_sensor_value_rcliff:
            max_sensor_value_rcliff = get_create_rcliff_amt()
        if get_create_rcliff_amt() < min_sensor_value_rcliff:
            min_sensor_value_rcliff = get_create_rcliff_amt()
        if get_create_lcliff_amt() > max_sensor_value_lcliff:
            max_sensor_value_lcliff = get_create_lcliff_amt()
        if get_create_lcliff_amt() < min_sensor_value_lcliff:
            min_sensor_value_lcliff = get_create_lcliff_amt()
        if get_create_rfcliff_amt() > max_sensor_value_rfcliff:
            max_sensor_value_rfcliff = get_create_rfcliff_amt()
        if get_create_rfcliff_amt() < min_sensor_value_rfcliff:
            min_sensor_value_rfcliff = get_create_rfcliff_amt()
        if get_create_lfcliff_amt() > max_sensor_value_lfcliff:
            max_sensor_value_lfcliff = get_create_lfcliff_amt()
        if get_create_lfcliff_amt() < min_sensor_value_lfcliff:
            min_sensor_value_lfcliff = get_create_lfcliff_amt()
        msleep(1)
    m.deactivate_motors()
    c.LCLIFF_BW = ((max_sensor_value_lcliff + min_sensor_value_lcliff) / 2) + 750
    c.RCLIFF_BW = ((max_sensor_value_rcliff + min_sensor_value_rcliff) / 2) + 750
    c.LFCLIFF_BW = ((max_sensor_value_lfcliff + min_sensor_value_lfcliff) / 2) + 770
    c.RFCLIFF_BW = ((max_sensor_value_rfcliff + min_sensor_value_rfcliff) / 2) + 1000
    print "LCLIFF_BW: " + str(c.LCLIFF_BW)
    print "RCLIFF_BW: " + str(c.RCLIFF_BW)
    print "LFCLIFF_BW: " + str(c.LFCLIFF_BW)
    print "RFCLIFF_BW: " + str(c.RFCLIFF_BW)
    print "max_sensor_value_rcliff: " + str(max_sensor_value_rcliff)
    print "min_sensor_value_rcliff: " + str(min_sensor_value_rcliff)
    msleep(500)
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    msleep(300)
    s.forwards_until_black_lcliff()
    s.align_close_cliffs()
    msleep(300)
    s.forwards_until_bump()
    m.backwards(100)
    #m.activate_motors(1)
    #msleep(4250)
    #m.deactivate_motors()
    msleep(1500)
    ao()
    # DON'T DELETE THESE NEXT 4 LINES. They are purposeful. It avoids the roomba going into sleep mode after the calibration and not starting right.
    create_disconnect()
    wait_for_light(c.LIGHT_SENSOR)
    create_connect()
    shut_down_in(120)  # URGENT: PUT BACK IN BEFORE COMPETITION


def calibrate_manually():
    calibrateBW_front_cliffs()
    calibrateBW_side_cliffs()


def calibrateBW_front_cliffs(time = 90):
    print "Running calibrateBW_front_cliffs()"
    print "You have %d seconds until calibration ends" % time
    print "Press L(eft) button to continue actual code using default bw_front values"
    print "Press R(ight) button to set tophat bw_front values\n"
    print "Waiting for user input...\n"
    sec = seconds() + time
    while seconds() < sec:
        if left_pressed():
            print "Left button pressed. Continuing with code"
            print "Left front cliff bw = %d for actual code" % c.LFCLIFF_BW
            print "Right front cliff bw = %d for actual code\n" % c.RFCLIFF_BW
            break
        elif right_pressed():
            print "Right button pressed"
            print "Calculating bw_front values...\n\n"
            c.LFCLIFF_BW = get_create_lfcliff_amt()
            c.RFCLIFF_BW = get_create_rfcliff_amt()
            msleep(1000)
            print "Left front cliff bw = %d now" % c.LFCLIFF_BW
            print "Right front cliff bw = %d now\n" % c.RFCLIFF_BW
            print "If satisfied with above bw_front values, press L(eft) button"
            print "If not, press R(ight) button again"
            print "Waiting for user input...\n"
    print "Cliff bw_front calibration complete"
    print "To user: Put robot in starting position"
    msleep(1000)

    
def calibrateBW_side_cliffs(time = 90):
    print "Running calibrateBW_side_cliffs()"
    print "You have %d seconds until calibration ends" % time
    print "Press L(eft) button to continue actual code using default bw_side values"
    print "Press R(ight) button to set tophat bw_side values\n"
    print "Waiting for user input...\n"
    sec = seconds() + time
    while seconds() < sec:
        if left_pressed():
            print "Left button pressed. Continuing with code"
            print "Left side cliff bw = %d for actual code" % c.LCLIFF_BW
            print "Right side cliff bw = %d for actual code\n" % c.RCLIFF_BW
            break
        elif right_pressed():
            print "Right button pressed"
            print "Calculating bw_side values...\n\n"
            c.LCLIFF_BW = get_create_lcliff_amt()
            c.RCLIFF_BW = get_create_rcliff_amt()
            msleep(1000)
            print "Left side cliff bw = %d now" % c.LCLIFF_BW
            print "Right side cliff bw = %d now" % c.RCLIFF_BW
            print "If satisfied with above bw_side values, press L(eft) button"
            print "If not, press R(ight) button again"
            print "Waiting for user input...\n"
    print "Cliff bw_side calibration complete"
    print "To user: Put robot in starting position"
    msleep(2000)
    #wait_for_light(c.LIGHT_SENSOR)
    shut_down_in(100)


def shutdown(value = 255):
    print "Shutdown started"
    create_stop()
    msleep(25)
    ao()
    create_disconnect()
    disable_servos()
    print "Shutdown completed"
    if value < 255:
        print "Exiting...\n"
        exit(value)


def sd():
    shutdown(86)

#---------------------------------------------Debug-------------------------------------------

def test_movement():  # Used to see if movements and their defaults function as intended
    print "Testing movement\n"
    m.drive()
    msleep(500)  # Using msleep() instead of wait() to make sure each command turns off its wheels
    m.backwards()
    msleep(500)
    m.turn_left()
    msleep(500)
    m.turn_right()
    msleep(500)
    print "Testing complete. Exiting...\n"
    exit(86)


def test_veer(time = 10000):
    m.activate_motors()
    msleep(time)
    m.deactivate_motors()
    sd()


def test_turns():
    m.turn_left()
    msleep(500)
    m.turn_right()
    sd()

def test_servos():  # Used to see if basic servo commands and constants function as intended
    print "Testing servos\n"
    #m.extend_elbow()
    #m.wait()  # Using wait() instead of msleep() to make sure wheels are off
    #m.flex_elbow()
    #m.wait()
    #m.shoulder_up()
    #m.wait()
    #m.shoulder_down()
    #m.wait()
    print "Testing complete. Exiting...\n"
    exit(86)


def runtest():
    create_connect()
    create_drive_direct(100,100)
    msleep(3000)
    create_stop()
    create_disconnect()
