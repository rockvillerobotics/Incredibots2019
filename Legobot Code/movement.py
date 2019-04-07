# Codes involving general motor or servo motion go here

from wallaby import *
import constants as c

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Base Commands ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#  These commands start the motors in a certain way. They are a simplification of activate_motors().

def base_drive(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_left(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_right(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))


def base_backwards(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Basic Movement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Note: Every time the wheels are set to a speed, they must be set back to 0 or they will continue to spin.

def drive(time = c.DEFAULT_DRIVE_TIME, speed_multiplier=1.0):
    base_drive(speed_multiplier)
    print "Drive forwards for %d ms" % time
    msleep(time)
    deactivate_motors()


def turn_left(time = c.LEFT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_left(speed_multiplier)
    print "Turn left for %d ms" % time
    msleep(time)
    deactivate_motors()


def turn_right(time = c.RIGHT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_right(speed_multiplier)
    print "Turn right for %d ms" % time
    msleep(time)
    deactivate_motors()


def backwards(time = c.DEFAULT_BACKWARDS_TIME, speed_multiplier=1.0):
    base_backwards(speed_multiplier)
    print "Drive backwards for %d ms"%time
    msleep(time)
    deactivate_motors()


def wait(time = 1000):  # Same as msleep command, but stops the wheels.
    deactivate_motors()
    msleep(time)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ No Stop Movement~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def drive_no_stop(time = c.DEFAULT_DRIVE_TIME, speed_multiplier=1.0):
    base_drive(speed_multiplier)
    print "Drive forwards for %d ms" % time
    msleep(time)



def turn_left_no_stop(time = c.LEFT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_left(speed_multiplier)
    print "Turn left for %d ms" % time
    msleep(time)


def turn_right_no_stop(time = c.RIGHT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_right(speed_multiplier)
    print "Turn right for %d ms" % time
    msleep(time)


def backwards_no_stop(time = c.DEFAULT_BACKWARDS_TIME, speed_multiplier=1.0):
    base_backwards(speed_multiplier)
    print "Drive backwards for %d ms"%time
    msleep(time)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ No Print Movement~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def drive_no_print(time = c.DEFAULT_DRIVE_TIME, speed_multiplier=1.0):
    base_drive(speed_multiplier)
    msleep(time)
    deactivate_motors()


def turn_left_no_print(time = c.LEFT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_left(speed_multiplier)
    msleep(time)
    deactivate_motors()


def turn_right_no_print(time = c.RIGHT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_right(speed_multiplier)
    msleep(time)
    deactivate_motors()


def backwards_no_print(time = c.DEFAULT_BACKWARDS_TIME, speed_multiplier=1.0):
    base_backwards(speed_multiplier)
    msleep(time)
    deactivate_motors()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ No Stop, No Print Movement~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def drive_no_stop_no_print(time = c.DEFAULT_DRIVE_TIME, speed_multiplier=1.0):
    base_drive(speed_multiplier)
    msleep(time)


def turn_left_no_stop_no_print(time = c.LEFT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_left(speed_multiplier)
    msleep(time)


def turn_right_no_stop_no_print(time = c.RIGHT_TURN_TIME, speed_multiplier = 1.0):
    base_turn_right(speed_multiplier)
    msleep(time)


def backwards_no_stop_no_print(time = c.DEFAULT_BACKWARDS_TIME, speed_multiplier=1.0):
    base_backwards(speed_multiplier)
    msleep(time)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Complex Movement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def activate_motors(left_motor_power = c.BASE_LM_POWER, right_motor_power = c.BASE_RM_POWER):
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
    left_velocity_change = (left_motor_power - c.CURRENT_LM_POWER) / 30
    right_velocity_change = (right_motor_power - c.CURRENT_RM_POWER) / 30
    while abs(c.CURRENT_LM_POWER - left_motor_power) > 100 and abs(c.CURRENT_RM_POWER - right_motor_power) > 100:
        mav(c.LEFT_MOTOR, c.CURRENT_LM_POWER)
        c.CURRENT_LM_POWER += left_velocity_change
        mav(c.RIGHT_MOTOR, c.CURRENT_RM_POWER)
        c.CURRENT_RM_POWER += right_velocity_change
        #if abs(c.CURRENT_LM_POWER) > abs(left_motor_power) or abs(c.CURRENT_RM_POWER) > abs(right_motor_power):
           # print "Velocity too high"
            #exit(86)
        msleep(1)
    mav(c.LEFT_MOTOR, left_motor_power)  # Ensures actual desired value is reached.
    mav(c.RIGHT_MOTOR, right_motor_power)
    c.CURRENT_LM_POWER = left_motor_power
    c.CURRENT_RM_POWER = right_motor_power


def deactivate_motors():
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)
    c.CURRENT_LM_POWER = 0
    c.CURRENT_RM_POWER = 0


def drive_tics(tics, stop = True):
    print "Starting drive_tics"
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER)
    while gmpc(c.LEFT_MOTOR) < tics and gmpc(c.RIGHT_MOTOR) > -1 * tics:
        pass
    if stop == True:
        deactivate_motors()


def backwards_tics(tics, stop = True):
    print "Starting backwards_tics"
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
    while gmpc(c.LEFT_MOTOR) > -1 * tics and gmpc(c.RIGHT_MOTOR) < tics:
        pass
    if stop == True:
        deactivate_motors()


def av(motor_port, desired_velocity):
# Revs a motor up to a given velocity from 0. The motor and desired velocity must be specified. Cannot rev two motors simultaneously.
    if desired_velocity > 1450:
        print "desired_velocity is too high! Power autoset from " + str(desired_velocity) + " to 1450"
        desired_velocity = 1450
    elif desired_velocity < -1450:
        print "desired_velocity is too low! Power autoset from " + str(desired_velocity) + " to -1450"
        desired_velocity = -1450
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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Servos ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#   All these commands move the servo to a specified location at a specified speed. 
#   The more tics per second, the faster the servo moves.

def open_claw(tics = 3, ms = 1, servo_position = c.CLAW_OPEN_POS):
    print "Open claw to desired position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, servo_position, tics, ms)  # Checking for faulty values must go before setting position.
    print "Claw opened to position: %d" % get_servo_position(c.CLAW_SERVO)


def close_claw(tics = 3, ms = 1, servo_position = c.CLAW_CLOSE_POS):
    print "Close claw to desired position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, servo_position, tics, ms)
    print "Claw closed to position: %d" % get_servo_position(c.CLAW_SERVO)


def lift_arm(tics = 3, ms = 1, servo_position = c.ARM_UP_POS):
    print "Set arm servo to desired up position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.ARM_SERVO, servo_position, tics, ms)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)


def lower_arm(tics = 3, ms = 1, servo_position = c.BASE_TIME):
    print "Set arm servo to desired down position: %d" % servo_position
    if servo_position == c.BASE_TIME:
        servo_position = c.ARM_DOWN_POS
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.ARM_SERVO, servo_position, tics, ms)
    print "Arm reached down position: %d" % get_servo_position(c.ARM_SERVO)


def lift_cube_arm(tics = 3, ms = 1, servo_position = c.CUBE_ARM_UP_POS):
    print "Set cube arm servo to desired up position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CUBE_ARM_SERVO, servo_position, tics, ms)
    print "Arm reached up position: %d" % get_servo_position(c.CUBE_ARM_SERVO)


def lower_cube_arm(tics = 3, ms = 1, servo_position = c.CUBE_ARM_DOWN_POS):
    print "Set cube arm servo to desired down position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CUBE_ARM_SERVO, servo_position, tics, ms)
    print "Arm reached down position: %d" % get_servo_position(c.CUBE_ARM_SERVO)


def move_claw(desired_claw_position = c.CLAW_OPEN_POS, claw_tics = 3, claw_ms = 1):
    print "Moving Claw to " + str(desired_claw_position)
    move_servo(c.CLAW_SERVO, desired_claw_position, claw_tics, claw_ms)


def move_arm(desired_arm_position = c.ARM_UP_POS, arm_tics = 3, arm_ms = 1):
    print "Moving Arm to " + str(desired_arm_position)
    move_servo(c.ARM_SERVO, desired_arm_position, arm_tics, arm_ms)


def move_cube_arm(desired_cube_arm_position = c.CUBE_ARM_UP_POS, cube_arm_tics = 3, cube_arm_ms = 1):
    print "Moving Cube Arm to " + str(desired_cube_arm_position)
    move_servo(c.CUBE_ARM_SERVO, desired_cube_arm_position, cube_arm_tics, cube_arm_ms)


def move_servo(servo_port, desired_servo_position, tics = 3, ms = 1):  
# Moves a servo to a given position from its current position. The servo and desired position must be specified.
# Servo move speed = tics / ms
# >18 tics is too high
    intermediate_position = get_servo_position(servo_port)
    print "Starting move_servo()"
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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Bump Sensors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def BumpPressedRight():
    return(digital(c.RIGHT_BUMP_SENSOR) == 1)

def NotBumpPressedRight():
    return(digital(c.RIGHT_BUMP_SENSOR) == 0)


def base_bumpfollow_right():
    if BumpPressedRight():
        m.activate_motors(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)
    else:
        m.activate_motors(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)


def bumpfollow_right_until_left_senses_black(time=c.SAFETY_TIME):
    print "Starting bumpfollow_right_until_left_senses_black()"
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        base_bumpfollow_right()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def bumpfollow_right_until_left_senses_white(time=c.SAFETY_TIME):
    print "Starting bumpfollow_right_until_left_senses_white()"
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        base_bumpfollow_right()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def bumpfollow_right_until_right_senses_black(time=c.SAFETY_TIME):
    print "Starting bumpfollow_right_until_right_senses_black()"
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        base_bumpfollow_right()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()


def bumpfollow_right_until_right_senses_white(time=c.SAFETY_TIME):
    print "Starting bumpfollow_right_until_right_senses_black()"
    if time == 0:
        time = c.SAFETY_TIME_NO_STOP
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        base_bumpfollow_right()
    if time != c.SAFETY_TIME_NO_STOP:
        m.deactivate_motors()