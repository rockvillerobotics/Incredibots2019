from wallaby import *
import constants as c
import movement as m
import utils as u


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HOW TO USE LFOLLOW COMMANDS~~~~~~~~~~~~~~~~~~~~~~~~
# All lfollow commands follow a certain pattern which if you learn, you can come up
# with commands without the need to look in this file. Keep in mind that these rules apply only to
# lfollow commands, but once you learn their pattern you can figure out all other patterns.
# To start off, this is the pattern:
# lfollow_[left, right, backwards]_[inside_line]_[until_left_senses_black, until right senses black, until (event)]_[smooth]([time you want the lfollow to run in ms], [starting speed for left motor], [starting speed for right motor], [refresesh rate for the lfollow in ms])
# - To signify that you want to run an lfollow command, write lfollow.
# - Then, you must choose which sensor you want to lfollow with (left tophat, right tophat, or the third tophat respectively)
# - After this, everything is optional and is only required if you choose to put it in and the situation calls for it.
# - If you input time=0, then the command will not stop after it is finished.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~States~~~~~~~~~~~~~~~~~~~~~~~~

def BlackLeft():
    return (analog(c.LEFT_TOPHAT) > c.LEFT_TOPHAT_BW)

def NotBlackLeft():
    return (analog(c.LEFT_TOPHAT) < c.LEFT_TOPHAT_BW)

def BlackRight():
    return (analog(c.RIGHT_TOPHAT) > c.RIGHT_TOPHAT_BW)

def NotBlackRight():
    return (analog(c.RIGHT_TOPHAT) < c.RIGHT_TOPHAT_BW)

def BlackThird():
    return (analog(c.THIRD_TOPHAT) > c.THIRD_TOPHAT_BW)

def NotBlackThird():
    return (analog(c.THIRD_TOPHAT) < c.THIRD_TOPHAT_BW)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Basic Align Functions~~~~~~~~~~~~~~~~~~~~~~~~

def align_close():
    # Aligns completely on the side of the line closest to the claw
    print "Starting align_close()"
    left_backwards_until_white()
    right_backwards_until_white()
    right_forwards_until_black()
    left_forwards_until_black()
    print "Aligned to close side of line\n"


def align_close_smart():
    # Aligns completely on the side of the line closest to the claw
    print "Starting align_close_smart()"
    starting_left_time = seconds()
    if BlackLeft():
        left_backwards_until_white()
    else:
        left_forwards_until_black()
    total_left_time = seconds() - starting_left_time
    starting_right_time = seconds()
    if BlackRight():
        right_backwards_until_white()
    else:
        right_forwards_until_black()
    total_right_time = seconds() - starting_right_time
    print "Second motor run time: " + str(total_right_time)
    if total_right_time > .3:
        print "Another align is probably necessary here.\n"
        if BlackLeft():
            left_backwards_until_white()
        else:
            left_forwards_until_black()
    print "Aligned to close side of line\n"


def align_far(left_first=True):
    # Aligns completely on the side of the line closest to the camera
    print "Starting align_far()"
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
    print "Aligned to far side of line\n"


def align_far_smart():
    # Aligns completely on the side of the line closest to the camera
    print "Starting align_far_smart()"
    if BlackLeft() and BlackRight():
        drive_until_both_white()
    starting_left_time = seconds()
    if BlackLeft():
        left_forwards_until_white()
    else:
        left_backwards_until_black()
    total_left_time = seconds() - starting_left_time
    starting_right_time = seconds()
    if BlackRight():
        right_forwards_until_white()
    else:
        right_backwards_until_black()
    total_right_time = seconds() - starting_right_time
    print "Time difference: " + str(abs(total_left_time - total_right_time))
    if abs(total_left_time - total_right_time) > .5:
        print "Woah there! We probably need to do another align here./n"
        if total_left_time > total_right_time:
            if BlackRight():
                right_forwards_until_white()
            else:
                right_backwards_until_black()
        else:
            if BlackLeft():
                left_forwards_until_white()
            else:
                left_backwards_until_black()
    print "Aligned to far side of line\n"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Single Motor Align Functions~~~~~~~~~~~~~~~~~~~~~~~~

def left_forwards_until_black(time=c.SAFETY_TIME):
    # Left motor goes forwards until right tophat senses black
    print "Starting left_forwards_until_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_forwards_until_white(time=c.SAFETY_TIME):
    # Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_forwards_until_right_senses_black(time=c.SAFETY_TIME):
    print "Starting left_forwards_until_right_senses_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_forwards_until_right_senses_white(time=c.SAFETY_TIME):
    print "Starting left_forwards_until_right_senses_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

def left_forwards_until_third_senses_black(time=c.SAFETY_TIME):
    # Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_forwards_until_third_senses_white(time=c.SAFETY_TIME):
    # Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_forwards_until_black(time=c.SAFETY_TIME):
    # Right motor goes forwards until right tophat senses black
    print "Starting right_forwards_until_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_forwards_until_white(time=c.SAFETY_TIME):
    # Right motor goes forwards until right tophat senses white
    print "Starting right_forwards_until_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_forwards_until_left_senses_black(time=c.SAFETY_TIME):
    print "Starting right_forwards_until_left_senses_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_forwards_until_left_senses_white(time=c.SAFETY_TIME):
    print "Starting right_forwards_until_left_senses_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_forwards_until_third_senses_black(time=c.SAFETY_TIME):
    # Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_forwards_until_third_senses_white(time=c.SAFETY_TIME):
    # Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_backwards_until_black(time=c.SAFETY_TIME):
    # Left motor goes backwards until left tophat senses black
    print "Starting left_backwards_until_black()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_backwards_until_white(time=c.SAFETY_TIME):
    # Left motor goes backwards until the left tophat senses white
    print "Starting left_backwards_until_white()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_backwards_until_right_senses_black(time=c.SAFETY_TIME):
    # Left motor goes backwards until right tophat senses black
    print "Starting left_backwards_until_right_senses_black()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_backwards_until_right_senses_white(time=c.SAFETY_TIME):
    # Left motor goes backwards until the right tophat senses white
    print "Starting left_backwards_until_right_senses_white()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_backwards_until_third_senses_black(time=c.SAFETY_TIME):
    # Left motor goes backwards until third tophat senses white
    print "Starting left_backwards_until_third_senses_black()"
    m.av(c.LEFT_MOTOR, -c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def left_backwards_until_third_senses_white(time=c.SAFETY_TIME):
    # Left motor goes backwards until third tophat senses white
    print "Starting left_backwards_until_third_senses_white()"
    m.av(c.LEFT_MOTOR, -c.BASE_LM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_backwards_until_black(time=c.SAFETY_TIME):
    # Right motor goes back until right tophat senses black
    print "Starting right_backwards_until_black()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_backwards_until_white(time=c.SAFETY_TIME):
    # Right motor goes back until right tophat senses white
    print "Starting right_backwards_until_white()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_backwards_until_left_senses_black(time=c.SAFETY_TIME):
    # Right motor goes back until left tophat senses black
    print "Starting right_backwards_until_left_senses_black()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_backwards_until_left_senses_white(time=c.SAFETY_TIME):
    # Right motor goes back until left tophat senses white
    print "Starting right_backwards_until_left_senses_white()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_backwards_until_third_senses_black(time=c.SAFETY_TIME):
    # Left motor goes forwards until third tophat senses white
    print "Starting right_backwards_until_third_senses_black()"
    m.av(c.RIGHT_MOTOR, -c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def right_backwards_until_third_senses_white(time=c.SAFETY_TIME):
    # Left motor goes forwards until third tophat senses white
    print "Starting right_backwards_until_third_senses_white()"
    m.av(c.RIGHT_MOTOR, -c.BASE_RM_POWER)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Point Turn Align Functions~~~~~~~~~~~~~~~~~~~~~~~~

def turn_left_until_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_left_until_black()"
    m.base_turn_left(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_left_until_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_left_until_white()"
    m.base_turn_left(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_left_until_right_senses_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_left_until_right_senses_black()"
    m.base_turn_left(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_left_until_right_senses_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_left_until_right_senses_white()"
    m.base_turn_left(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_left_until_third_senses_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_left_until_third_senses_black()"
    m.base_turn_left(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_left_until_third_senses_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_left_until_third_senses_white()"
    m.base_turn_left(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_right_until_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_right_until_black()"
    m.base_turn_right(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_right_until_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_right_until_white()"
    m.base_turn_right(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_right_until_left_senses_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_right_until_left_senses_black()"
    m.base_turn_right(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_right_until_left_senses_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_right_until_left_senses_white()"
    m.base_turn_right(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_right_until_third_senses_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_right_until_third_senses_black()"
    m.base_turn_right(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def turn_right_until_third_senses_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting turn_right_until_third_senses_white()"
    m.base_turn_right(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Driving Align Functions~~~~~~~~~~~~~~~~~~~~~~~~

def snap_to_line_left(turn_time=c.SAFETY_TIME):
    drive_through_line_third()
    turn_left_until_black(turn_time)


def snap_to_line_right(turn_time=c.SAFETY_TIME):
    drive_through_line_third()
    turn_right_until_black(turn_time)


def drive_until_black_left(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_black_left()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def drive_until_black_right(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_black_right()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def drive_until_black_third(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_black_third()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def drive_until_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_black()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft() and NotBlackRight():
        pass
    if BlackLeft():
        sensor_on_black = c.LEFT_TOPHAT
    else:
        sensor_on_black = c.RIGHT_TOPHAT
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def drive_until_both_black(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_both_black()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft() or NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def drive_until_white_left(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_white_left()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def drive_until_white_right(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_white_right()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def drive_until_white_third(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_white_third()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def drive_until_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_white()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft() and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def drive_until_both_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting drive_until_both_white()"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft() or BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def drive_through_line_left(time=c.SAFETY_TIME):
    print "Starting drive_through_line_left()"
    drive_until_black_left(0)
    drive_until_white_left(time)


def drive_through_line_right(time=c.SAFETY_TIME):
    print "Starting drive_through_line_right()"
    drive_until_black_right(0)
    drive_until_white_right(time)


def drive_through_line_third(time=c.SAFETY_TIME):
    print "Starting drive_through_line_third()"
    drive_until_black_third(0)
    drive_until_white_third(time)


def drive_through_two_lines_third(time=c.SAFETY_TIME):  # Drives without stopping the motors in between
    print "Starting drive_through_two_lines_third()"
    drive_until_black_third(0)
    drive_until_white_third(0)
    drive_until_black_third(0)
    drive_until_white_third(time)


def backwards_until_black_left(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_black_left()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def backwards_until_black_right(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_black_right()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "Line sensed\n"


def backwards_until_black_third(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_black_third()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    print "Line sensed\n"
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def backwards_until_white_left(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_white_left()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def backwards_until_white_right(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_white_right()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def backwards_until_white_third(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_white_third()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    print "Line sensed\n"
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def backwards_until_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_white()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight() and BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def backwards_until_both_white(time=c.SAFETY_TIME, speed_multiplier=1):
    print "Starting backwards_until_both_white()"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight() or BlackLeft():
        pass
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    print "White sensed\n"


def backwards_through_line_left(time=c.SAFETY_TIME):
    backwards_until_black_left(0)
    backwards_until_white_left(time)
        
        
def backwards_through_line_third(time=c.SAFETY_TIME):
    backwards_until_black_third(0)
    backwards_until_white_third(time)
        
        
def backwards_through_line_right(time=c.SAFETY_TIME):
    backwards_until_black_right(0)
    backwards_until_white_right(time)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Line Follow Functions~~~~~~~~~~~~~~~~~~~~~~~~

def lfollow_left(time=c.SAFETY_TIME):
    # Line follow with the left tophat until time is reached.
    print "Starting lfollow_left()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != 0:
        m.deactivate_both_motors()


def base_lfollow_left_smooth():
    if BlackLeft():
        mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
        mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
    else:
        mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
        mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)


def base_lfollow_left_inside_line_smooth():
    if BlackLeft():
        mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
        mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    else:
        mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
        mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)


def lfollow_left_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the left tophat for time.
    print "Starting lfollow_left_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_left_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_smooth_amount(time, left_speed=c.BASE_LM_POWER, right_speed=c.BASE_RM_POWER,
                               left_smooth_speed=c.LFOLLOW_SMOOTH_LM_POWER,
                               right_smooth_speed=c.LFOLLOW_SMOOTH_RM_POWER):
    # TO DO
    print "Starting lfollow_left_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackLeft():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        else:
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black(time=c.SAFETY_TIME):
    # Line follow with the left tophat until right tophat senses black or time is reached.
    print "Starting lfollow_left_until_right_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
            
def lfollow_left_until_third_senses_black(time=c.SAFETY_TIME):
    # Line follow with the left tophat until third tophat senses black or time is reached.
    print "Starting lfollow_left_until_third_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    print "Starting lfollow_left_until_right_senses_black_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        base_lfollow_left_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
            
def lfollow_left_until_third_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the left tophat until third tophat senses black or time is reached.
    print "Starting lfollow_left_until_third_senses_black_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        base_lfollow_left_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_inside_line(time=c.SAFETY_TIME):
    # Line follow with the left tophat inside the line until time is reached.
    print "Starting lfollow_left_inside_line()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_inside_line_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the left tophat inside the line until time is reached.
    print "Starting lfollow_left_inside_line_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_left_inside_line_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_inside_line_until_right_senses_black(time=c.SAFETY_TIME):
    # Line follow with the left tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_left_inside_line_until_right_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_inside_line_until_right_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the left tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_left_inside_line_until_right_senses_black_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        base_lfollow_left_inside_line_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != 0:
        m.deactivate_both_motors()


def lfollow_left_inside_line_until_right_senses_black_smooth_amount(time=c.SAFETY_TIME, left_speed=c.BASE_LM_POWER,
                                                                    right_speed=c.BASE_RM_POWER,
                                                                    left_smooth_speed=c.LFOLLOW_SMOOTH_LM_POWER,
                                                                    right_smooth_speed=c.LFOLLOW_SMOOTH_RM_POWER):
    # IGNORE THIS, ALSO WORK ON THIS LATER
    print "Starting lfollow_left_inside_line_until_right_senses_black_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if NotBlackLeft():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        elif BlackLeft():
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_third_senses_black(time=c.SAFETY_TIME):
    # Line follow with the left tophat until the third tophat senses black or the time is reached.
    print "Starting lfollow_left_until_third_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_third_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the left tophat until the third tophat senses black or the time is reached.
    print "Starting lfollow_left_until_third_senses_black_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        base_lfollow_left_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right(time=c.SAFETY_TIME):
    # Line follow with the right tophat until time is reached.
    print "Starting lfollow_right()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def base_lfollow_right_smooth():
    if BlackRight():
        mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
        mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    elif NotBlackRight():
        mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
        mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)


def base_lfollow_right_inside_line_smooth():
    if BlackRight():
        mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
        mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
    elif NotBlackRight():
        mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
        mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)


def lfollow_right_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the right tophat until time is reached.
    print "Starting lfollow_right_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_right_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black(time=c.SAFETY_TIME):
    # Line follow with the right tophat until left tophat senses black or time is reached.
    print "Starting lfollow_right_until_left_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):  # Must begin code while touching the line
    # Line follow smoothly with the right tophat until left tophat senses black or time is reached.
    print "Starting lfollow_right_until_left_senses_black_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        base_lfollow_right_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black_smooth_amount(time, left_speed=c.BASE_LM_POWER, right_speed=c.BASE_RM_POWER,
                                                        left_smooth_speed=c.LFOLLOW_SMOOTH_LM_POWER,
                                                        right_smooth_speed=c.LFOLLOW_SMOOTH_RM_POWER):  # Must begin code while touching the line
    # IGNORE THIS, ALSO WORK ON THIS LATER
    print "Starting lfollow_right_until_left_senses_black_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if BlackRight():
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_inside_line(time=c.SAFETY_TIME):
    # Line follow with the right tophat inside the line until time is reached.
    print "Starting lfollow_right_inside_line()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_inside_line_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the right tophat inside the line until time is reached.
    print "Starting lfollow_right_inside_line_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_right_inside_line_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_inside_line_until_left_senses_black(time=c.SAFETY_TIME):
    # Line follow with the right tophat inside the line until the left tophat senses black or time is reached.
    print "Starting lfollow_right_inside_line_until_left_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_inside_line_until_left_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow smoothly with the right tophat inside the line until the left tophat senses black or time is reached.
    print "Starting lfollow_right_inside_line_until_left_senses_black_smooth()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        base_lfollow_right_inside_line_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_inside_line_until_left_senses_black_smooth_amount(time=c.SAFETY_TIME, left_speed=c.BASE_LM_POWER,
                                                                    right_speed=c.BASE_RM_POWER,
                                                                    left_smooth_speed=c.LFOLLOW_SMOOTH_LM_POWER,
                                                                    right_smooth_speed=c.LFOLLOW_SMOOTH_RM_POWER):
    # IGNORE THIS, THIS IS A WORKING COMMAND BUT IS CONVALUTED.
    print "Starting lfollow_right_inside_line_until_left_senses_black_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if BlackRight():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_until_third_senses_black(time=c.SAFETY_TIME):
    # Line follow with the right tophat until the third tophat senses black or time is reached.
    print "Starting lfollow_right_until_third_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_until_third_senses_black_smooth(time=c.SAFETY_TIME):
    # Line follow smoothly with the right tophat until the third tophat senses black or time is reached.
    print "Starting lfollow_right_until_third_senses_black_smooth()\n"
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        base_lfollow_right_smooth()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_backwards(time=c.SAFETY_TIME):
    # Line follow backwards with the third tophat until time is reached.
    print "Starting lfollow_backwards()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def base_lfollow_backwards_smooth_bot_right():
    # This is the right side of the line from the bot's point of view.
    if BlackThird():
        mav(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
        mav(c.RIGHT_MOTOR, -1 * c.LFOLLOW_SMOOTH_RM_POWER)
    elif NotBlackThird():
        mav(c.LEFT_MOTOR, -1 * c.LFOLLOW_SMOOTH_LM_POWER)
        mav(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)


def base_lfollow_backwards_smooth_bot_left():
    # This is the left side of the line from the bot's point of view.
    if BlackThird():
        mav(c.LEFT_MOTOR, -1 * c.LFOLLOW_SMOOTH_LM_POWER)
        mav(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    elif NotBlackThird():
        mav(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
        mav(c.RIGHT_MOTOR, -1 * c.LFOLLOW_SMOOTH_RM_POWER)


def lfollow_backwards_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow backwards smoothly with the third tophat until time is reached.
    # It goes to the left side of the line from the bot's point of view.
    print "Starting lfollow_backwards_smooth()\n"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_smooth_bot_left()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != 0:
        m.deactivate_both_motors()


def lfollow_backwards_until_left_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow backwards smoothly with the third tophat until the left tophat senses black.
    # It goes to the left side of the line from the bot's point of view.
    print "Starting lfollow_backwards_until_left_senses_black_smooth()\n"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        base_lfollow_backwards_smooth_bot_left()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != 0:
        m.deactivate_both_motors()


def lfollow_backwards_until_left_senses_white_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow backwards smoothly with the third tophat until the left tophat senses white.
    # It goes to the left side of the line from the bot's point of view.
    print "Starting lfollow_backwards_until_left_senses_white_smooth()\n"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        base_lfollow_backwards_smooth_bot_left()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != 0:
        m.deactivate_both_motors()


def lfollow_backwards_bot_right(time=c.SAFETY_TIME):
    # Line follow backwards with the third tophat on the right side of the line until time is reached.
    print "Starting lfollow_backwards_bot_right()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_backwards_bot_right_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow backwards smoothly with the third tophat inside the line until time is reached.
    print "Starting lfollow_backwards_bot_right_smooth()\n"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        base_lfollow_backwards_smooth_bot_right()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_backwards_bot_right_until_right_senses_black(time=c.SAFETY_TIME):
    # Line follow backwards with the third tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_backwards_bot_right_until_right_senses_black()\n"
    first_black = True
    first_white = True
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if first_black and BlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
            first_black = False
            first_white = True
        elif first_white and NotBlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
            first_black = True
            first_white = False
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_backwards_bot_right_until_right_senses_black_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow backwards smoothly with the third tophat on the right side of the line until the right tophat senses black.
    print "Starting lfollow_backwards_bot_right_until_right_senses_black_smooth()\n"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        base_lfollow_backwards_smooth_bot_right()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_backwards_bot_right_until_right_senses_white_smooth(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow backwards smoothly with the third tophat on the right side of the line until the right tophat senses white.
    print "Starting lfollow_backwards_bot_right_until_right_senses_black_smooth()\n"
    m.base_backwards(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        base_lfollow_backwards_smooth_bot_right()
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_both(time=c.SAFETY_TIME, speed_multiplier=1):
    # Line follow using both tophats until time is reached.
    print "Starting lfollow_both()\n"
    m.base_drive(speed_multiplier)
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackRight() and BlackLeft():
            m.drive_no_print(30)
        elif BlackRight() and NotBlackLeft():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
        elif NotBlackRight() and BlackLeft():
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackRight and NotBlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(c.LFOLLOW_REFRESH_RATE)
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_pid(time, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (
                c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (
                    c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_RIGHT: " + str(c.MAX_TOPHAT_VALUE_RIGHT)
            print "c.MIN_TOPHAT_VALUE_RIGHT: " + str(c.MIN_TOPHAT_VALUE_RIGHT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_pid_value_testing(time, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (
                c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_VALUE_RIGHT) / (c.MAX_VALUE_RIGHT - c.MIN_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_RIGHT: " + str(c.MAX_TOPHAT_VALUE_RIGHT)
            print "c.MIN_TOPHAT_VALUE_RIGHT: " + str(c.MIN_TOPHAT_VALUE_RIGHT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        if u.right_pressed():
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
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black_pid(time=c.SAFETY_TIME, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (
                c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_VALUE_RIGHT) / (c.MAX_VALUE_RIGHT - c.MIN_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_RIGHT: " + str(c.MAX_TOPHAT_VALUE_RIGHT)
            print "c.MIN_TOPHAT_VALUE_RIGHT: " + str(c.MIN_TOPHAT_VALUE_RIGHT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_right_inside_line_pid(time, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.RIGHT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_RIGHT) / (
                c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.RIGHT_TOPHAT) - c.MIN_TOPHAT_VALUE_RIGHT) / (
                    c.MAX_TOPHAT_VALUE_RIGHT - c.MIN_TOPHAT_VALUE_RIGHT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_RIGHT: " + str(c.MAX_TOPHAT_VALUE_RIGHT)
            print "c.MIN_TOPHAT_VALUE_RIGHT: " + str(c.MIN_TOPHAT_VALUE_RIGHT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_pid(time, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (
                    c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_value_testing_pid(time, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (
                    c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        if u.right_pressed():
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
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black_pid_safe_no_stop(time=c.SAFETY_TIME, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30 or error < -30:
            kp = 20
        else:
            kp = c.KP
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False


def lfollow_left_until_right_senses_black_pid(time=c.SAFETY_TIME, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black_pid_cheeky(time=c.SAFETY_TIME, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.LEFT_TOPHAT_BW + 300 - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT + 300 - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black_pid_better_for_white_bad_for_black(time=c.SAFETY_TIME, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    flag = True
    target = 100.0 * (c.LEFT_TOPHAT_BW + 300 - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT + 300 - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        if error > 30:
            kp = 7
            ki = c.KI
            kd = c.KD
            flag = False
        if error < 1 and error > -1:
            kp = 3
            ki = 0
            kd = 0
            flag = False
        if flag == True:
            kp = 3
            ki = 1
            kd = 1
        flag = True
        left_power = c.BASE_LM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER - ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def lfollow_left_inside_line_pid(time, kp=c.KP, ki=c.KI, kd=c.KD):
    first_run_through = True
    target = 100.0 * (c.LEFT_TOPHAT_BW - c.MIN_TOPHAT_VALUE_LEFT) / (c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
    base_power_left = c.BASE_LM_POWER
    base_power_right = c.BASE_RM_POWER
    last_error = 0
    integral = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        norm_reading = 100.0 * (analog(c.LEFT_TOPHAT) - c.MIN_TOPHAT_VALUE_LEFT) / (
                    c.MAX_TOPHAT_VALUE_LEFT - c.MIN_TOPHAT_VALUE_LEFT)
        error = target - norm_reading  # Positive error means white, negative means black.
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + (
                    (kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
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
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))
            print "Norm reading: " + str(norm_reading)
            print "Error: " + str(error)
            print "Derivative: " + str(derivative)
            print "kd: " + str(kd)
            print "left_power: " + str(left_power)
            print "right_power: " + str(right_power)
            print "BASE_RM_POWER: " + str(c.BASE_RM_POWER)
            print "c.MAX_TOPHAT_VALUE_LEFT: " + str(c.MAX_TOPHAT_VALUE_LEFT)
            print "c.MIN_TOPHAT_VALUE_LEFT: " + str(c.MIN_TOPHAT_VALUE_LEFT)
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Debug~~~~~~~~~~~~~~~~~~~~~~~~

def debug_right_tophat():
    if BlackRight():
        print "Right tophat senses black: " + str(analog(c.RIGHT_TOPHAT))
    elif NotBlackRight():
        print "Right tophat see white: " + str(analog(c.RIGHT_TOPHAT))
    else:
        print "Error in defining BlackRight and NotBlackRight"
        u.sd()


def debug_left_tophat():
    if BlackLeft():
        print "Left tophat senses black: " + str(analog(c.LEFT_TOPHAT))
    elif NotBlackLeft():
        print "Left tophat senses white: " + str(analog(c.LEFT_TOPHAT))
    else:
        print "Error in defining BlackLeft and NotBlackLeft"
        u.sd()
