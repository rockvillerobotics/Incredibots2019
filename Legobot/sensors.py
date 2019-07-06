from wallaby import *
from decorators import *
import constants as c
import gyro as g
import movement as m
import utils as u

# TODO pid before until
# TODO add in other PID loops

# -----------------------------HOW TO USE LFOLLOW COMMANDS------------------------
# All lfollow commands follow a certain pattern which if you learn, you can come up
# with commands without the need to look in this file. Keep in mind that these rules apply only to
# lfollow commands, but once you learn their pattern you can figure out all other patterns.
# To start off, this is the pattern:
# lfollow_[left, right, backwards]_[inside_line]_[until_black_left, until right senses black, until (event)]_[smooth]([time you want the lfollow to run in ms], [starting speed for left motor], [starting speed for right motor], [refresesh rate for the lfollow in ms])
# - To signify that you want to run an lfollow command, write lfollow.
# - Then, you must choose which sensor you want to lfollow with (left tophat, right tophat, or the third tophat respectively)
# - After this, everything is optional and is only required if you choose to put it in and the situation calls for it.
# - If you input time=0, then the command will not stop after it is finished.

# -------------------------------States------------------------

def isLeftOnBlack():
    return(analog(c.LEFT_TOPHAT) > c.LEFT_TOPHAT_BW)

def isLeftOnWhite():
    return(analog(c.LEFT_TOPHAT) < c.LEFT_TOPHAT_BW)

def isRightOnBlack():
    return(analog(c.RIGHT_TOPHAT) > c.RIGHT_TOPHAT_BW)

def isRightOnWhite():
    return(analog(c.RIGHT_TOPHAT) < c.RIGHT_TOPHAT_BW)

def isThirdOnBlack():
    return(analog(c.THIRD_TOPHAT) > c.THIRD_TOPHAT_BW)

def isThirdOnWhite():
    return(analog(c.THIRD_TOPHAT) < c.THIRD_TOPHAT_BW)

def isThirdOnMiddle():
    return(analog(c.THIRD_TOPHAT) < (c.MIN_TOPHAT_VALUE_THIRD - 10))

def isFourthOnBlack():
    return(analog(c.FOURTH_TOPHAT) > c.FOURTH_TOPHAT_BW)

def isFourthOnWhite():
    return(analog(c.FOURTH_TOPHAT) < c.FOURTH_TOPHAT_BW)

def isLeftLimitSwitchPressed():
    return(digital(c.LEFT_LIMIT_SWITCH) == 1)

def isLeftLimitSwitchNotPressed():
    return(digital(c.LEFT_LIMIT_SWITCH) == 0)

def isRightLimitSwitchPressed():
    return(digital(c.RIGHT_LIMIT_SWITCH) == 1)

def isRightLimitSwitchNotPressed():
    return(digital(c.RIGHT_LIMIT_SWITCH) == 0)

def areLimitSwitchesPressed():
    return(isLeftLimitSwitchPressed() or isRightLimitSwitchPressed())

def areLimitSwitchesNotPressed():
    return(not(isLeftLimitSwitchPressed() or isRightLimitSwitchPressed()))

# -------------------------------Wait Until Event Commands--------------------

def wait_until(boolean_function, time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        msleep(1)


def wait_until_black_left(time=c.SAFETY_TIME):
    wait_until(isLeftOnBlack, time)


def wait_until_white_left(time=c.SAFETY_TIME):
    wait_until(isLeftOnWhite, time)


def wait_until_black_right(time=c.SAFETY_TIME):
    wait_until(isRightOnBlack, time)


def wait_until_white_right(time=c.SAFETY_TIME):
    wait_until(isRightOnWhite, time)


def wait_until_black_third(time=c.SAFETY_TIME):
    wait_until(isThirdOnBlack, time)


def wait_until_white_third(time=c.SAFETY_TIME):
    wait_until(isThirdOnWhite, time)


def wait_until_limit_switch_is_pressed(time=c.SAFETY_TIME):
    wait_until(isLeftLimitSwitchPressed, time)


def wait_until_limit_switch_is_not_pressed(time=c.SAFETY_TIME):
    wait_until(isLeftLimitSwitchNotPressed, time)

def wait_until_limit_switches_are_pressed(time=c.SAFETY_TIME):
    wait_until(areLimitSwitchesPressed, time)

def wait_until_limit_switches_are_not_pressed(time=c.SAFETY_TIME):
    wait_until(areLimitSwitchesNotPressed, time)

# -------------------------------Basic Align Commands ------------------------

@print_function_name
def align_close():
    # Aligns completely on the side of the line closest to the claw
    left_backwards_until_white()
    right_backwards_until_white()
    right_forwards_until_black()
    left_forwards_until_black()
    c.ROBOT_ANGLE = 0


@print_function_name
def align_far(left_first=True):
    # Aligns completely on the side of the line closest to the camera
    if left_first == True:
        right_forwards_until_white()
        left_forwards_until_white()
        left_backwards_until_black()
        right_backwards_until_black()
    else:
        left_forwards_until_white()
        right_forwards_until_white()
        right_backwards_until_black()
        left_backwards_until_black()
    c.ROBOT_ANGLE = 0


# -------------------------------Single Motor Align Commands ------------------------

@print_function_name_with_arrows
def left_forwards_until_black(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until right tophat senses black
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_forwards_until_white(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until right tophat senses white
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_forwards_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_forwards_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_forwards_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until right tophat senses white
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_forwards_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until right tophat senses white
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_forwards_until_black(time=c.SAFETY_TIME, should_stop=True):
    # Right motor goes forwards until right tophat senses black
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_forwards_until_white(time=c.SAFETY_TIME, should_stop=True):
    # Right motor goes forwards until right tophat senses white
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_forwards_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_forwards_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_forwards_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until right tophat senses white
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_forwards_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until right tophat senses white
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_backwards_until_black(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes backwards until left tophat senses black
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_backwards_until_white(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes backwards until the left tophat senses white
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_backwards_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes backwards until right tophat senses black
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_backwards_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes backwards until the right tophat senses white
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_backwards_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes backwards until third tophat senses black
    m.av(c.LEFT_MOTOR, -c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def left_backwards_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes backwards until third tophat senses white
    m.av(c.LEFT_MOTOR, -c.BASE_LM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_backwards_until_black(time=c.SAFETY_TIME, should_stop=True):
    # Right motor goes back until right tophat senses black
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_backwards_until_white(time=c.SAFETY_TIME, should_stop=True):
    # Right motor goes back until right tophat senses white
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_backwards_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Right motor goes back until left tophat senses black
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_backwards_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Right motor goes back until left tophat senses white
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_backwards_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until third tophat senses white
    m.av(c.RIGHT_MOTOR, -c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def right_backwards_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Left motor goes forwards until third tophat senses white
    m.av(c.RIGHT_MOTOR, -c.BASE_RM_POWER)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


# -------------------------------Point Turn Align Commands ------------------------

@print_function_name_with_arrows
def turn_left_until_black(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_left()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_white(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_left()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_left()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_left()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_left()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_left()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_black(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_right()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_white(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_right()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_right()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_right()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_right()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    m.base_turn_right()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


# -------------------------------Driving Align Commands ------------------------

@print_function_name
def snap_to_line_left(turn_time=c.SAFETY_TIME):
    drive_through_line_third()
    turn_left_until_black(turn_time)


@print_function_name
def snap_to_line_right(turn_time=c.SAFETY_TIME):
    drive_through_line_third()
    turn_right_until_black(turn_time)


@print_function_name_with_arrows
def drive_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    m.base_drive()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until(boolean_function, time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    drive_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def drive_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    drive_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def drive_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    drive_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def drive_until_black(time=c.SAFETY_TIME, should_stop=True):
    m.base_drive()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnWhite() and isRightOnWhite():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_both_black(time=c.SAFETY_TIME, should_stop=True):
    m.base_drive()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and (isLeftOnWhite() or isRightOnWhite()):
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    drive_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def drive_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    drive_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def drive_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    drive_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def drive_until_white(time=c.SAFETY_TIME, should_stop=True):
    m.base_drive()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnBlack() and isRightOnBlack():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_both_white(time=c.SAFETY_TIME, should_stop=True):
    m.base_drive()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and (isLeftOnBlack() or isRightOnBlack()):
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name
def drive_through_line_left(time=c.SAFETY_TIME, should_stop=True):
    drive_until_black_left(should_stop=False)
    drive_until_white_left(time, should_stop)


@print_function_name
def drive_through_line_right(time=c.SAFETY_TIME, should_stop=True):
    drive_until_black_right(should_stop=False)
    drive_until_white_right(time, should_stop)


@print_function_name
def drive_through_line_third(time=c.SAFETY_TIME, should_stop=True):
    drive_until_black_third(should_stop=False)
    drive_until_white_third(time, should_stop)


@print_function_name
def drive_through_two_lines_third(time=c.SAFETY_TIME, should_stop=True):  # Drives without stopping the motors in between
    drive_until_black_third(should_stop=False)
    drive_until_white_third(should_stop=False)
    drive_until_black_third(should_stop=False)
    drive_until_white_third(time, should_stop)


@print_function_name_with_arrows
def backwards_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    m.base_backwards()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until(boolean_function, time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    backwards_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def backwards_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    backwards_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def backwards_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    backwards_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def backwards_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    backwards_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def backwards_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    backwards_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def backwards_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    backwards_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def backwards_until_white(time=c.SAFETY_TIME, should_stop=True):
    m.base_backwards()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnBlack() and isLeftOnBlack():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_both_white(time=c.SAFETY_TIME, should_stop=True):
    m.base_backwards()
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnBlack() or isLeftOnBlack():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name
def backwards_through_line_left(time=c.SAFETY_TIME, should_stop=True):
    backwards_until_black_left(should_stop=False)
    backwards_until_white_left(time, should_stop)


@print_function_name
def backwards_through_line_third(time=c.SAFETY_TIME, should_stop=True):
    backwards_until_black_third(should_stop=False)
    backwards_until_white_third(time, should_stop)


@print_function_name
def backwards_through_line_right(time=c.SAFETY_TIME, should_stop=True):
    backwards_until_black_right(should_stop=False)
    backwards_until_white_right(time, should_stop)

#-------------------------- Base Line Follow Commands -----------------------

def base_lfollow_left():
    if isLeftOnBlack():
        mav(c.RIGHT_MOTOR, 0)
        m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    elif isLeftOnWhite():
        mav(c.LEFT_MOTOR, 0)
        m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_left_inside_line():
    if isLeftOnBlack():
        mav(c.LEFT_MOTOR, 0)
        m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    elif isLeftOnWhite():
        mav(c.RIGHT_MOTOR, 0)
        m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_right():
    if isRightOnBlack():
        mav(c.LEFT_MOTOR, 0)
        m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    elif isRightOnWhite():
        mav(c.RIGHT_MOTOR, 0)
        m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_right_inside_line():
    if isRightOnBlack():
        mav(c.RIGHT_MOTOR, 0)
        m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    elif isRightOnWhite():
        mav(c.LEFT_MOTOR, 0)
        m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_backwards_bot_right():
    if isThirdOnBlack():
        mav(c.LEFT_MOTOR, 0)
        m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    elif isThirdOnWhite():
        mav(c.RIGHT_MOTOR, 0)
        m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_backwards_bot_left():
    if isThirdOnWhite():
        mav(c.LEFT_MOTOR, 0)
        m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    elif isThirdOnBlack():
        mav(c.RIGHT_MOTOR, 0)
        m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_left_smooth():
    if isLeftOnBlack():
        m.activate_motors(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
    else:
        m.activate_motors(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_left_inside_line_smooth():
    if isLeftOnBlack():
        m.activate_motors(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)
    else:
        m.activate_motors(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_right_smooth():
    if isRightOnBlack():
        m.activate_motors(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)
    elif isRightOnWhite():
        m.activate_motors(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_right_inside_line_smooth():
    if isRightOnBlack():
        m.activate_motors(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
    elif isRightOnWhite():
        m.activate_motors(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_backwards_smooth_bot_right():
    # This is the right side of the line from the bot's point of view.
    if isThirdOnBlack():
        m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.LFOLLOW_SMOOTH_RM_POWER)
    elif isThirdOnWhite():
        m.activate_motors(-1 * c.LFOLLOW_SMOOTH_LM_POWER, -1 * c.BASE_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)


def base_lfollow_backwards_smooth_bot_left():
    # This is the left side of the line from the bot's point of view.
    if isThirdOnBlack():
        m.activate_motors(-1 *  c.LFOLLOW_SMOOTH_LM_POWER, -1 * c.BASE_RM_POWER)
    elif isThirdOnWhite():
        m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.LFOLLOW_SMOOTH_RM_POWER)
    msleep(c.LFOLLOW_REFRESH_RATE)

# ------------------------------- Line Follow Commands ------------------------

@print_function_name_with_arrows
def lfollow_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_left()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_left_inside_line()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_right()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_right_inside_line()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_bot_left()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_right(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat inside the line until the right tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_bot_right()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_both(time=c.SAFETY_TIME, should_stop=True):
    # Line follow using both tophats until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if isRightOnBlack() and isLeftOnBlack():
            m.drive_no_print(30)
        elif isRightOnBlack() and isLeftOnWhite():
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        elif isRightOnWhite() and isLeftOnBlack():
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(c.LFOLLOW_REFRESH_RATE)
    if should_stop:
        m.deactivate_motors()

# ------------------------------- Line Follow Until Event Commands ------------------------

@print_function_name_with_arrows
def lfollow_left_until(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_left()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until right tophat senses black or time is reached.
    lfollow_left_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until third tophat senses black or time is reached.
    lfollow_left_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until right tophat senses white or time is reached.
    lfollow_left_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until third tophat senses white or time is reached.
    lfollow_left_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until time is reached or the provided condition is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_left_inside_line()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses black or time is reached.
    lfollow_left_inside_line_until(isRightOnBlack)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses black or time is reached.
    lfollow_left_inside_line_until(isThirdOnBlack)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses white or time is reached.
    lfollow_left_inside_line_until(isRightOnWhite)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses white or time is reached.
    lfollow_left_inside_line_until(isThirdOnWhite)


@print_function_name_with_arrows
def lfollow_right_until(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until left tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_right()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until left tophat senses black or time is reached.
    lfollow_right_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until left tophat senses black or time is reached.
    lfollow_right_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until left tophat senses white or time is reached.
    lfollow_right_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until third tophat senses white or time is reached.
    lfollow_right_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until the left tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_right_inside_line()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until the left tophat senses black or time is reached.
    lfollow_right_inside_line_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until the third tophat senses black or time is reached.
    lfollow_right_inside_line_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until the left tophat senses white or time is reached.
    lfollow_right_inside_line_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until the third tophat senses white or time is reached.
    lfollow_right_inside_line_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_backwards_bot_left()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the left tophat senses black.
    lfollow_backwards_bot_left_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the right tophat senses black.
    lfollow_backwards_bot_left_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the left tophat senses white.
    lfollow_backwards_bot_left_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the right tophat senses white.
    lfollow_backwards_bot_left_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until(condition, time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat inside the line until the right tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_backwards_bot_right()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the left tophat senses black.
    lfollow_backwards_bot_right_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the right tophat senses black.
    lfollow_backwards_bot_right_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the left tophat senses white.
    lfollow_backwards_bot_right_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached or the right tophat senses white.
    lfollow_backwards_bot_right_until(isRightOnWhite, time, should_stop)

#----------------- Smooth Line Follow Commands -----------------------------------------------

@print_function_name_with_arrows
def lfollow_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_left_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat inside the line until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_left_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_right_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat inside the line until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_right_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards smoothly with the third tophat until time is reached.
    # It goes to the left side of the line from the bot's point of view.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_smooth_bot_left()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards smoothly with the third tophat inside the line until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_smooth_bot_right()
    if should_stop:
        m.deactivate_motors()

#----------------- Smooth Line Follow Until Event Commands -----------------------------------------------

@print_function_name_with_arrows
def lfollow_left_smooth_until(condition, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_left_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_until_black_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_until_black_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_smooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_until_white_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_smooth_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_until_white_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_smooth_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_smooth_until(condition, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_left_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_smooth_until(condition, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_right_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_until_black_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_smooth_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_until_black_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_right_smooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_until_white_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_smooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_until_white_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_right_smooth_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_smooth_until(condition, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_right_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_until_black_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_inside_line_smooth_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until_black_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_right_inside_line_smooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until_white_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_inside_line_smooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_until_white_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_right_inside_line_smooth_until(isThirdOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_smooth_until(condition, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_backwards_bot_left_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_black_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_left_smooth_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_black_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_left_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_white_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_left_smooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until_white_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_left_smooth_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth_until(condition, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(condition()):
        base_lfollow_backwards_bot_right_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_black_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_right_smooth_until(isLeftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_black_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_right_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_white_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_right_smooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until_white_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_right_smooth_until(isRightOnWhite, time, should_stop)

#----------------- PID Line Follow Commands --------------------------------------------------
# Line follow commans that use a proportional, integral, derivative control algorithim. Basically, the farther away
# from the line the faster the robot turns to get back onto the line.

@print_function_name_with_arrows
def lfollow_left_pid(time, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 15
            ki = c.KI
            kd = c.KD
        elif error < 10 and error > -10:
            kp = 2 * 1.2
            ki = c.KI / 10
            kd = c.KD / 10
        else:
            kp = 4 * 1.2
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
        msleep(10)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_value_testing_pid(time, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    kp = c.KP
    ki = c.KI
    kd = c.KD
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
        if u.isRightPressed():
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_RIGHT: " + str(c.MAX_TOPHAT_VALUE_RIGHT)
            print "c.MIN_TOPHAT_VALUE_RIGHT: " + str(c.MIN_TOPHAT_VALUE_RIGHT)
            msleep(30)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_pid(time, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 20 or error < -20:
            kp = 20
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = 5
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_pid(time, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 20 or error < -20:
            kp = 20
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = 5
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()





@print_function_name_with_arrows
def lfollow_right_pid_value_testing(time, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    kp = c.KP
    ki = c.KI
    kd = c.KD
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
        if u.isRightPressed():
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_RIGHT: " + str(c.MAX_TOPHAT_VALUE_RIGHT)
            print "c.MIN_TOPHAT_VALUE_RIGHT: " + str(c.MIN_TOPHAT_VALUE_RIGHT)
            msleep(30)
    if should_stop:
        m.deactivate_motors()


#----------------- PID Line Follow Until Event Commands --------------------------------------------------

@print_function_name_with_arrows
def lfollow_left_pid_until(boolean_function, time=c.SAFETY_TIME, should_stop=True, bias=0, should_open_and_close_micro=True):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    ms = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 15
            ki = c.KI / 1.1
            kd = c.KD / 1.1
        elif error < 10 and error > -10:
            kp = 2 * 1.2
            ki = c.KI / 10
            kd = c.KD / 10
        else:
            kp = 4 * 1.2
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
        if should_open_and_close_micro:
            m.wipe_with_micro(50)
        msleep(10)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_pid_until_black_right(time=c.SAFETY_TIME, should_open_and_close_micro=False, should_stop=True, bias=0):
    lfollow_left_pid_until(isRightOnBlack, time, should_stop, bias, should_open_and_close_micro)


@print_function_name_with_arrows
def lfollow_left_pid_until_black_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(boolean_functino=isThirdOnBlack, time=time, should_stop=should_stop, bias=bias)


@print_function_name_with_arrows
def lfollow_left_pid_until_white_right(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isRightOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isThirdOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_pid_until_third_senses_middle(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isThirdOnMiddle, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_pid_until(boolean_function, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 20 or error < -20:
            kp = 20
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = 5
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_right_pid(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isRightOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_third_pid(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_right_pid(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isRightOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_third_pid(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isThirdOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until(boolean_function, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 20 or error < -20:
            kp = 20
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = 5
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_pid_until_black_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_until(isLeftOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until_black_thirs(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_until(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until_white_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_until(isLeftOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_until(isThirdOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid(time, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 20 or error < -20:
            kp = 20
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = 5
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until(boolean_function, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 20 or error < -20:
            kp = 20
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = 5
            ki = c.KI / 2
            kd = c.KD / 2
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_black_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_until(isLeftOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_black_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_until(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_white_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_until(isLeftOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_until(isThirdOnWhite, time, should_stop, bias)

# -------------------------------Debug------------------------

def debug_right_tophat():
    if isRightOnBlack():
        print "Right tophat senses black: " + str(analog(c.RIGHT_TOPHAT))
    elif isRightOnWhite():
        print "Right tophat see white: " + str(analog(c.RIGHT_TOPHAT))
    else:
        print "Error in defining isRightOnBlack and isRightOnWhite"
        u.sd()


def debug_left_tophat():
    if isLeftOnBlack():
        print "Left tophat senses black: " + str(analog(c.LEFT_TOPHAT))
    elif isLeftOnWhite():
        print "Left tophat senses white: " + str(analog(c.LEFT_TOPHAT))
    else:
        print "Error in defining isLeftOnBlack and isLeftOnWhite"
        u.sd()
