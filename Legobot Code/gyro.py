from wallaby import *
import constants as c
import sensors as s
import movement as m
import utils as u

def turn_left_gyro(degrees = 90):
    turn_gyro(-degrees)


def turn_right_gyro(degrees = 90):
    turn_gyro(degrees)


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
    print "Gyro reading: " + str(gyro_z())
    i = 0
    sum_of_angles = 0
    while i < 100:
        sum_of_angles += gyro_z()
        msleep(1)
        i += 1
    c.AVG_BIAS = sum_of_angles / 100.0
    print "Average bias: " + str(c.AVG_BIAS)


def get_change_in_theta():
    theta = (gyro_z() - c.AVG_BIAS)
    return(theta)


def get_change_in_angle():
    c.ROBOT_ANGLE += (gyro_z() - c.AVG_BIAS)
    msleep(c.GYRO_TIME)


def calibrate_gyro_degrees():
    wallagrees = 0
    i = 0
    #s.drive_until_black()
    #s.align_close()
    m.base_turn_left()
    while s.NotBlackLeft():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.BlackLeft():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.NotBlackLeft():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.BlackLeft():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.NotBlackLeft():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    m.deactivate_motors()
    c.WALLAGREES_TO_DEGREES_RATE = 360.0 / wallagrees * -1
    print "Wallagree-Degree conversion rate: " + str(c.WALLAGREES_TO_DEGREES_RATE)


def calibrate_gyro_degrees_right():
    wallagrees = 0
    i = 0
    #s.drive_until_black()
    #s.align_close()
    m.base_turn_right()
    while s.NotBlackRight():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.BlackRight():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.NotBlackRight():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.BlackRight():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    while s.NotBlackRight():
        wallagrees += get_change_in_theta()
        msleep(c.GYRO_TIME)
    m.deactivate_motors()
    c.WALLAGREES_TO_DEGREES_RATE = 360.0 / wallagrees
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


def drive_gyro(time, kp=1, ki=1, kd=1, stop=True):
    error = 0
    last_error = 0
    integral = 0
    derivative = 0
    first_run_through = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        i = 0
        temp_error = 0
        while i < 10:
            temp_error += get_change_in_theta()
            i += 1
            msleep(1)
        error = temp_error / 10.0  # Positive error means white, negative means black.
        print str(error)
        derivative = error - last_error  # If rate of change is going negative, need to veer left
        last_error = error
        integral = 0.5 * integral + error
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
            m.activate_motors(int(left_power), int(right_power))
        else:
            mav(c.LEFT_MOTOR, int(left_power))
            mav(c.RIGHT_MOTOR, int(right_power))
        first_run_through = False
    if stop == True:
        m.deactivate_motors()



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
                print str(gyro_z() - c.AVG_BIAS)
                msleep(300)
            if c.CURRENT_LM_POWER == 0 and c.CURRENT_RM_POWER == 0:
                pass
            else:
                theta += (gyro_z() - c.AVG_BIAS)
        print str(theta)
        print str(gyro_z() - c.AVG_BIAS)