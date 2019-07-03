from wallaby import *
from decorators import *
import constants as c
import movement as m
import gyro as g
import sensors as s

#---------------------------------------------States-------------------------------------------

def isLeftButtonPressed():
    return(left_button() == 1)

def isLeftButtonNotPressed():
    return(left_button() == 0)

def isRightButtonPressed():
    return(right_button() == 1)

def isRightButtonNotPressed():
    return(right_button() == 0)

#---------------------------------------------Functions-------------------------------------------

def setup():
    print "Starting setup()"
    reset_roomba()
    msleep(20)
    g.calibrate_gyro()
    enable_servo(c.ARM_SERVO)
    enable_servo(c.MAGNET_ARM_SERVO)
    enable_servo(c.MICRO_SERVO)
    enable_servo(c.WRIST_SERVO)
    print "Arm servo enabled = %d\n" % get_servo_enabled(c.ARM_SERVO)
    print "Magnet arm servo enabled = %d\n" % get_servo_enabled(c.MAGNET_ARM_SERVO)
    m.move_arm(c.ARM_START_POS)
    m.move_magnet_arm(c.MAGNET_ARM_START_POS)
    m.move_micro(c.MICRO_START_POS)
    m.move_wrist(c.WRIST_START_POS)
    print "Setup complete\n"


def calibrate():
    # Initialize variables.
    c.MIN_SENSOR_VALUE_LCLIFF = 90000
    c.MAX_SENSOR_VALUE_LCLIFF = 0
    c.MAX_SENSOR_VALUE_RCLIFF = 0
    c.MIN_SENSOR_VALUE_RCLIFF = 90000
    c.MAX_SENSOR_VALUE_LFCLIFF = 0
    c.MIN_SENSOR_VALUE_LFCLIFF = 90000
    c.MAX_SENSOR_VALUE_RFCLIFF = 0
    c.MIN_SENSOR_VALUE_RFCLIFF = 90000
    angle = 0
    error = 0
    total_left_speed = 0
    total_right_speed = 0
    run_throughs = 0
    total_tophat_reading = 0
    sec = seconds() + 3
    print "Running calibrate()"
    m.activate_motors(int(c.BASE_LM_POWER / 2), int(c.BASE_RM_POWER / 2))
    while seconds() < sec:
        if get_create_lcliff_amt() > c.MAX_SENSOR_VALUE_LCLIFF:
            c.MAX_SENSOR_VALUE_LCLIFF = get_create_lcliff_amt()
        if get_create_lcliff_amt() < c.MIN_SENSOR_VALUE_LCLIFF:
            c.MIN_SENSOR_VALUE_LCLIFF = get_create_lcliff_amt()
        if get_create_rcliff_amt() > c.MAX_SENSOR_VALUE_RCLIFF:
            c.MAX_SENSOR_VALUE_RCLIFF = get_create_rcliff_amt()
        if get_create_rcliff_amt() < c.MIN_SENSOR_VALUE_RCLIFF:
            c.MIN_SENSOR_VALUE_RCLIFF = get_create_rcliff_amt()
        if get_create_lfcliff_amt() > c.MAX_SENSOR_VALUE_LFCLIFF:
            c.MAX_SENSOR_VALUE_LFCLIFF = get_create_lfcliff_amt()
        if get_create_lfcliff_amt() < c.MIN_SENSOR_VALUE_LFCLIFF:
            c.MIN_SENSOR_VALUE_LFCLIFF = get_create_lfcliff_amt()
        if get_create_rfcliff_amt() > c.MAX_SENSOR_VALUE_RFCLIFF:
            c.MAX_SENSOR_VALUE_RFCLIFF = get_create_rfcliff_amt()
        if get_create_rfcliff_amt() < c.MIN_SENSOR_VALUE_RFCLIFF:
            c.MIN_SENSOR_VALUE_RFCLIFF = get_create_rfcliff_amt()
        total_tophat_reading += analog(c.CLAW_TOPHAT)
        left_speed = int(c.BASE_LM_POWER / 2) + error
        right_speed = int(c.BASE_RM_POWER / 2) - error
        m.activate_motors(left_speed, right_speed)
        total_left_speed += left_speed
        total_right_speed += right_speed
        run_throughs += 1
        msleep(10)
        angle += (gyro_z() - g.bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    m.deactivate_motors()
    c.LCLIFF_BW = ((c.MAX_SENSOR_VALUE_LCLIFF + c.MIN_SENSOR_VALUE_LCLIFF) / 2) - 100
    c.RCLIFF_BW = ((c.MAX_SENSOR_VALUE_RCLIFF + c.MIN_SENSOR_VALUE_RCLIFF) / 2) - 100
    c.LFCLIFF_BW = ((c.MAX_SENSOR_VALUE_LFCLIFF + c.MIN_SENSOR_VALUE_LFCLIFF) / 2) - 100
    c.RFCLIFF_BW = ((c.MAX_SENSOR_VALUE_RFCLIFF + c.MIN_SENSOR_VALUE_RFCLIFF) / 2) - 200
    c.BASE_LM_POWER = int((total_left_speed * 2) / run_throughs)
    c.BASE_RM_POWER = int((total_right_speed * 2) / run_throughs)
    c.FULL_LM_POWER = c.BASE_LM_POWER
    c.FULL_RM_POWER = c.BASE_RM_POWER
    c.HALF_LM_POWER = int(c.BASE_LM_POWER) / 2
    c.HALF_RM_POWER = int(c.BASE_RM_POWER) / 2
    print "LCLIFF_BW: " + str(c.LCLIFF_BW)
    print "RCLIFF_BW: " + str(c.RCLIFF_BW)
    print "LFCLIFF_BW: " + str(c.LFCLIFF_BW)
    print "RFCLIFF_BW: " + str(c.RFCLIFF_BW)
    print "BASE_LM_POWER: " + str(c.BASE_LM_POWER)
    print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
    msleep(100)
    c.CLAW_TOPHAT_NOTHING_READING = total_tophat_reading / run_throughs
    print "\nPut coupler in claw and press the right button..."
    s.wait_until(isRightButtonPressed)
    c.CLAW_TOPHAT_COUPLER_READING = analog(c.CLAW_TOPHAT)
    c.CLAW_TOPHAT_BW = (c.CLAW_TOPHAT_COUPLER_READING + c.CLAW_TOPHAT_NOTHING_READING) / 2
    print "c.CLAW_TOPHAT_BW: " + str(c.CLAW_TOPHAT_BW)
    if c.CLAW_TOPHAT_COUPLER_READING > c.CLAW_TOPHAT_NOTHING_READING:
        print "Coupler reading is higher."
    else:
        print "Nothing reading is higher."
    s.backwards_until_black_cliffs()
    s.align_far_cliffs()
    s.backwards_until_black_lfcliff()
    s.align_far_fcliffs()
    s.backwards_through_line_lfcliff()
    s.align_close_fcliffs()
    m.backwards(200)
    msleep(300)
    ao()
    # DON'T DELETE THESE NEXT 4 LINES. They are purposeful. It avoids the roomba going into sleep mode after the calibration and not starting right.
    create_disconnect()
    wait_for_light(c.LIGHT_SENSOR)
    create_connect()
    shut_down_in(120)  # URGENT: PUT BACK IN BEFORE COMPETITION


def calibrate_with_gyro_angle_calibration():
    # Initialize variables.
    c.MIN_SENSOR_VALUE_LCLIFF = 90000
    c.MAX_SENSOR_VALUE_LCLIFF = 0
    c.MAX_SENSOR_VALUE_RCLIFF = 0
    c.MIN_SENSOR_VALUE_RCLIFF = 90000
    c.MAX_SENSOR_VALUE_LFCLIFF = 0
    c.MIN_SENSOR_VALUE_LFCLIFF = 90000
    c.MAX_SENSOR_VALUE_RFCLIFF = 0
    c.MIN_SENSOR_VALUE_RFCLIFF = 90000
    angle = 0
    error = 0
    total_left_speed = 0
    total_right_speed = 0
    run_throughs = 0
    sec = seconds() + 3
    print "Running calibrate()"
    m.activate_motors(int(c.BASE_LM_POWER / 2), int(c.BASE_RM_POWER / 2))
    while seconds() < sec:
        if get_create_lcliff_amt() > c.MAX_SENSOR_VALUE_LCLIFF:
            c.MAX_SENSOR_VALUE_LCLIFF = get_create_lcliff_amt()
        if get_create_lcliff_amt() < c.MIN_SENSOR_VALUE_LCLIFF:
            c.MIN_SENSOR_VALUE_LCLIFF = get_create_lcliff_amt()
        if get_create_rcliff_amt() > c.MAX_SENSOR_VALUE_RCLIFF:
            c.MAX_SENSOR_VALUE_RCLIFF = get_create_rcliff_amt()
        if get_create_rcliff_amt() < c.MIN_SENSOR_VALUE_RCLIFF:
            c.MIN_SENSOR_VALUE_RCLIFF = get_create_rcliff_amt()
        if get_create_lfcliff_amt() > c.MAX_SENSOR_VALUE_LFCLIFF:
            c.MAX_SENSOR_VALUE_LFCLIFF = get_create_lfcliff_amt()
        if get_create_lfcliff_amt() < c.MIN_SENSOR_VALUE_LFCLIFF:
            c.MIN_SENSOR_VALUE_LFCLIFF = get_create_lfcliff_amt()
        if get_create_rfcliff_amt() > c.MAX_SENSOR_VALUE_RFCLIFF:
            c.MAX_SENSOR_VALUE_RFCLIFF = get_create_rfcliff_amt()
        if get_create_rfcliff_amt() < c.MIN_SENSOR_VALUE_RFCLIFF:
            c.MIN_SENSOR_VALUE_RFCLIFF = get_create_rfcliff_amt()
        left_speed = int(c.BASE_LM_POWER / 2) + error
        right_speed = int(c.BASE_RM_POWER / 2) - error
        m.activate_motors(left_speed, right_speed)
        total_left_speed += left_speed
        total_right_speed += right_speed
        run_throughs += 1
        msleep(10)
        angle += (gyro_z() - g.bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    m.deactivate_motors()
    c.LCLIFF_BW = ((c.MAX_SENSOR_VALUE_LCLIFF + c.MIN_SENSOR_VALUE_LCLIFF) / 2) + 100
    c.RCLIFF_BW = ((c.MAX_SENSOR_VALUE_RCLIFF + c.MIN_SENSOR_VALUE_RCLIFF) / 2) + 100
    c.LFCLIFF_BW = ((c.MAX_SENSOR_VALUE_LFCLIFF + c.MIN_SENSOR_VALUE_LFCLIFF) / 2) + 100
    c.RFCLIFF_BW = ((c.MAX_SENSOR_VALUE_RFCLIFF + c.MIN_SENSOR_VALUE_RFCLIFF) / 2) + 200
    c.BASE_LM_POWER = int((total_left_speed * 2) / run_throughs)
    c.BASE_RM_POWER = int((total_right_speed * 2) / run_throughs)
    c.FULL_LM_POWER = c.BASE_LM_POWER
    c.FULL_RM_POWER = c.BASE_RM_POWER
    c.HALF_LM_POWER = int(c.BASE_LM_POWER) / 2
    c.HALF_RM_POWER = int(c.BASE_RM_POWER) / 2
    print "LCLIFF_BW: " + str(c.LCLIFF_BW)
    print "RCLIFF_BW: " + str(c.RCLIFF_BW)
    print "LFCLIFF_BW: " + str(c.LFCLIFF_BW)
    print "RFCLIFF_BW: " + str(c.RFCLIFF_BW)
    print "BASE_LM_POWER: " + str(c.BASE_LM_POWER)
    print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
    msleep(100)
    s.backwards_until_black_cliffs()
    s.align_far_cliffs()
    s.turn_left_until_lfcliff_senses_black(0)
    g.determine_gyro_conversion_rate()
    msleep(100)
    g.turn_right_gyro(45)
    s.backwards_until_black_lfcliff()
    s.align_far_fcliffs()
    s.backwards_through_line_lfcliff()
    s.align_close_fcliffs()
    m.backwards(200)
    msleep(300)
    ao()
    # DON'T DELETE THESE NEXT 4 LINES. They are purposeful. It avoids the roomba going into sleep mode after the calibration and not starting right.
    create_disconnect()
    msleep(4000)
    #wait_for_light(c.LIGHT_SENSOR)
    create_connect()
    shut_down_in(120)  # URGENT: PUT BACK IN BEFORE COMPETITION


def calibrate_manually():
    calibrateBW_front_cliffs()
    calibrateBW_side_cliffs()


def calibrateBW_front_cliffs(time = 90):
    print "Running calibrateBW_front_cliffs()"
    print "You have %d seconds until calibration ends" % time
    print "Press L(eft) button to continue actual code using default bw_front values"
    print "Press R(ight) button to set cliff bw_front values\n"
    print "Waiting for user input...\n"
    sec = seconds() + time
    while seconds() < sec:
        if isLeftButtonPressed():
            print "Left button pressed. Continuing with code"
            print "Left front cliff bw = %d for actual code" % c.LFCLIFF_BW
            print "Right front cliff bw = %d for actual code\n" % c.RFCLIFF_BW
            break
        elif isRightButtonPressed():
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
    print "Press R(ight) button to set cliff bw_side values\n"
    print "Waiting for user input...\n"
    sec = seconds() + time
    while seconds() < sec:
        if isLeftButtonPressed():
            print "Left button pressed. Continuing with code"
            print "Left side cliff bw = %d for actual code" % c.LCLIFF_BW
            print "Right side cliff bw = %d for actual code\n" % c.RCLIFF_BW
            break
        elif isRightButtonPressed():
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
    m.deactivate_motors()
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


def reset_roomba(ms_before_roomba_turns_back_on=10):
    create_disconnect()
    print "Boi"
    msleep(ms_before_roomba_turns_back_on)
    create_connect()
    print "Connected :)"

#---------------------------------------------Debug-------------------------------------------

@print_function_name
def test_movement():  # Used to see if movements and their defaults function as intended
    print "Testing movement\n"
    m.forwards()
    msleep(500)  # Using msleep() instead of wait() to make sure each command turns off its wheels
    m.backwards()
    msleep(500)
    m.turn_left()
    msleep(500)
    m.turn_right()
    msleep(500)
    print "Testing complete. Exiting...\n"
    exit(86)


@print_function_name
def test_veer(time = 10000):
    m.activate_motors()
    msleep(time)
    m.deactivate_motors()
    sd()


@print_function_name
def test_turns():
    m.turn_left()
    msleep(500)
    m.turn_right()
    sd()


@print_function_name
def test_gyro_turns():
    print "Turning right 90 degrees."
    g.turn_right_gyro()
    msleep(500)
    print "Turning left 90 degrees."
    g.turn_left_gyro()
    msleep(500)
    print "Turning right 180 degrees."
    g.turn_right_gyro(180)
    msleep(500)
    print "Turning left 180 degrees."
    g.turn_left_gyro(180)
    msleep(500)
    print "Turning right 360 degrees."
    g.turn_right_gyro(360)
    msleep(500)
    print "Turning left 360 degrees."
    g.turn_left_gyro(360)
    msleep(500)
    sd()


@print_function_name
def test_bump(time=120):
    sec = seconds() + time
    while seconds() < sec:
        if s.isRightBumped() and s.isLeftBumped():
            print "Bumped on both sides."
        elif s.isLeftBumped() and not(s.isRightBumped()):
            print "Bumped Left."
        elif s.isRightBumped() and not(s.isLeftBumped()):
            print "Bumped Right."
        else:
            print "No Bumps."
        print "\n\n\n\n\n\n\n"
        msleep(100)
    sd()


@print_function_name
def test_ir(time=120):
    sec = seconds() + time
    while seconds() < sec:
        if s.doesIRSenseAnythingAtFront() and s.doesIRSenseAnythingAtSides():
            print "IR is sensing at the front and the side."
        elif s.doesIRSenseAnythingAtFront():
            print "IR is sensing something at the front."
        elif s.doesIRSenseAnythingAtSides():
            print "IR is sensing something at the sides."
        else:
            print "Nothing sensed."
        print "\n\n\n\n\n\n\n"
        msleep(100)
    sd()


@print_function_name
def test_cliffs(time=120):
    sec = seconds() + time
    while seconds() < sec:
        print "Left Cliff: " + str(get_create_lcliff_amt())
        print "Right Cliff: " + str(get_create_rcliff_amt())
        print "Left Front Cliff: " + str(get_create_lfcliff_amt())
        print "Right Front Cliff: " + str(get_create_rfcliff_amt())
        print "\n\n\n\n\n\n\n"
        msleep(100)
    sd()


@print_function_name
def runtest():
    create_connect()
    m.base_forwards()
    msleep(3000)
    m.deactivate_motors()
    create_disconnect()

#--------------------------------------Variable Modifiers-------------------------------------------

#@print_function_name
def halve_speeds():
    c.BASE_LM_POWER = c.HALF_LM_POWER
    c.BASE_RM_POWER = c.HALF_RM_POWER


#@print_function_name
def normalize_speeds():
    c.BASE_LM_POWER = c.FULL_LM_POWER
    c.BASE_RM_POWER = c.FULL_RM_POWER


#@print_function_name
def change_speeds_by(modifier):
    c.BASE_LM_POWER = int(c.BASE_LM_POWER * modifier)
    c.BASE_RM_POWER = int(c.BASE_RM_POWER * modifier)