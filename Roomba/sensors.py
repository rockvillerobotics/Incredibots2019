from wallaby import *
from decorators import *
import constants as c
import sensors as s
import gyro as g
import movement as m
import utils as u

#---------------------------------------------States-------------------------------------------

def isLeftOnBlack():
    return(get_create_lcliff_amt() < c.LCLIFF_BW)

def isLeftOnWhite():
    return(get_create_lcliff_amt() > c.LCLIFF_BW)

def isRightOnBlack():
    return(get_create_rcliff_amt() < c.RCLIFF_BW)

def isRightOnWhite():
    return(get_create_rcliff_amt() > c.RCLIFF_BW)

def isLeftFrontOnBlack():
    return(get_create_lfcliff_amt() < c.LFCLIFF_BW)

def isLeftFrontOnWhite():
    return(get_create_lfcliff_amt() > c.LFCLIFF_BW)

def isRightFrontOnBlack():
    return(get_create_rfcliff_amt() < c.RFCLIFF_BW)

def isRightFrontOnWhite():
    return(get_create_rfcliff_amt() > c.RFCLIFF_BW)

def isRoombaBumped():
    return(isLeftBumped() or isRightBumped())

def isRoombaNotBumped():
    return(not(isLeftBumped() or isRightBumped()))

def isBothBumped():
    return(isLeftBumped() and isRightBumped())

def isBothNotBumped():
    return(isLeftBumped() and isRightBumped())

def isLeftBumped():
    return(get_create_lbump() == 1)

def isLeftNotBumped():
    return(get_create_lbump() == 0)

def isRightBumped():
    return(get_create_rbump() == 1)

def isRightNotBumped():
    return(get_create_rbump() == 0)

def doesIRSenseAnythingAtSides():
    return(doesLeftIRSenseAnything() or doesRightIRSenseAnything())

def doesIRSenseNothingAtSides():
    return(not(doesLeftIRSenseAnything() or doesRightIRSenseAnything()))

def doesIRSenseAnythingAtFront():
    return(doesLeftFrontIRSenseAnything() or doesRightFrontIRSenseAnything())

def doesIRSenseNothingAtFront():
    return(not(doesLeftFrontIRSenseAnything() or doesRightFrontIRSenseAnything()))

def doesLeftIRSenseAnything():
    return(get_create_lclightbump() == 1)

def doesLeftIRSenseNothing():
    return(get_create_lclightbump() == 0)

def doesLeftFrontIRSenseAnything():
    return(get_create_lflightbump() == 1)

def doesLeftFrontIRSenseNothing():
    return(get_create_lflightbump() == 0)

def doesRightIRSenseAnything():
    return(get_create_rclightbump() == 1)

def doesRightIRSenseNothing():
    return(get_create_rclightbump() == 0)

def doesRightFrontIRSenseAnything():
    return(get_create_rflightbump() == 1)

def doesRightFrontIRSenseNothing():
    return(get_create_rflightbump() == 0)

def isDepthSensed():
    return(analog(c.DEPTH_SENSOR) > c.DEPTH_CF)

def isDepthNotSensed():
    return(analog(c.DEPTH_SENSOR) < c.DEPTH_CF)

def isSecondDepthSensed():
    return(analog(c.SECOND_DEPTH_SENSOR) > c.SECOND_DEPTH_CF)

def isSecondDepthNotSensed():
    return(analog(c.SECOND_DEPTH_SENSOR) < c.SECOND_DEPTH_CF)

def isBumpSwitchPressed():
    return(digital(c.BUMP_SWITCH) == 1)

def isBumpSwitchNotPressed():
    return(digital(c.BUMP_SWITCH) == 0)

def isItemInClaw():
    if c.CLAW_TOPHAT_COUPLER_READING > c.CLAW_TOPHAT_BW:
        return(analog(c.CLAW_TOPHAT) > c.CLAW_TOPHAT_BW)
    else:
        return(analog(c.CLAW_TOPHAT) < c.CLAW_TOPHAT_BW)

def isNothingInClaw():
    if c.CLAW_TOPHAT_COUPLER_READING > c.CLAW_TOPHAT_BW:
        return(analog(c.CLAW_TOPHAT) < c.CLAW_TOPHAT_BW)
    else:
        return(analog(c.CLAW_TOPHAT) > c.CLAW_TOPHAT_BW)

# ---------------------- Wait Until Condition Commands --------------------------------------------

def wait_until(boolean, time=c.SAFETY_TIME):
    sec = seconds() + time
    while seconds() < sec and not(boolean()):
        msleep(1)

def wait_until_pressed_bump_switch(time=c.SAFETY_TIME):
    wait_until(isBumpSwitchPressed, time)


def wait_until_not_pressed_bump_switch(time=c.SAFETY_TIME):
    wait_until(isBumpSwitchNotPressed, time)


def wait_until_item_in_claw(time=c.SAFETY_TIME):
    wait_until(isItemInClaw, time)


def wait_until_nothing_in_claw(time=c.SAFETY_TIME):
    wait_until(isNothingInClaw, time)

#-------------------------------------Basic Movement Until Cliff----------------------------------------------

@print_function_name
def forwards_until_black_lcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_white_lcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_black_rcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_white_rcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_black_lfcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_white_lfcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_black_rfcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_white_rfcliff(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_black_lcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    while isLeftOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_white_lcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_black_rcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_white_rcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_black_lfcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_white_lfcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_black_rfcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_white_rfcliff(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_black_cliffs(time=c.SAFETY_TIME):
#  Goes forwards until both sensors have sensed black.
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite() and isRightOnWhite():
        msleep(1)
    if isLeftOnBlack():
        while isRightOnWhite():
            msleep(1)
    else:
        while isLeftOnWhite():
            msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_black_fcliffs(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite() and isRightFrontOnWhite():
        msleep(1)
    if isLeftFrontOnBlack():
        while isRightFrontOnWhite():
            msleep(1)
    else:
        while isLeftFrontOnWhite():
            msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_black_cliffs(time=c.SAFETY_TIME):
#  Goes backwards until both sensors have sensed black.
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite() and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_black_fcliffs(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite() and isRightFrontOnWhite():
        msleep(1)
    if isLeftFrontOnBlack():
        while isRightFrontOnWhite():
            msleep(1)
    else:
        while isLeftFrontOnWhite():
            msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name_only_at_beginning
def forwards_through_line_lcliff(time=c.SAFETY_TIME):
    forwards_until_black_lcliff(0)
    forwards_until_white_lcliff(time)


@print_function_name_only_at_beginning
def forwards_through_line_rcliff(time=c.SAFETY_TIME):
    forwards_until_black_rcliff(0)
    forwards_until_white_rcliff(time)


@print_function_name_only_at_beginning
def forwards_through_line_lfcliff(time=c.SAFETY_TIME):
    forwards_until_black_lfcliff(0)
    forwards_until_white_lfcliff(time)


@print_function_name_only_at_beginning
def forwards_through_line_rfcliff(time=c.SAFETY_TIME):
    forwards_until_black_rcliff(0)
    forwards_until_white_rfcliff(time)


@print_function_name_only_at_beginning
def backwards_through_line_lcliff(time=c.SAFETY_TIME):
    backwards_until_black_lcliff(0)
    backwards_until_white_lcliff(time)


@print_function_name_only_at_beginning
def backwards_through_line_rcliff(time=c.SAFETY_TIME):
    backwards_until_black_rcliff(0)
    backwards_until_white_rcliff(time)


@print_function_name_only_at_beginning
def backwards_through_line_lfcliff(time=c.SAFETY_TIME):
    backwards_until_black_lfcliff(0)
    backwards_until_white_lfcliff(time)


@print_function_name_only_at_beginning
def backwards_through_line_rfcliff(time=c.SAFETY_TIME):
    backwards_until_black_rfcliff(0)
    backwards_until_white_rfcliff(time)

#---------------------------------------------Line Follow Functions-------------------------------------------

@print_function_name
def lfollow_left(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):  # Line follow with the left cliff for time
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec:
        if isLeftOnBlack():
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif isLeftOnWhite():
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()


@print_function_name
def lfollow_left_front(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):  # Line follow with the left cliff for time
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec:
        if isLeftFrontOnBlack():
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif isLeftFrontOnWhite():
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()


@print_function_name
def lfollow_left_inside_line(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec:
        if isLeftOnBlack():
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        else:
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()


@print_function_name
def lfollow_right(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):  # Line follow with the right cliff for time
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec:
        if isRightOnBlack():
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
        elif not isRightOnBlack():
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()


@print_function_name
def lfollow_lfcliff_smooth_until_rfcliff_senses_black():
    while isRightFrontOnWhite():
        if isLeftFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()


@print_function_name
def lfollow_lfcliff_smooth(time):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec:
        if isLeftFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()


@print_function_name
def lfollow_lfcliff_smooth_until_rfcliff_senses_white():
    while isRightFrontOnBlack():
        if isLeftFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()

#--------------------------------------PID Line Follows-------------------------------------------------

def lfollow_rcliff_pid(time, bias=10):
    target = 100.0 * (c.RCLIFF_BW - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_rcliff_amt() - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.55
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6666
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rcliff_pid_value_testing(time, bias=10):
    target = 100.0 * (c.RCLIFF_BW - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF) + bias
    last_error = 0
    integral = 0
    kp = c.KP
    ki = c.KI
    kd = c.KD
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_rcliff_amt() - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
        if u.isRightButtonPressed():
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_SENSOR_VALUE_RCLIFF: " + str(c.MAX_SENSOR_VALUE_RCLIFF)
            print "c.MIN_SENSOR_VALUE_RCLIFF: " + str(c.MIN_SENSOR_VALUE_RCLIFF)
            msleep(30)

    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rcliff_until_lcliff_senses_black_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.RCLIFF_BW - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnWhite():
        norm_reading = 100.0 * (get_create_rcliff_amt() - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rcliff_inside_line_pid(time, bias=10):
    target = 100.0 * (c.RCLIFF_BW - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_rcliff_amt() - c.MIN_SENSOR_VALUE_RCLIFF) / (c.MAX_SENSOR_VALUE_RCLIFF - c.MIN_SENSOR_VALUE_RCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lcliff_pid(time, bias=10):
    target = 100.0 * (c.LCLIFF_BW - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_lcliff_amt() - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lcliff_value_testing_pid(time, bias=10):
    target = 100.0 * (c.LCLIFF_BW - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF) + bias
    last_error = 0
    integral = 0
    kp = c.KP
    ki = c.KI
    kd = c.KD
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_lcliff_amt() - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
        if u.isRightButtonPressed():
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_SENSOR_VALUE_RCLIFF: " + str(c.MAX_SENSOR_VALUE_RCLIFF)
            print "c.MIN_SENSOR_VALUE_RCLIFF: " + str(c.MIN_SENSOR_VALUE_RCLIFF)
            msleep(30)

    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lcliff_until_rcliff_senses_black_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.LCLIFF_BW - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnWhite():
        norm_reading = 100.0 * (get_create_lcliff_amt - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()



def lfollow_lcliff_inside_line_pid(time, bias=10):
    target = 100.0 * (c.LCLIFF_BW - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_lcliff_amt - c.MIN_SENSOR_VALUE_LCLIFF) / (c.MAX_SENSOR_VALUE_LCLIFF - c.MIN_SENSOR_VALUE_LCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_pid(time, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_pid_value_testing(time, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    kp = c.KP
    ki = c.KI
    kd = c.KD
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
        if u.isRightButtonPressed():
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_SENSOR_VALUE_RFCLIFF: " + str(c.MAX_SENSOR_VALUE_RFCLIFF)
            print "c.MIN_SENSOR_VALUE_RFCLIFF: " + str(c.MIN_SENSOR_VALUE_RFCLIFF)
            msleep(30)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_until_lfcliff_senses_black_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnWhite():
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) - (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_until_lfcliff_senses_white_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnBlack():
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) - (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_until_bump_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(isRoombaBumped()):
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error + last_error  # If rate of change is going negative, need to veer right
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 2
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6667
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_inside_line_pid(time, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()



def lfollow_rfcliff_inside_line_until_lfcliff_senses_black_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(isLeftFrontOnBlack()):
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error + last_error  # If rate of change is going negative, need to veer right
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 2
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6667
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_rfcliff_inside_line_until_lfcliff_senses_white_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.RFCLIFF_BW - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnBlack():
        norm_reading = 100.0 * (get_create_rfcliff_amt() - c.MIN_SENSOR_VALUE_RFCLIFF) / (c.MAX_SENSOR_VALUE_RFCLIFF - c.MIN_SENSOR_VALUE_RFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error + last_error  # If rate of change is going negative, need to veer right
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 2
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6667
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_pid(time, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_value_testing_pid(time, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    kp = c.KP
    ki = c.KI
    kd = c.KD
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
        if u.isRightButtonPressed():
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_SENSOR_VALUE_RFCLIFF: " + str(c.MAX_SENSOR_VALUE_RFCLIFF)
            print "c.MIN_SENSOR_VALUE_RFCLIFF: " + str(c.MIN_SENSOR_VALUE_RFCLIFF)
            msleep(30)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_until_rfcliff_senses_black_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnWhite():
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) - (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_until_rfcliff_senses_white_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnBlack():
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) - (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_until_bump_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(isRoombaBumped()):
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 2
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6667
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_inside_line_pid(time, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 1.56
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.67
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_inside_line_until_rfcliff_senses_black_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(isRightFrontOnBlack()):
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 2
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6667
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_lfcliff_inside_line_until_rfcliff_senses_white_pid(time=c.SAFETY_TIME, bias=10):
    target = 100.0 * (c.LFCLIFF_BW - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF) + bias
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnBlack():
        norm_reading = 100.0 * (get_create_lfcliff_amt() - c.MIN_SENSOR_VALUE_LFCLIFF) / (c.MAX_SENSOR_VALUE_LFCLIFF - c.MIN_SENSOR_VALUE_LFCLIFF)
        error = target - norm_reading  # Positive error means black, negative means white.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 2
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 0.6667
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        create_drive_direct(int(left_power), int(right_power))
        c.CURRENT_LM_POWER = left_power
        c.CURRENT_RM_POWER = right_power
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

#--------------------------------------Depth Functions--------------------------------------------------

@print_function_name
def backwards_until_depth(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isDepthNotSensed():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_not_depth(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isDepthSensed():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_depth(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isDepthNotSensed():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def lfollow_lfcliff_smooth_until_depth(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isDepthNotSensed:
        if isLeftFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wait_for_depth(time=c.SAFETY_TIME):
    sec = seconds() + time
    while isDepthNotSensed() and seconds() < sec:
        msleep(10)


@print_function_name
def wait_for_not_depth(time=c.SAFETY_TIME):
    sec = seconds() + time
    while isDepthSensed() and seconds() < sec:
        msleep(10)


@print_function_name
def wait_for_second_depth(time=c.SAFETY_TIME):
    sec = seconds() + time
    while isSecondDepthNotSensed() and seconds() < sec:
        msleep(10)


@print_function_name
def wait_for_not_second_depth(time=c.SAFETY_TIME):
    sec = seconds() + time
    while isSecondDepthSensed() and seconds() < sec:
        msleep(10)

#----------------------------------------------Bump-------------------------------------------
#-------Base Bumps---------

def base_wfollow_left(speed=1):
    if isRoombaBumped():
        if isRightBumped():
            m.backwards(100)
            m.turn_right()
        else:
            if c.FIRST_BUMP == True:
                m.deactivate_motors()
            u.halve_speeds()
            m.base_turn_right()
            c.FIRST_BUMP = False
        msleep(50)
    else:
        m.base_veer_left(0.6)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    u.change_speeds_by(speed)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_wfollow_right():
    if isRoombaBumped():
        if isLeftBumped():
            m.backwards(100)
            m.turn_left()
        else:
            if c.FIRST_BUMP == True:
                m.deactivate_motors()
            u.halve_speeds()
            m.base_turn_left()
            c.FIRST_BUMP = False
    else:
        m.base_veer_right(0.6)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_wfollow_left_smooth(speed):
    if isRoombaBumped():
        #if c.FIRST_BUMP == True:
            #m.deactivate_motors()
        if speed == 1:
            c.BASE_LM_POWER = c.FULL_LM_POWER * 1.3
        m.base_veer_right(0.9)
        c.FIRST_BUMP = False
    else:

        m.base_veer_left(0.9)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    u.change_speeds_by(speed)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_wfollow_right_smooth(speed):
    if isRoombaBumped():
        #if c.FIRST_BUMP == True:
            #m.deactivate_motors()
        if speed == 1:
            c.BASE_LM_POWER = c.FULL_LM_POWER * 1.3
        m.base_veer_left(0.9)
        c.FIRST_BUMP = False
    else:

        m.base_veer_right(0.9)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    u.change_speeds_by(speed)
    msleep(c.LFOLLOW_REFRESH_RATE)
            

def base_wfollow_right_backwards_smooth():
    u.change_speeds_by(-1)
    if isRoombaBumped():
        #if c.FIRST_BUMP == True:
            #m.deactivate_motors()
        m.base_veer_right(0.95)
        c.FIRST_BUMP = False
    else:

        m.base_veer_left(0.65)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_wfollow_left_slowly_smooth(speed=0.3):
    if isRoombaBumped():
        if c.FIRST_BUMP == True:
            m.deactivate_motors()
        m.base_veer_right(0.2)
        c.FIRST_BUMP = False
    else:
        m.base_veer_left(0.6)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    u.change_speeds_by(speed)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_wfollow_right_slowly_smooth(speed=0.3):
    if isRoombaBumped():
        if c.FIRST_BUMP == True:
            m.deactivate_motors()
        m.base_veer_left(0.2)
        c.FIRST_BUMP = False
    else:
        m.base_veer_right(0.6)
        c.FIRST_BUMP = True
    u.normalize_speeds()
    u.change_speeds_by(speed)
    msleep(c.LFOLLOW_REFRESH_RATE)

#-------Movement Bumps---------

@print_function_name
def forwards_until_bump(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRoombaNotBumped():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_until_pressed_bump_switch(time=c.SAFETY_TIME):
    m.base_backwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    wait_until_pressed_bump_switch(time)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

            
#------- Wall-Aligns ---------

@print_function_name
def align_on_wall_left():
    m.base_veer_left(0.5)
    wait_until(isRoombaBumped)
    m.deactivate_motors()
    u.halve_speeds()
    m.base_turn_right()
    wait_until(isRoombaNotBumped)
    m.deactivate_motors()
    msleep(100)
    g.turn_left_gyro(4)
    msleep(500)


print_function_name
def align_on_wall_right():
    m.base_veer_right(0.5)
    wait_until(isRoombaBumped)
    m.deactivate_motors()
    u.halve_speeds()
    m.base_turn_left()
    wait_until(isRoombaNotBumped)
    m.deactivate_motors()
    msleep(100)
    g.turn_right_gyro(4)
    msleep(500)

#------- Wall-Based Bumps ---------
# "wfollow" means "wall follow."

@print_function_name
def wfollow_left(time, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_wfollow_left(speed)
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_until(boolean, speed=1, time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        base_wfollow_left(speed)
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
       

@print_function_name
def wfollow_left_until_second_depth(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_until(isSecondDepthSensed, speed, time)


@print_function_name
def wfollow_left_until_not_second_depth(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_until(isSecondDepthNotSensed, speed, time)


@print_function_name
def wfollow_left_until_black_left(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnWhite():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_until_white_left(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnBlack():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_until_black_right(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnWhite():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_until_white_right(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnBlack():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def wfollow_left_until_black_left_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnWhite():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()



@print_function_name
def wfollow_left_until_white_left_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnBlack():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_smooth_until_white_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isRightOnWhite, speed)


@print_function_name
def wfollow_right_until_black_left_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnWhite():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_until_black_right_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnWhite():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()



@print_function_name
def wfollow_left_until_white_right_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnBlack():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_until_white_left_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftFrontOnBlack():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_until_black_left(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnWhite():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_until_white_left(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnBlack():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()



@print_function_name
def wfollow_right_until_black_right(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnWhite():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_until_white_right(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnBlack():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_until_black_right_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnWhite():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_right_until_white_right_front(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightFrontOnBlack():
        base_wfollow_right()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
            
####

@print_function_name
def wfollow_left_until_second_depth_sensed(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isSecondDepthNotSensed():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_until_second_depth_not_sensed(time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and isSecondDepthSensed():
        base_wfollow_left()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

@print_function_name
def wfollow_right_through_line_lfcliff(time=c.SAFETY_TIME):
    wfollow_right_until_black_left_front(0)
    wfollow_right_until_white_left_front(time)

        
@print_function_name
def wfollow_right_through_line_rfcliff(time=c.SAFETY_TIME):
    wfollow_right_until_black_right_front(0)
    wfollow_right_until_white_right_front(time)

@print_function_name
def wfollow_right_through_line_lcliff(time=c.SAFETY_TIME):
    wfollow_right_until_black_left(0)
    wfollow_right_until_white_left(time)

@print_function_name
def wfollow_right_through_line_rcliff(time=c.SAFETY_TIME):
    wfollow_right_until_black_right(0)
    wfollow_right_until_white_right(time)


# ---------- Wall Follow Smooth Commands -------------------
@print_function_name
def wfollow_left_smooth_until(boolean, speed, time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        base_wfollow_left_smooth(speed)
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def wfollow_left_smooth_slowly_until(boolean, speed=0.3, time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        base_wfollow_left_slowly_smooth(speed)
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

            
@print_function_name
def wfollow_left_smooth_slowly(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_wfollow_left_slowly_smooth(speed)
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
            
            
@print_function_name
def wfollow_left_smooth_slowly_until_second_depth(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_slowly_until(isSecondDepthSensed, speed, time)


@print_function_name
def wfollow_left_smooth_slowly_until_not_second_depth(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_slowly_until(isSecondDepthNotSensed, speed, time)


@print_function_name
def wfollow_left_smooth_until_black_lfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isLeftFrontOnBlack, speed, time)


@print_function_name
def wfollow_left_smooth_until_black_rfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isRightFrontOnBlack, speed, time)


@print_function_name
def wfollow_left_smooth_until_black_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isLeftOnBlack, speed, time)


@print_function_name
def wfollow_left_smooth_until_black_rcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isRightOnBlack, speed, time)


@print_function_name
def wfollow_left_smooth_until_white_lfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isLeftFrontOnWhite, speed, time)


@print_function_name
def wfollow_left_smooth_until_white_lfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isRightFrontOnWhite, speed, time)


@print_function_name
def wfollow_left_smooth_until_white_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isLeftOnWhite, speed, time)


@print_function_name
def wfollow_left_smooth_until_white_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_left_smooth_until(isRightOnWhite, speed, time)
 
@print_function_name
def wfollow_right_smooth_until(boolean, speed, time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        base_wfollow_right_smooth(speed)
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

            
@print_function_name
def wfollow_right_backwards_smooth_until(boolean, speed, time=c.SAFETY_TIME, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        base_wfollow_right_backwards_smooth()
    u.normalize_speeds()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()        
      
            
@print_function_name
def wfollow_right_smooth_until_second_depth(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isSecondDepthSensed, speed, time)


@print_function_name
def wfollow_right_smooth_until_not_second_depth(time=c.SAFETY_TIME, speed=0.3, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isSecondDepthNotSensed, speed, time)


@print_function_name
def wfollow_right_smooth_until_black_lfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isLeftFrontOnBlack, speed, time)


@print_function_name
def wfollow_right_smooth_until_black_rfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isRightFrontOnBlack, speed, time)


@print_function_name
def wfollow_right_smooth_until_black_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isLeftOnBlack, speed, time)


@print_function_name
def wfollow_right_smooth_until_black_rcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isRightOnBlack, speed, time)


@print_function_name
def wfollow_right_smooth_until_white_lfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isLeftFrontOnWhite, speed, time)


@print_function_name
def wfollow_right_smooth_until_white_lfcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isRightFrontOnWhite, speed, time)


@print_function_name
def wfollow_right_smooth_until_white_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_smooth_until(isLeftOnWhite, speed, time)
        
        
@print_function_name
def wfollow_right_backwards_smooth_until_black_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_backwards_smooth_until(isLeftOnBlack, speed, time)

        
@print_function_name
def wfollow_right_backwards_smooth_until_white_lcliff(time=c.SAFETY_TIME, speed=1, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    wfollow_right_backwards_smooth_until(isLeftOnWhite, speed, time)
#----------------------------------------------Align Functions-------------------------------------------

@print_function_name_only_at_beginning
def align_close_fcliffs():
    right_front_backwards_until_white()
    left_front_backwards_until_white()
    right_front_forwards_until_black()
    left_front_forwards_until_black()


@print_function_name_only_at_beginning
def align_far_fcliffs():
    left_front_forwards_until_white()
    right_front_forwards_until_white()
    left_front_backwards_until_black()
    right_front_backwards_until_black()


@print_function_name_only_at_beginning
def align_close_cliffs():
    left_backwards_until_lcliff_senses_white()
    right_backwards_until_rcliff_senses_white()
    left_forwards_until_lcliff_senses_black()
    right_forwards_until_rcliff_senses_black()


@print_function_name_only_at_beginning
def align_far_cliffs():
    left_forwards_until_lcliff_senses_white()
    right_forwards_until_rcliff_senses_white()
    left_backwards_until_lcliff_senses_black()
    right_backwards_until_rcliff_senses_black()

#----------------------------------Single Motor Align Functions--------------

@print_function_name
def left_front_backwards_until_white(time=c.SAFETY_TIME):  # Left motor goes back until the left front cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    while isLeftFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_front_backwards_until_white(time=c.SAFETY_TIME):  # Right motor goes back until right front cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    while isRightFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def left_front_backwards_until_black(time=c.SAFETY_TIME):  # Left motor goes back until left front cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    while isLeftFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_front_backwards_until_black(time=c.SAFETY_TIME):  # Right motor goes back until right front cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    while isRightFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def left_front_forwards_until_white(time=c.SAFETY_TIME):  # Left motor goes forwards until the left front cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    while isLeftFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_front_forwards_until_white(time=c.SAFETY_TIME):  # Right motor goes forwards until right front cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    while isRightFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def left_front_forwards_until_black(time=c.SAFETY_TIME):  # Left motor goes forwards until left front cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    while isLeftFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_front_forwards_until_black(time=c.SAFETY_TIME):  # Right motor goes forwards until left front cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    while isRightFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

#----------------------------------Turning Align Functions--------------

@print_function_name
def turn_left_until_lcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_rcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_lfcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_rfcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_lcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_rcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_lfcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_left_until_rfcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_left(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnBlack():
        msleep(1)
    m.base_turn_left(multiplier)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_lcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_rcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_lfcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_rfcliff_senses_black(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_lcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_rcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_lfcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def turn_right_until_rfcliff_senses_white(time=c.SAFETY_TIME, multiplier=1):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_turn_right(multiplier)
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


#----------------------------------Driving Back Cliff Align Functions----------------------

@print_function_name
def left_backwards_until_lcliff_senses_white(time=c.SAFETY_TIME):  # Left motor goes back until the left cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    sec = seconds() + time
    while seconds() < sec and isLeftOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_backwards_until_rcliff_senses_white(time=c.SAFETY_TIME):  # Right motor goes back until right cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    sec = seconds() + time
    while seconds() < sec and isRightOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def left_backwards_until_lcliff_senses_black(time=c.SAFETY_TIME):  # Left motor goes back until left cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_backwards_until_rcliff_senses_black(time=c.SAFETY_TIME):  # Right motor goes back until left cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    sec = seconds() + time
    while seconds() < sec and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def left_forwards_until_lcliff_senses_white(time=c.SAFETY_TIME):  # Left motor goes forwards until the left cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    sec = seconds() + time
    while seconds() < sec and isLeftOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_forwards_until_rcliff_senses_white(time=c.SAFETY_TIME):  # Right motor goes forwards until right cliff senses white
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    sec = seconds() + time
    while seconds() < sec and isRightOnBlack():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def left_forwards_until_lcliff_senses_black(time=c.SAFETY_TIME):  # Left motor goes forwards until left cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    sec = seconds() + time
    while seconds() < sec and isLeftOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def right_forwards_until_rcliff_senses_black(time=c.SAFETY_TIME):  # Right motor goes forwards until left cliff senses black
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    sec = seconds() + time
    while seconds() < sec and isRightOnWhite():
        msleep(1)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

#-------------------------------------------New Stuff ---------------------------------------
# TODO organize these commands into their actual places

@print_function_name
def forwards_until_black_rfcliff_safe(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_forwards()
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnWhite():
        if isRightBumped():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_white_rfcliff_safe(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_forwards()
    sec = seconds() + time
    while seconds() < sec and isRightFrontOnBlack():
        if isRightBumped():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_black_lfcliff_safe(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    m.base_forwards()
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnWhite():
        if isRightBumped():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_until_white_lfcliff_safe(time=c.SAFETY_TIME):
    m.base_forwards()
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isLeftFrontOnBlack():
        if isRightBumped():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def lfollow_lfcliff_until_bump(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRoombaNotBumped():
        if isLeftFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()


@print_function_name
def lfollow_lfcliff_smooth_until_bump(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRoombaNotBumped():
        if isLeftFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()


@print_function_name
def lfollow_rfcliff_smooth_until_bump(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRoombaNotBumped():
        if isRightFrontOnBlack():
            m.base_veer_right()
        else:
            m.base_veer_left()


@print_function_name
def lfollow_rfcliff_until_bump(time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time
    while seconds() < sec and isRoombaNotBumped():
        if isRightFrontOnBlack():
            m.base_veer_left()
        else:
            m.base_veer_right()

#---------------------------------------------Debug-------------------------------------------

def debug_lcliff():
    if isLeftOnBlack():
        print "Left cliff sees black: " + str(get_create_lcliff_amt())
    elif isLeftOnWhite():
        print "Left cliff sees white: " + str(get_create_lcliff_amt())
    else:
        print "Error in defining isLeftOnBlack and isLeftOnWhite"
        exit(86)


def debug_lfcliff():
    if isLeftFrontOnBlack():
        print "Left front cliff sees black: " + str(get_create_lfcliff_amt())
    elif isLeftFrontOnWhite():
        print "Left front cliff sees white: " + str(get_create_lfcliff_amt())
    else:
        print "Error in defining isLeftOnBlack and isLeftOnWhite"
        exit(86)


def debug_rcliff():
    if isRightOnBlack():
        print "Right cliff sees black: " + str(get_create_rcliff_amt())
    elif isRightOnWhite():
         print "Right cliff see white: " + str(get_create_rcliff_amt())
    else:
         print "Error in defining isRightOnBlack and isRightOnWhite"
         exit(86)


def debug_rfcliff():
    if isRightFrontOnBlack():
        print "Right front cliff sees black: " + str(get_create_rfcliff_amt())
    elif isRightFrontOnWhite():
        print "Right front cliff see white: " + str(get_create_rfcliff_amt())
    else:
         print "Error in defining isRightOnBlack and isRightOnWhite"
         exit(86)


