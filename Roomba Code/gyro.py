from wallaby import *
import constants as c
import sensors as s
import movement as m
import utils as u

def turn_left_gyro(degrees = 90):
    print "Starting turn_left_gyro()"
    turn_gyro(-degrees)
    print "Degrees turned: " + str(c.ROBOT_ANGLE * -1 * c.WALLAGREES_TO_DEGREES_RATE)


def turn_right_gyro(degrees = 90):
    print "Starting turn_right_gyro()"
    turn_gyro(degrees)
    print "Degrees turned: " + str(c.ROBOT_ANGLE * c.WALLAGREES_TO_DEGREES_RATE)


def run_gyro():
    print "Starting run_gyro()"
    u.calibrate()
    msleep(3000)
    i = 0
    while i < 4:
        turn_gyro(-90)
        print str(c.ROBOT_ANGLE * c.WALLAGREES_TO_DEGREES_RATE)
        msleep(1000)
        i += 1
    print str(c.ROBOT_ANGLE * c.WALLAGREES_TO_DEGREES_RATE)


def calibrate_gyro():
    # We need to figure out the gyro's resting value. This runs 50 trials to figure out the average amount the gyro
    # sensor is off. The robot must be still while this occurs.
    print "Gyro reading: " + str(gyro_x())
    i = 0
    sum_of_angles = 0
    while i < 100:
        sum_of_angles += gyro_x()
        msleep(1)
        i += 1
    c.AVG_BIAS = sum_of_angles / 100.0
    print "Average bias: " + str(c.AVG_BIAS)


def get_change_in_theta():
    theta = (gyro_x() - c.AVG_BIAS)
    return(theta)


def get_change_in_angle():
    c.ROBOT_ANGLE += (gyro_x() - c.AVG_BIAS)
    msleep(c.GYRO_TIME)


def calibrate_gyro_degrees():
    print "Starting calibrate_gyro_degrees()"
    c.ROBOT_ANGLE = 0
    #s.drive_until_black()
    #s.align_close()
    sec = seconds()
    m.base_turn_left()
    while s.NotBlackFrontLeft():
        get_change_in_angle()
    while s.BlackFrontLeft():
        get_change_in_angle()
    while s.NotBlackFrontLeft():
        get_change_in_angle()
    while s.BlackFrontLeft():
        get_change_in_angle()
    while s.NotBlackFrontLeft():
        get_change_in_angle()
    c.RIGHT_TURN_TIME = int((seconds() - sec) * 1000 / 4.0) - 30
    c.LEFT_TURN_TIME = int((seconds() - sec) * 1000 / 4.0) - 30
    m.deactivate_motors()
    c.WALLAGREES_TO_DEGREES_RATE = (360.0 / c.ROBOT_ANGLE * -1) / 2
    print "Finished calibrating.\nWallagree-Degree conversion rate: " + str(c.WALLAGREES_TO_DEGREES_RATE)
    print "Right turn time: " + str(c.RIGHT_TURN_TIME)


def calibrate_gyro_degrees_right():
    c.ROBOT_ANGLE = 0
    #s.drive_until_black()
    #s.align_close()
    m.base_turn_right()
    while s.NotBlackFrontRight():
        get_change_in_angle()
    while s.BlackFrontRight():
        get_change_in_angle()
    while s.NotBlackFrontRight():
        get_change_in_angle()
    while s.BlackFrontRight():
        get_change_in_angle()
    while s.NotBlackFrontRight():
        get_change_in_angle()
    m.deactivate_motors()
    c.WALLAGREES_TO_DEGREES_RATE = (360.0 / c.ROBOT_ANGLE) * 2
    print "Wallagree-Degree conversion rate: " + str(c.WALLAGREES_TO_DEGREES_RATE)


def turn_gyro(target_degrees = 90, speed_multiplier = 1):
    c.ROBOT_ANGLE = 0
    if target_degrees < 0:  # Left turn code is different than right turn. Positive degrees are left.
        m.base_turn_left(speed_multiplier)
        while c.ROBOT_ANGLE * c.WALLAGREES_TO_DEGREES_RATE > target_degrees:
            get_change_in_angle()
    else:
        m.base_turn_right(speed_multiplier)
        while c.ROBOT_ANGLE * c.WALLAGREES_TO_DEGREES_RATE < target_degrees:
            get_change_in_angle()
    m.deactivate_motors()


def drive_gyro(time, kp=10, ki=.1, kd=1, stop=True):
    error = 0
    last_error = 0
    integral = 0
    derivative = 0
    first_run_through = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        error = (gyro_x() - c.AVG_BIAS) * c.WALLAGREES_TO_DEGREES_RATE
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
        c.ROBOT_ANGLE += error
        left_power = c.BASE_LM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))
        right_power = c.BASE_RM_POWER + ((kp * error) + (ki * integral) + (kd * derivative))  # Addition decreases power here
        if left_power > 1300:
            left_power = 1300
        elif left_power < -1000:
            left_power = -1000
        if right_power < -1300:
            right_power = -1300
        elif right_power > 1000:
            right_power = 1000
        if first_run_through == True:
            m.activate_motors(int(left_power), int(right_power))  # this is where the accelerate command would go if we had one.
        else:
            m.activate_motors(int(left_power), int(right_power))
        first_run_through = False
        msleep(c.GYRO_TIME)
    if stop == True:
        m.deactivate_motors()


def calibrate_gyro_degrees_hard_coded():
    print "Starting calibrate_gyro_degrees_hard_coded()"
    i = 0
    #s.drive_until_black()
    #s.align_close()
    m.base_turn_right()
    sec = seconds() + 4 * c.RIGHT_TURN_TIME / 1000.0
    while seconds() < sec:
        get_change_in_angle()
    m.deactivate_motors()
    c.WALLAGREES_TO_DEGREES_RATE = 360.0 / c.ROBOT_ANGLE
    print "Wallagree-Degree conversion rate: " + str(c.WALLAGREES_TO_DEGREES_RATE)


def test_gyro(time=20000):
    print "Starting test_gyro"
    theta = 0
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER*-1)
    sec = seconds() + time / 1000.0
    turn_time = seconds() + c.RIGHT_TURN_TIME / 1000.0
    while seconds() < sec:
        sec_2 = seconds() + 1
        while seconds() < sec_2:
            msleep(10)
            if seconds() > turn_time:
                print "Turn time reached"
                m.deactivate_motors()
                print str(theta)
                print str(gyro_x() - c.AVG_BIAS)
                msleep(300)
            if c.CURRENT_LM_POWER == 0 and c.CURRENT_RM_POWER == 0:
                pass
            else:
                theta += (gyro_x() - c.AVG_BIAS)
        print str(theta)
        print str(gyro_x() - c.AVG_BIAS)