from wallaby import *
from decorators import *
import constants as c
import gyro as g
import movement as m
import utils as u

# -----------------------------HOW TO USE LFOLLOW COMMANDS------------------------
# All lfollow commands follow a certain pattern which if you learn, you can come up
# with commands without the need to look in this file.
# To start off, this is the pattern:
# lfollow_[sensor]_[inside_line, smooth, pid]_until_[color]_[sensor]()
# - the sensors are: left, right, third, and fourth. The left and right sensors are on the front on our bot.
#   The third sensor is on the back and the fourth sensor is extra; it's spot changes depending on where we want it.
# -

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

def isFourthOnBlack():
    return(analog(c.FOURTH_TOPHAT) > c.FOURTH_TOPHAT_BW)

def isFourthOnWhite():
    return(analog(c.FOURTH_TOPHAT) < c.FOURTH_TOPHAT_BW)

# -------------------------------Wait Until Event Commands--------------------
# These commands wait until a condition is met.

def wait_until(boolean_function, time=c.SAFETY_TIME):
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):  # The loop doesn't break until the condition is met.
        msleep(1)


def wait_until_black_left(time=c.SAFETY_TIME):
    wait_until(isLeftOnBlack, time)


def wait_until_white_left(time=c.SAFETY_TIME):
    wait_until(isLeftOnWhite, time)


def wait_until_black_right(time=c.SAFETY_TIME):
    wait_until(isRightOnBlac, time)


def wait_until_white_right(time=c.SAFETY_TIME):
    wait_until(isRightOnWhite, time)


def wait_until_black_third(time=c.SAFETY_TIME):
    wait_until(isThirdOnBlack, time)


def wait_until_white_third(time=c.SAFETY_TIME):
    wait_until(isThirdOnWhite, time)

# ------------------------- Basic Align Commands ------------------------

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


# ------------------- Single Motor Align Commands -------------------------------

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


# ------------------------------- Point Turn Align Commands ------------------------

@print_function_name_with_arrows
def turn_left_until_black(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_left(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_white(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_left(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_black_right(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_left(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_white_right(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_left(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_black_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_left(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_left_until_white_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_left(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_black(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_right(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_white(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_right(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_black_left(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_right(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_white_left(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_right(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_black_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_right(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def turn_right_until_white_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_turn_right(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


# ------------------------------- Drive Until Tophats Commands ------------------------

@print_function_name
def snap_to_line_left(turn_time=c.SAFETY_TIME, should_stop=True):
    drive_through_line_third()
    turn_left_until_black(turn_time)


@print_function_name
def snap_to_line_right(turn_time=c.SAFETY_TIME, should_stop=True):
    drive_through_line_third()
    turn_right_until_black(turn_time)


@print_function_name_with_arrows
def drive_until_black_left(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_black_right(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_black_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_black(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnWhite() and isRightOnWhite():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_both_black(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and (isLeftOnWhite() or isRightOnWhite()):
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_white_left(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_white_right(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_white_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_white(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isLeftOnBlack() and isRightOnBlack():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_until_both_white(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_drive(speed_multiplier)
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
def backwards_until_black_left(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_black_right(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_black_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_black_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_white_left(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_left(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_white_right(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_right(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_white_third(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    wait_until_white_third(time)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_white(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and isRightOnBlack() and isLeftOnBlack():
        msleep(1)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_until_both_white(time=c.SAFETY_TIME, should_stop=True, speed_multiplier=1):
    m.base_backwards(speed_multiplier)
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
def lfollow_left_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
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
def lfollow_left_inside_line_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until time is reached or the provided boolean_function is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_left_inside_line()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses black or time is reached.
    lfollow_left_inside_line_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses black or time is reached.
    lfollow_left_inside_line_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses white or time is reached.
    lfollow_left_inside_line_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the left tophat inside the line until the right tophat senses white or time is reached.
    lfollow_left_inside_line_until(isThirdOnWhite, time, should_stop)


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
def lfollow_right_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat until left tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
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
def lfollow_right_inside_line_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    # Line follow with the right tophat inside the line until the left tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
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
def lfollow_backwards_bot_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_bot_right()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_left_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_backwards_bot_right()
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
def lfollow_backwards_bot_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat on the right side of the line until time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_bot_right()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_right_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    # Line follow backwards with the third tophat inside the line until the right tophat senses black or time is reached.
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
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
def lfollow_left_smooth_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_left_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_smooth_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_smooth_until_black_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_smooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_smooth_until_white_right_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_smooth_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_smooth_until_white_third_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_smooth_until(isThirdOnWhite, time, should_stop)


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
def lfollow_left_inside_line_smooth_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_left_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_smooth_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_smooth_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_smooth_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isRightOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_left_inside_line_smooth_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    lfollow_left_inside_line_smooth_until(isThirdOnWhite, time, should_stop)

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
def lfollow_right_smooth_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_right_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_until_black_left_smooth(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_smooth_until(isleftOnBlack, time, should_stop)


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
def lfollow_right_inside_line_smooth_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_right_inside_linesmooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_smooth_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_inside_linesmooth_until(isleftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_smooth_until_black_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_right_inside_linesmooth_until(isThirdOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_smooth_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_right_inside_linesmooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_right_inside_line_smooth_until_white_third(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_right_inside_linesmooth_until(isThirdOnWhite, time, should_stop)


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
def lfollow_backwards_bot_left_smooth_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_backwards_bot_left_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_left_smooth_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_left_inside_line_smooth_until(isleftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_smooth_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_left_inside_line_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_smooth_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_left_inside_line_smooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_left_smooth_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_left_inside_line_smooth_until(isRightOnWhite, time, should_stop)


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


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth_until(boolean_function, time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        base_lfollow_backwards_bot_right_inside_line_smooth()
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_right_inside_line_smooth_until(isleftOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_right_inside_line_smooth_until(isRightOnBlack, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until right tophat senses black or time is reached.
    lfollow_backwards_bot_right_inside_line_smooth_until(isLeftOnWhite, time, should_stop)


@print_function_name_with_arrows
def lfollow_backwards_bot_right_smooth_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    # Line follow smoothly with the right tophat until third tophat senses black or time is reached.
    lfollow_backwards_bot_right_inside_line_smooth_until(isRightOnWhite, time, should_stop)

#----------------- PID Line Follow Commands --------------------------------------------------
# Line follow commands that use a proportional, integral, derivative control algorithim. Basically, the farther away
# from the line the faster the robot turns to get back onto the line.

@print_function_name_with_arrows
def lfollow_left_pid(time, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias  # Desired bw value put on a scale between 0 and 100.
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
        # This changes the aggressiveness of robot dynamically based off of how far off the line it is.
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_pid_value_testing(time, should_stop=True, bias=0):
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
def lfollow_left_pid_until(boolean, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_pid_until_black_right(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isRightOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_pid_until_black_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_pid_until_white_right(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isRightOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_pid_until(isThirdOnWhite, time, should_stop, bias)


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
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_pid_until(boolean, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_left_inside_line_pid_until_black_right(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isRightOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_pid_until_black_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_pid_until_white_right(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isRightOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_left_inside_line_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_left_inside_line_pid_until(isThirdOnWhite, time, should_stop, bias)


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
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
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


@print_function_name_with_arrows
def lfollow_right_pid_until(boolean, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_pid_until_black_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_while(isLeftOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until_black_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_while(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until_white_lefttime=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_while(isLeftOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_pid_while(isThirdOnWhite, time, should_stop, bias)


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
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until(boolean, time=c.SAFETY_TIME, should_stop=True, bias=0):
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT) + bias
    last_error = 0
    integral = 0
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 7
            ki = c.KI
            kd = c.KD
        elif error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
        else:
            kp = c.KP
            ki = c.KI
            kd = c.KD
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        m.activate_motors(left_power, right_power)
    if should_stop:
        m.deactivate_motors()


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_black_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_while(isLeftOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_black_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_while(isThirdOnBlack, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_white_left(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_while(isLeftOnWhite, time, should_stop, bias)


@print_function_name_with_arrows
def lfollow_right_inside_line_pid_until_white_third(time=c.SAFETY_TIME, should_stop=True, bias=0):
    lfollow_right_inside_line_pid_while(isThirdOnWhite, time, should_stop, bias)

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