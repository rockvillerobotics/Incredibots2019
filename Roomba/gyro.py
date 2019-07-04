from wallaby import *
from decorators import *
import constants as c
import sensors as s
import movement as m
import utils as u

@print_function_name
def calibrate_gyro():
    i = 0
    avg = 0
    while i < 100:
        avg = avg + gyro_z()
        msleep(1)
        i = i + 1
    global bias
    bias = avg/i
    msleep(60)


@print_function_name
def forwards_gyro(time, should_stop=True):
    angle = 0
    error = 0
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if should_stop:
        m.deactivate_motors()


@print_function_name
def backwards_gyro(time):
    angle = 0
    error = 0
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering right. Negative means veering left.
    m.deactivate_motors()


@print_function_name
def turn_left_gyro(degrees=90, time=c.RIGHT_TURN_TIME * 6):
    turn_gyro(degrees, time)


@print_function_name
def turn_right_gyro(degrees=90, time=c.RIGHT_TURN_TIME * 6):
    turn_gyro(-degrees, time)


def turn_gyro(degrees, time=c.SAFETY_TIME):
    angle = 0
    target_angle = degrees * c.DEGREE_CONVERSION_RATE
    if target_angle > 0:
        m.base_turn_left()
        sec = seconds() + time
        while angle < target_angle and seconds() < sec:
            msleep(10)
            angle += (gyro_z() - bias) * 10
    else:
        m.base_turn_right()
        sec = seconds() + time
        while angle > target_angle and seconds() < sec:
            msleep(10)
            angle += (gyro_z() - bias) * 10
    m.deactivate_motors()


@print_function_name
def determine_gyro_conversion_rate():
    sec = seconds()
    angle = 0
    while s.isLeftFrontOnWhite():
        msleep(1)
    while s.isLeftFrontOnBlack():
        msleep(10)
        angle += (gyro_z() - bias) * 10
    while s.isLeftFrontOnWhite():
        msleep(10)
        angle += (gyro_z() - bias) * 10
    while s.isLeftFrontOnBlack():
        msleep(10)
        angle += (gyro_z() - bias) * 10
    while s.isLeftFrontOnWhite():
        msleep(10)
        angle += (gyro_z() - bias) * 10
    m.deactivate_motors()
    c.RIGHT_TURN_TIME = int((seconds() - sec) * 1000 / 4.0) - 32
    c.LEFT_TURN_TIME = int((seconds() - sec) * 1000 / 4.0) - 32
    c.DEGREE_CONVERSION_RATE = abs(angle / 360.0) + 2850
    print "DEGREE_CONVERSION_RATE: " + str(c.DEGREE_CONVERSION_RATE)
    print "Finished calibrating.\nWallagree-Degree conversion rate: " + str(c.DEGREE_CONVERSION_RATE)
    print "Right turn time: " + str(c.RIGHT_TURN_TIME)


@print_function_name
def calibrate_motor_powers():
    angle = 0
    error = 0
    i = 0
    total_left_speed = 0
    total_right_speed = 0
    sec = seconds() + 3
    while seconds() < sec:
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        total_left_speed += left_speed
        total_right_speed += right_speed
        i += 1
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    m.deactivate_motors()
    avg_left_speed = total_left_speed / i
    avg_right_speed = total_right_speed / i
    c.BASE_LM_POWER = int(avg_left_speed)
    c.BASE_RM_POWER = int(avg_right_speed)
    print "c.BASE_LM_POWER: " + str(c.BASE_LM_POWER)
    print "c.BASE_RM_POWER: " + str(c.BASE_RM_POWER)

#--------------------------------Gyro Movement Until Cliffs---------------------------------------------

@print_function_name
def forwards_gyro_until_black_rfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightFrontOnWhite():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_black_rcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnWhite():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_black_lfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftFrontOnWhite():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_black_lcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftOnWhite():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_white_rfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightFrontOnBlack():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

@print_function_name
def forwards_gyro_until_white_rcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnBlack():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_white_lfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftFrontOnBlack():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_white_lcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftOnBlack():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_until_black_cliffs(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnWhite() and s.isLeftOnWhite():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_black_rfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightFrontOnWhite():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_black_rcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnWhite():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_black_lfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftFrontOnWhite():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_black_lcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftOnWhite():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_white_rfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightFrontOnBlack():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

@print_function_name
def backwards_gyro_until_white_rcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnBlack():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_white_lfcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftFrontOnBlack():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def backwards_gyro_until_white_lcliff(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftOnBlack():
        left_speed = -c.BASE_LM_POWER - error
        right_speed = -c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name_only_at_beginning
def forwards_gyro_through_line_lcliff(time=c.SAFETY_TIME):
    forwards_gyro_until_black_lcliff(0)
    forwards_gyro_until_white_lcliff(time)


@print_function_name_only_at_beginning
def forwards_gyro_through_line_rcliff(time=c.SAFETY_TIME):
    forwards_gyro_until_black_rcliff(0)
    forwards_gyro_until_white_rcliff(time)


@print_function_name_only_at_beginning
def forwards_gyro_through_line_lfcliff(time=c.SAFETY_TIME):
    forwards_gyro_until_black_lfcliff(0)
    forwards_gyro_until_white_lfcliff(time)


@print_function_name_only_at_beginning
def forwards_gyro_through_line_rfcliff(time=c.SAFETY_TIME):
    forwards_gyro_until_black_rfcliff(0)
    forwards_gyro_until_white_rfcliff(time)


@print_function_name_only_at_beginning
def backwards_gyro_through_line_lcliff(time=c.SAFETY_TIME):
    backwards_gyro_until_black_lcliff(0)
    backwards_gyro_until_white_lcliff(time)


@print_function_name_only_at_beginning
def backwards_gyro_through_line_rcliff(time=c.SAFETY_TIME):
    backwards_gyro_until_black_rcliff(0)
    backwards_gyro_until_white_rcliff(time)


@print_function_name_only_at_beginning
def backwards_gyro_through_line_lfcliff(time=c.SAFETY_TIME):
    backwards_gyro_until_black_lfcliff(0)
    backwards_gyro_until_white_lfcliff(time)


@print_function_name_only_at_beginning
def backwards_gyro_through_line_rfcliff(time=c.SAFETY_TIME):
    backwards_gyro_until_black_rfcliff(0)
    backwards_gyro_until_white_rfcliff(time)


@print_function_name
def backwards_gyro_until_both_white_cliffs(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and (s.isRightOnWhite() and s.isLeftOnWhite()):
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if s.isRightOnBlack():
        while seconds() < sec and s.isLeftOnWhite():
            left_speed = -c.BASE_LM_POWER + error
            right_speed = -c.BASE_RM_POWER - error
            m.activate_motors(left_speed, right_speed)
            msleep(10)
            angle += (gyro_z() - bias) * 10
            error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    else:
        while seconds() < sec and s.isLeftOnWhite():
            left_speed = -c.BASE_LM_POWER + error
            right_speed = -c.BASE_RM_POWER - error
            m.activate_motors(left_speed, right_speed)
            msleep(10)
            angle += (gyro_z() - bias) * 10
            error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

#--------------------------------Gyro Movement Until Depth---------------------------------------------

@print_function_name
def backwards_gyro_until_second_depth(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isSecondDepthNotSensed():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

            
@print_function_name
def backwards_gyro_until_depth(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isDepthNotSensed():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

#--------------------------------Gyro Movement Until Tophat---------------------------------------------

def backwards_gyro_until_item_is_in_claw(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isNothingInClaw():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


#--------------------------------Bump Gyro Commands---------------------------------------------

@print_function_name
def forwards_gyro_until_bump(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRoombaNotBumped():
        left_speed = c.BASE_LM_POWER + error
        right_speed = c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()

@print_function_name
def backwards_gyro_until_pressed_bump_switch(time=c.SAFETY_TIME):
    angle = 0
    error = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isBumpSwitchNotPressed():
        left_speed = -c.BASE_LM_POWER + error
        right_speed = -c.BASE_RM_POWER - error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = 0.003830106222 * angle  # Positive error means veering left. Negative means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()
    

#--------------------------------Wall Assisted Gyro Commands---------------------------------------------
@print_function_name
def forwards_gyro_wall_assisted_on_left(time=c.SAFETY_TIME, kp=1):
    angle = 0
    error = 0
    target_angle = 0
    first_bump = False
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if s.isRoombaBumped():
            if first_bump == True:
                time_at_last_check = seconds()
                time_on_wall = 0
            time_on_wall += (seconds() - time_at_last_check)
            time_at_last_check = seconds()
            u.halve_speeds()
            if s.isLeftBumped() and not(s.isRightBumped()) and time_on_wall < 0.1:
                print "Left is bumped, early on the wall."
                target_angle -= 10
                print "(Left) Target angle: " + str(target_angle)
            elif s.isLeftBumped() and not(s.isRightBumped()) and time_on_wall >= 0.1:
                print "Left is bumped, late on wall."
                target_angle -= 2
                u.normalize_speeds()
                print "(Left) Target angle: " + str(target_angle)
            else:
                print "Both bumped. Turning away faster."
                target_angle -= 70
                print "(Left) Target angle: " + str(target_angle)
            first_bump = False
        else:
            first_bump = True
            u.normalize_speeds()
        left_speed = c.BASE_LM_POWER - error
        right_speed = c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(10)
        angle += (gyro_z() - bias) * 10
        error = target_angle - 0.003830106222 * kp * angle  # Negative error means veering left. Positive means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


@print_function_name
def forwards_gyro_wall_assisted_on_right(time=c.SAFETY_TIME, kp=1):
    angle = 0
    error = 0
    target_angle = 0
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if s.isRoombaBumped():
            u.halve_speeds()
            kp = 5
            target_angle -= 0.1
            print "(Right) Target angle: " + str(target_angle)
        else:
            u.normalize_speeds()
            kp = 1
        left_speed = c.BASE_LM_POWER - error
        right_speed = c.BASE_RM_POWER + error
        m.activate_motors(left_speed, right_speed)
        msleep(100)
        angle += (gyro_z() - bias) * 100
        error = target_angle - 0.003830106222 * kp * angle  # Negative error means veering left. Positive means veering right.
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()