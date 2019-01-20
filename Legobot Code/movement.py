# Codes involving general motor or servo motion go here

from wallaby import *
import constants as c

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Basic Movement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Note: Every time the wheels are set to a speed, they must be set back to 0 or they will continue to spin.

def drive(time = c.DEFAULT_DRIVE_TIME, drive_left_motor_power = c.BASE_LM_POWER, drive_right_motor_power = c.BASE_RM_POWER, drive_starting_speed_left = 0, drive_starting_speed_right = 0, stop = True, drive_print = True):
    activate_motors(drive_left_motor_power, drive_right_motor_power, drive_starting_speed_left, drive_starting_speed_right)
    if drive_print == True:
        print "Drive forwards for %d ms" % time
    msleep(time)
    if stop == True:
        deactivate_motors()


def turn_left(time = c.LEFT_TURN_TIME, speed_multiplier = 1.0, starting_speed_left = 0, starting_speed_right = 0, stop = True, turn_left_print = True):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier *  c.BASE_RM_POWER), starting_speed_left, starting_speed_right)
    if turn_left_print == True:
        print "Turn left for %d ms" % time
    msleep(time)
    if stop == True:
        deactivate_motors()


def turn_right(time = c.RIGHT_TURN_TIME, speed_multiplier = 1.0, starting_speed_left = 0, starting_speed_right = 0, stop = True, turn_right_print = True):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER), starting_speed_left, starting_speed_right)
    if turn_right_print == True:
        print "Turn right for %d ms" % time
    msleep(time)
    if stop == True:
        deactivate_motors()


def backwards(time = c.DEFAULT_BACKWARDS_TIME, backwards_left_motor_power = -1 * c.BASE_LM_POWER, backwards_right_motor_power = -1 * c.BASE_RM_POWER, backwards_starting_speed_left = 0, backwards_starting_speed_right = 0, stop = True, backwards_print = True):
    activate_motors(backwards_left_motor_power, backwards_right_motor_power, backwards_starting_speed_left, backwards_starting_speed_right)
    if backwards_print == True:
        print "Drive backwards for %d ms"%time
    msleep(time)
    if stop == True:
        deactivate_motors()


def wait(time = 1000):  # Same as msleep command, but stops the wheels.
    deactivate_motors()
    msleep(time)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Complex Movement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def activate_motors(left_motor_power = c.BASE_LM_POWER, right_motor_power = c.BASE_RM_POWER, starting_speed_left = c.NO_VALUE, starting_speed_right = c.NO_VALUE):
    if left_motor_power > 1450:
        print "left_motor_power is too high! Power autoset from " + str(left_motor_power) + " to 1450"
        left_motor_power = 1450
    elif left_motor_power < -1450:
        print "left_motor_power is too high! Power autoset from " + str(left_motor_power) + " to -1450"
        left_motor_power = -1450
    if right_motor_power < -1450:
        print "right_motor_power is too high! Power autoset from " + str(right_motor_power) + " to -1450"
        right_motor_power = -1450
    elif right_motor_power > 1450:
        print "right_motor_power is too high! Power autoset from " + str(right_motor_power) + " to 1450"
        right_motor_power = 1450
    left_velocity_change = left_motor_power / 30
    right_velocity_change = right_motor_power / 30
    if starting_speed_left == c.NO_VALUE and starting_speed_right == c.NO_VALUE:
        while abs(c.CURRENT_LM_POWER - left_motor_power) > 100 and abs(c.CURRENT_RM_POWER - right_motor_power) > 100:
            mav(c.LEFT_MOTOR, c.CURRENT_LM_POWER)
            c.CURRENT_LM_POWER += left_velocity_change
            mav(c.RIGHT_MOTOR, c.CURRENT_RM_POWER)
            c.CURRENT_RM_POWER += right_velocity_change
            if abs(c.CURRENT_LM_POWER) > abs(left_motor_power) or abs(c.CURRENT_RM_POWER) > abs(right_motor_power):
                print "Velocity too high"
                exit(86)
            msleep(1)
    elif starting_speed_left != c.NO_VALUE and starting_speed_right != c.NO_VALUE:
        while abs(starting_speed_left - left_motor_power) > 100 and abs(starting_speed_right - right_motor_power) > 100:
            mav(c.LEFT_MOTOR, starting_speed_left)
            c.CURRENT_LM_POWER = starting_speed_left
            starting_speed_left += left_velocity_change
            mav(c.RIGHT_MOTOR, starting_speed_right)
            c.CURRENT_RM_POWER = starting_speed_right
            starting_speed_right += right_velocity_change
            if abs(starting_speed_left) > abs(left_motor_power) or abs(starting_speed_right) > abs(right_motor_power):
                print "Velocity too high"
                exit(86)
            msleep(1)
        mav(c.LEFT_MOTOR, left_motor_power)  # Ensures actual desired value is reached.
    else:
        print "Something seems to have gone wrong. One motor is given a starting speed while the other is not."
        print "Revving being skipped..."
    mav(c.LEFT_MOTOR, left_motor_power)  # Ensures actual desired value is reached.
    mav(c.RIGHT_MOTOR, right_motor_power)
    c.CURRENT_LM_POWER = left_motor_power
    c.CURRENT_RM_POWER = right_motor_power


def deactivate_motors():
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)
    c.CURRENT_LM_POWER = 0
    c.CURRENT_RM_POWER = 0


def drive_tics(tics, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_tics"
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    while gmpc(c.LEFT_MOTOR) < tics and gmpc(c.RIGHT_MOTOR) > -1 * tics:
        pass
    if stop == True:
        deactivate_motors()


def backwards_tics(tics, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_tics"
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    while gmpc(c.LEFT_MOTOR) > -1 * tics and gmpc(c.RIGHT_MOTOR) < tics:
        pass
    if stop == True:
        deactivate_motors()


def drive_no_print(time = c.DEFAULT_DRIVE_TIME, drive_left_motor_power = c.BASE_LM_POWER, drive_right_motor_power = c.BASE_RM_POWER, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    drive(time, drive_left_motor_power, drive_right_motor_power, drive_starting_speed_left, drive_starting_speed_right, stop, False)


def backwards_no_print(time = c.DEFAULT_BACKWARDS_TIME, backwards_left_motor_power = -1 * c.BASE_LM_POWER, backwards_right_motor_power = -1 * c.BASE_RM_POWER, starting_speed_left = 0, starting_speed_right = 0, stop = True):            
    backwards(time, backwards_left_motor_power, backwards_right_motor_power, starting_speed_left, starting_speed_right, stop, False)


def turn_left_no_print(time = c.LEFT_TURN_TIME, speed_multiplier = 1.0, starting_speed_left = 0, starting_speed_right = 0, stop = True):
     turn_left(time, speed_multiplier, starting_speed_left, starting_speed_right, stop, False)


def turn_right_no_print(time = c.RIGHT_TURN_TIME, speed_multiplier = 1.0, starting_speed_left = 0, starting_speed_right = 0, stop = True):
     turn_right(time, speed_multiplier, starting_speed_left, starting_speed_right, stop, False)


def av(motor_port, desired_velocity, intermediate_velocity = c.NO_VALUE):
# Revs a motor up to a given velocity from 0. The motor and desired velocity must be specified. Cannot rev two motors simultaneously.
    if intermediate_velocity == c.NO_VALUE:
        if motor_port == c.LEFT_MOTOR:
            intermediate_velocity = c.CURRENT_LM_POWER
        elif motor_port == c.RIGHT_MOTOR:
            intermediate_velocity = c.CURRENT_RM_POWER
        else:
            print "An invalid motor port was selected."
    velocity_change = desired_velocity / 30
    while abs(intermediate_velocity - desired_velocity) > 100:
        mav(motor_port, intermediate_velocity)
        if motor_port == c.LEFT_MOTOR:
            c.CURRENT_LM_POWER = desired_velocity
        elif motor_port == c.RIGHT_MOTOR:
            c.CURRENT_RM_POWER = desired_velocity
        intermediate_velocity += velocity_change
        if abs(intermediate_velocity) > abs(desired_velocity):
            print "Velocity too high"
            u.sd(86)
        msleep(1)
    mav(motor_port, desired_velocity)  # Ensures actual desired value is reached
    if motor_port == c.LEFT_MOTOR:
        c.CURRENT_LM_POWER = desired_velocity
    elif motor_port == c.RIGHT_MOTOR:
        c.CURRENT_RM_POWER = desired_velocity


def accel(left_desired_velocity = c.BASE_LM_POWER, right_desired_velocity = c.BASE_RM_POWER, left_intermediate_velocity = 0, right_intermediate_velocity = 0):
# Revs both motors up to a given velocity at the same time.
    left_velocity_change = left_desired_velocity / 30
    right_velocity_change = right_desired_velocity / 30
    while abs(left_intermediate_velocity - left_desired_velocity) > 100 and abs(right_intermediate_velocity - right_desired_velocity) > 100:
        mav(c.LEFT_MOTOR, left_intermediate_velocity)
        left_intermediate_velocity += left_velocity_change
        mav(c.RIGHT_MOTOR, right_intermediate_velocity)
        right_intermediate_velocity += right_velocity_change
        if abs(left_intermediate_velocity) > abs(left_desired_velocity) or abs(right_intermediate_velocity) > abs(right_desired_velocity):
            print "Velocity too high"
            exit(86)
        msleep(1)
    mav(c.LEFT_MOTOR, left_desired_velocity)  # Ensures actual desired value is reached.
    mav(c.RIGHT_MOTOR, right_desired_velocity)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Servos ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#   Remember that servos need time to move. A common mistake is to assume they change position instantly.
#   If you set a servo to a position but don't put a long enough wait, the next line can overwrite the
#   servo command. The wallaby cannot move the servo and run another command at the same time.

def open_claw(servo_position = c.CLAW_OPEN_POS, time = c.SERVO_DELAY):
    print "Open claw to desired position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    set_servo_position(c.CLAW_SERVO, servo_position)  # Checking for faulty values must go before setting position.
    msleep(time)
    print "Claw opened to position: %d" % get_servo_position(c.CLAW_SERVO)


def close_claw(servo_position = c.CLAW_CLOSE_POS, time = c.SERVO_DELAY):
    print "Close claw to desired position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    set_servo_position(c.CLAW_SERVO, servo_position)
    msleep(time)
    print "Claw closed to position: %d" % get_servo_position(c.CLAW_SERVO)


def lift_arm(servo_position = c.ARM_HIGH_POS, time = c.SERVO_DELAY):
    print "Set lift servo to desired up position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    set_servo_position(c.ARM_SERVO, servo_position)
    msleep(time)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)


def lower_arm(servo_position = c.ARM_DOWN_POS, time = c.SERVO_DELAY):
    print "Set lift servo to desired down position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    set_servo_position(c.ARM_SERVO, servo_position)
    msleep(time)
    print "Arm reached down position: %d" % get_servo_position(c.ARM_SERVO)


def claw_slow(desired_claw_position = c.CLAW_OPEN_POS, claw_tics = 1, claw_ms = 1):
    servo_slow(c.CLAW_SERVO, desired_claw_position, claw_tics, claw_ms)


def arm_slow(desired_arm_position = c.ARM_HIGH_POS, arm_tics = 1, arm_ms = 1):
    servo_slow(c.ARM_SERVO, desired_arm_position, arm_tics, arm_ms)


def servo_slow(servo_port, desired_servo_position, tics = 1, ms = 1):  # Note: A 1/1 speed is still slower than the base move speed
# Moves a servo slowly to a given position from its current position. The servo and desired position must be specified.
# Servo move speed = tics / ms
# >18 tics is too high
    intermediate_position = get_servo_position(servo_port)
    print "Starting servo_slow()"
    print "Servo current position = %d" % get_servo_position(servo_port)
    print "Servo desired position = %d" % desired_servo_position
    if desired_servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    print "Speed = " + str(tics) + "/" + str(ms) + " tics per ms"
    if tics > 18:
        print "Tic value is too high\n"
        exit(86)
    while abs(get_servo_position(servo_port) - desired_servo_position) > 10:
        # Tolerance of +/- 10 included to account for servo value skipping
        if (get_servo_position(servo_port) - desired_servo_position) >= 1:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position -= tics
        elif (get_servo_position(servo_port) - desired_servo_position) < 1:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position += tics
        else:
           break
        msleep(ms)
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    msleep(30)
    print "Desired position reached. Curent position is %d" % get_servo_position(servo_port)
    print "Completed servo_slow\n"

