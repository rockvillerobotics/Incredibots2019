from wallaby import *
from decorators import *
import constants as c
import sensors as s
import movement as m
import utils as u

#-----------------------Calibration Commands-------------------------------------
# Calibrate gyro "zeroes" the gyro sensor. It determines what the gyro reads when the bot is resting.
# Determine gyro conversion rate figures out how many degrees the gyro sensor counts during a 360 degree
# turn and uses that as a basis for all other turns
# Calibrate motor powers has the robot drive straight using the gyro sensor and sets the powers being used to drive
# straight to be the base powers.


def get_change_in_angle():
    return(-gyro_x())

def calibrate_gyro():
    i = 0
    avg = 0
    while i < 100:
        avg = avg + get_change_in_angle()
        msleep(1)
        i = i + 1
    global bias
    bias = avg/i
    msleep(60)


def determine_gyro_conversion_rate():
    angle = 0
    print "Starting determine_gyro_conversion_rate()"
    print "Starting s.isLeftOnWhite()"
    while s.isLeftOnWhite():
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
    print "Starting s.isLeftOnBlack()"
    while s.isLeftOnBlack():
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
    print "Starting s.isLeftOnWhite()"
    while s.isLeftOnWhite():
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
    print "Starting s.isLeftOnBlack()"
    while s.isLeftOnBlack():
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
    print "Starting s.isLeftOnWhite()"
    while s.isLeftOnWhite():
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
    print "Deactivating motors"
    m.deactivate_motors()
    print "Finished deactivating motors"
    c.DEGREE_CONVERSION_RATE = abs(angle / 360.0) #- 92
    print "DEGREE_CONVERSION_RATE: " + str(c.DEGREE_CONVERSION_RATE)


@print_function_name_with_arrows
def calibrate_motor_powers():
    angle = 0
    error = 0
    i = 0
    total_left_speed = 0
    total_right_speed = 0
    sec = seconds() + 3
    while seconds() < sec:
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER + error
        total_left_speed += left_speed
        total_right_speed += right_speed
        i += 1
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
        error = 0.034470956 * angle  # Positive error means veering left. Negative means veering right.
    m.deactivate_motors()
    avg_left_speed = total_left_speed / i
    avg_right_speed = total_right_speed / i
    c.BASE_LM_POWER = int(avg_left_speed)
    c.BASE_RM_POWER = int(avg_right_speed)
    print "c.BASE_LM_POWER: " + str(c.BASE_LM_POWER)
    print "c.BASE_RM_POWER: " + str(c.BASE_RM_POWER)


#---------------------Gyro Updating Commands--------------------------------------------
# The gyro sensor is best when it only updates every 10 ms, so we make sure it'll only update after that much time.

def update_gyro_cheeky():
    time_since_last_update = ((seconds() - c.SECONDS_DELAY) - c.LAST_GYRO_UPDATE) * 1000
    if time_since_last_update >= 10:
        c.ROBOT_ANGLE += (get_change_in_angle() - bias) * 10 * (time_since_last_update / (time_since_last_update - (time_since_last_update / 36.5)))
        c.LAST_GYRO_UPDATE = seconds() - c.SECONDS_DELAY


def update_gyro(ms=1):
    c.MS_SINCE_LAST_GYRO_UPDATE += ms
    if c.MS_SINCE_LAST_GYRO_UPDATE >= 10:
        c.ROBOT_ANGLE += (get_change_in_angle() - bias) * 10
        c.MS_SINCE_LAST_GYRO_UPDATE -= 10


def print_robot_angle():
    print "Robot Angle: " + str(c.ROBOT_ANGLE / c.DEGREE_CONVERSION_RATE)

#-----------------------Gyro-Based Movement Commands-------------------------------------
# The gyro sensor can determine what angle the robot is at any given point in time. So, if the gyro sensor senses
# an angle other than 0, then it is clear that the bot is veering. So, the robot veers in the opposite direction to
# reduce the error proportionally to how big the error is.

@print_function_name_with_arrows
def drive_gyro(time, stop=True):
    angle = 0
    error = 0
    if time == 0:
        stop = False
        time = c.SAFETY_TIME
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
        error = 0.034470956 * angle  # Positive error means veering left. Negative means veering right.
    if stop == True:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_gyro(time, stop=True):
    angle = 0
    error = 0
    if time == 0:
        stop = False
        time = c.SAFETY_TIME
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
        error = 0.034470956 * angle  # Positive error means veering right. Negative means veering left.
    if stop == True:
        m.deactivate_motors()


#-----------------------Gyro-Based Turning Commands-------------------------------------
# The robot turns until the gyro sensor senses the desired angle.

def turn_gyro(degrees, stop=True):
    angle = 0
    target_angle = degrees * c.DEGREE_CONVERSION_RATE
    if target_angle > 0:
        m.base_turn_left()
        sec = seconds() + c.SAFETY_TIME
        while angle < target_angle and seconds() < sec:
            msleep(10)
            angle += (get_change_in_angle() - bias) * 10
    else:
        m.base_turn_right()
        sec = seconds() + c.SAFETY_TIME
        while angle > target_angle and seconds() < sec:
            msleep(10)
            angle += (get_change_in_angle() - bias) * 10
    if stop == True:
        m.deactivate_motors()


def turn_left_gyro(degrees=90, stop=True):
    print "Starting turn_left_gyro() for " + str(degrees) + " degrees"
    turn_gyro(degrees, stop)


def turn_right_gyro(degrees=90, stop=True):
    print "Starting turn_right_gyro() for " + str(degrees) + " degrees"
    turn_gyro(-degrees, stop)


#----------------Gyro-Based Movement Until Tophat-----------------
# Basic gyro-based movement until the tophat senses black or white. This ensures that the
# bot doesn't veer on its way to a line.

@print_function_name_with_arrows
def drive_gyro_until(boolean, time=c.SAFETY_TIME, stop=True):
    angle = 0
    error = 0
    if time == 0:
        stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean()):
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
        error = 0.034470956 * angle  # Positive error means veering left. Negative means veering right.
    if stop == True:
        m.deactivate_motors()


@print_function_name_with_arrows
def drive_gyro_until_black_left(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isLeftOnBlack, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_white_left(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isLeftOnWhite, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_black_right(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isRightOnBlack, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_white_right(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isRightOnWhite, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_black_third(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isThirdOnBlack, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_white_third(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isThirdOnWhite, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_black_fourth(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isFourthOnBlack, time, stop)


@print_function_name_with_arrows
def drive_gyro_until_white_fourth(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until(s.isFourthOnWhite, time, stop)

@print_function_name_with_arrows
def drive_gyro_until_black_right_or_fourth(time=c.SAFETY_TIME, stop=True):
    angle = 0
    error = 0
    if time == 0:
        stop = False
        time = c.SAFETY_TIME
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isFourthOnWhite() and s.isRightOnWhite():
        left_speed = c.BASE_LM_POWER - error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
        error = 0.034470956 * angle  # Positive error means veering left. Negative means veering right.
    if stop == True:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_gyro_until(boolean_function, time=c.SAFETY_TIME, stop=True):
    angle = 0
    error = 0
    if time == 0:
        stop = False
        time = c.SAFETY_TIME
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and not(boolean_function()):
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (get_change_in_angle() - bias) * 10
        error = 0.034470956 * angle  # Positive error means veering left. Negative means veering right.
    if stop == True:
        m.deactivate_motors()


@print_function_name_with_arrows
def backwards_gyro_until_black_left(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isLeftOnBlack, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_white_left(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isLeftOnWhite, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_black_right(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isRightOnBlack, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_white_right(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isRightOnWhite, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_black_third(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isThirdOnBlack, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_white_third(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isThirdOnWhite, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_black_fourth(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isFourthOnBlack, time, stop)


@print_function_name_with_arrows
def backwards_gyro_until_white_fourth(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until(s.isFourthOnWhite, time, stop)


@print_function_name
def drive_gyro_through_line_left(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_black_left(stop=False)
    drive_gyro_until_white_left(time, stop)


@print_function_name
def drive_gyro_through_line_right(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_black_right(stop=False)
    drive_gyro_until_white_right(time, stop)


@print_function_name
def drive_gyro_through_line_third(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_black_third(stop=False)
    drive_gyro_until_white_third(time, stop)


@print_function_name
def drive_gyro_through_line_fourth(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_black_fourth(stop=False)
    drive_gyro_until_white_fourth(time, stop)


@print_function_name
def backwards_gyro_through_line_left(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until_black_left(stop=False)
    backwards_gyro_until_white_left(time, stop)


@print_function_name
def backwards_gyro_through_line_right(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until_black_right(stop=False)
    backwards_gyro_until_white_right(time, stop)


@print_function_name
def backwards_gyro_through_line_third(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until_black_third(stop=False)
    backwards_gyro_until_white_third(time, stop)


@print_function_name
def drive_gyro_to_line_left(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_white_left(stop=False)
    drive_gyro_until_black_left(time, stop)


@print_function_name
def drive_gyro_to_line_right(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_white_right(stop=False)
    drive_gyro_until_black_right(time, stop)


@print_function_name
def drive_gyro_to_line_third(time=c.SAFETY_TIME, stop=True):
    drive_gyro_until_white_third(stop=False)
    drive_gyro_until_black_third(time, stop)


@print_function_name
def backwards_gyro_to_line_left(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until_white_left(stop=False)
    backwards_gyro_until_black_left(time, stop)


@print_function_name
def backwards_gyro_to_line_right(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until_white_right(stop=False)
    backwards_gyro_until_black_right(time, stop)


@print_function_name
def backwards_gyro_to_line_third(time=c.SAFETY_TIME, stop=True):
    backwards_gyro_until_white_third(stop=False)
    backwards_gyro_until_black_third(time, stop)

#-------------------------Debug-----------------------------
