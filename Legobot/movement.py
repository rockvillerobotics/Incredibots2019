# Codes involving general motor or servo motion go here
from wallaby import *
from decorators import *
import constants as c
import gyro as g
import sensors as s

#------------------------------- Base Commands -------------------------------
#  These commands start the motors in a certain way. They are just activate motors but in a specific direction.

def base_drive(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_left(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_right(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))


def base_backwards(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))

#------------------------------- Movement Commands-------------------------------
# The most basic of movement. Turns on wheels for a certain amount of time, and then turns off the wheels.
# There is a lot of mumbo jumbo here to keep consistency with the rest of the code, but if you can understand this
# you can understand every other command here.

def drive(time=c.DEFAULT_DRIVE_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_drive(speed_multiplier)
    print "Drive forwards for %d ms" % time
    msleep(time)
    if should_stop:
        deactivate_motors()


def turn_left(time=c.LEFT_TURN_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_turn_left(speed_multiplier)
    print "Turn left for %d ms" % time
    msleep(time)
    if should_stop:
        deactivate_motors()


def turn_right(time=c.RIGHT_TURN_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_turn_right(speed_multiplier)
    print "Turn right for %d ms" % time
    msleep(time)
    if should_stop:
        deactivate_motors()


def backwards(time=c.DEFAULT_BACKWARDS_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_backwards(speed_multiplier)
    print "Drive backwards for %d ms"%time
    msleep(time)
    if should_stop:
        deactivate_motors()


def stop_for(time=1000):  # Same as msleep command, but stops the wheels.
    deactivate_motors()
    msleep(time)

#------------------------------- No Print Movement -------------------------------
# These, as the name implies, do the same thing as the basic movement commands just without the prints.
# At one time, these were very useful commands. But, as time has gone on and techniques have been improved, they
# have become obsolete. We keep them as an archaic reference to what things use to be. We're nostalgic like that.

def drive_no_print(time=c.DEFAULT_DRIVE_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_drive(speed_multiplier)
    msleep(time)
    if should_stop:
        deactivate_motors()


def turn_left_no_print(time=c.LEFT_TURN_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_turn_left(speed_multiplier)
    msleep(time)
    if should_stop:
        deactivate_motors()


def turn_right_no_print(time=c.RIGHT_TURN_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_turn_right(speed_multiplier)
    msleep(time)
    if should_stop:
        deactivate_motors()


def backwards_no_print(time=c.DEFAULT_BACKWARDS_TIME, should_stop=True, speed_multiplier=1.0):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    base_backwards(speed_multiplier)
    msleep(time)
    if should_stop:
        deactivate_motors()

#------------------------------- Basic Movement Commands -------------------------------
# These commands are really the building blocks of the whole code. They're practical; they're
# built to be used on a daily basis. If you're going to copy something of our code, I would suggest that it be this
# because these are better versions of the wallaby "mav".

def activate_motors(left_motor_power=c.BASE_VALUE, right_motor_power=c.BASE_VALUE):
    if left_motor_power == c.BASE_VALUE:
        left_motor_power = c.BASE_LM_POWER
    if right_motor_power == c.BASE_VALUE:
        right_motor_power = c.BASE_RM_POWER
    if left_motor_power > 1450:
        left_motor_power = 1450
    elif left_motor_power < -1450:
        left_motor_power = -1450
    elif left_motor_power < 1 and left_motor_power >= 0:
        left_motor_power = 1
    elif left_motor_power > -1 and left_motor_power < 0:
        left_motor_power = -1
    if right_motor_power < -1450:
        right_motor_power = -1450
    elif right_motor_power > 1450:
        right_motor_power = 1450
    elif right_motor_power < 1 and right_motor_power >= 0:
        right_motor_power = 1
    elif right_motor_power > -1 and right_motor_power < 0:
        right_motor_power = -1
    if abs(left_motor_power - c.CURRENT_LM_POWER) > 600 or abs(right_motor_power - c.CURRENT_RM_POWER) > 600 or c.CURRENT_LM_POWER == 0 or c.CURRENT_RM_POWER == 0:
        left_velocity_change = (left_motor_power - c.CURRENT_LM_POWER) / 30
        right_velocity_change = (right_motor_power - c.CURRENT_RM_POWER) / 30
        while abs(c.CURRENT_LM_POWER - left_motor_power) > 100 and abs(c.CURRENT_RM_POWER - right_motor_power) > 100:
            mav(c.LEFT_MOTOR, int(c.CURRENT_LM_POWER))
            c.CURRENT_LM_POWER += left_velocity_change
            mav(c.RIGHT_MOTOR, int(c.CURRENT_RM_POWER))
            c.CURRENT_RM_POWER += right_velocity_change
            msleep(1)
            g.update_gyro()
    mav(c.LEFT_MOTOR, int(left_motor_power))  # Ensures actual desired value is reached.
    mav(c.RIGHT_MOTOR, int(right_motor_power))
    c.CURRENT_LM_POWER = left_motor_power
    c.CURRENT_RM_POWER = right_motor_power


def deactivate_motors():
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)
    c.CURRENT_LM_POWER = 0
    c.CURRENT_RM_POWER = 0


def av(motor_port, desired_velocity):
# Revs a motor up to a given velocity from 0. The motor and desired velocity must be specified. Cannot rev two motors simultaneously.
    rev = False
    if desired_velocity > 1450:
        desired_velocity = 1450
    elif desired_velocity < -1450:
        desired_velocity = -1450
    elif desired_velocity < 1 and desired_velocity >= 0:
        desired_velocity = 1
    elif desired_velocity > -1 and desired_velocity < 0:
        desired_velocity = -1
    if motor_port == c.LEFT_MOTOR:
        intermediate_velocity = c.CURRENT_LM_POWER
        if abs(desired_velocity - c.CURRENT_LM_POWER) > 600 or c.CURRENT_LM_POWER == 0:
            rev = True
    elif motor_port == c.RIGHT_MOTOR:
        intermediate_velocity = c.CURRENT_RM_POWER
        if abs(desired_velocity - c.CURRENT_RM_POWER) > 600 or c.CURRENT_RM_POWER == 0:
            rev = True
    else:
        print "An invalid motor port was selected."
    if rev == True:
        velocity_change = desired_velocity / 30.0
        while abs(intermediate_velocity - desired_velocity) > 100:
            mav(motor_port, int(intermediate_velocity))
            if motor_port == c.LEFT_MOTOR:
                c.CURRENT_LM_POWER = desired_velocity
            elif motor_port == c.RIGHT_MOTOR:
                c.CURRENT_RM_POWER = desired_velocity
            intermediate_velocity += velocity_change
            msleep(1)
            g.update_gyro()
    mav(motor_port, int(desired_velocity))  # Ensures actual desired value is reached
    if motor_port == c.LEFT_MOTOR:
        c.CURRENT_LM_POWER = desired_velocity
    elif motor_port == c.RIGHT_MOTOR:
        c.CURRENT_RM_POWER = desired_velocity


#------------------------------- Tics Movement Commands -------------------------------
# Basic movment for a certain distance, measured in wallaby "tics." Your guess is as good as mine as to what a
# "tic" is, but it's the universal wallaby unit of distance. Normally there are about 200 tics to an inch.

@print_function_name_with_arrows
def drive_tics(tics, should_stop=True):
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER)
    while gmpc(c.LEFT_MOTOR) < tics and gmpc(c.RIGHT_MOTOR) > -1 * tics:
        msleep(1)
        g.update_gyro()
    if should_stop:
        deactivate_motors()


@print_function_name_with_arrows
def backwards_tics(tics, should_stop=True):
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
    while gmpc(c.LEFT_MOTOR) > -1 * tics and gmpc(c.RIGHT_MOTOR) < tics:
        msleep(1)
        g.update_gyro()
    if should_stop:
        deactivate_motors()


#------------------------------- Servos -------------------------------
# All these commands move the servo to a specified location at a specified speed.
# The more tics per second, the faster the servo moves.

def open_claw(tics=3, ms=1, servo_position=c.CLAW_OPEN_POS):
    print "Open claw to desired position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, servo_position, tics, ms)  # Checking for faulty values must go before setting position.
    print "Claw opened to position: %d" % get_servo_position(c.CLAW_SERVO)


def close_claw(tics=3, ms=1, servo_position=c.CLAW_CLOSE_POS):
    print "Close claw to desired position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, servo_position, tics, ms)
    print "Claw closed to position: %d" % get_servo_position(c.CLAW_SERVO)


def lift_arm(tics=3, ms=1, servo_position=c.ARM_UP_POS):
    print "Set arm servo to desired up position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.ARM_SERVO, servo_position, tics, ms)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)


def lower_arm(tics=3, ms=1, servo_position=c.BASE_TIME):
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


def swipe_left_windshield_wiper(tics=3, ms=1, servo_position=c.WINDSHIELD_WIPER_LEFT_POS):
    print "Set window wiper servo to desired up position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.WINDSHIELD_WIPER_SERVO, servo_position, tics, ms)
    print "Wiper reached left position: %d" % get_servo_position(c.WINDSHIELD_WIPER_SERVO)


def swipe_right_windshield_wiper(tics=3, ms=1, servo_position=c.WINDSHIELD_WIPER_RIGHT_POS):
    print "Set window wiper servo to desired down position: %d" % servo_position
    if servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.WINDSHIELD_WIPER_SERVO, servo_position, tics, ms)
    print "Wiper reached right position: %d" % get_servo_position(c.WINDSHIELD_WIPER_SERVO)


def move_claw(desired_claw_position=c.CLAW_OPEN_POS, claw_tics=3, claw_ms=1):
    print "Moving Claw to " + str(desired_claw_position)
    move_servo(c.CLAW_SERVO, desired_claw_position, claw_tics, claw_ms)


def move_arm(desired_arm_position = c.ARM_UP_POS, arm_tics=3, arm_ms=1):
    print "Moving Arm to " + str(desired_arm_position)
    move_servo(c.ARM_SERVO, desired_arm_position, arm_tics, arm_ms)


def move_windshield_wiper(desired_windshield_wiper_position, windshield_wiper_tics=3, windshield_wiper_ms=1):
    print "Moving Cube Arm to " + str(desired_windshield_wiper_position)
    move_servo(c.WINDSHIELD_WIPER_SERVO, desired_windshield_wiper_position, windshield_wiper_tics, windshield_wiper_ms)


def move_micro(desired_micro_pos, micro_tics=3, micro_ms=1):
    print "Moving Micro to " + str(desired_micro_pos)
    move_servo(c.MICRO_SERVO, desired_micro_pos, micro_tics, micro_ms)


def wipe_with_micro(tics=5):
    if c.MICRO_LEFT_POS > c.MICRO_RIGHT_POS:
        tics = tics
    elif c.MICRO_LEFT_POS < c.MICRO_RIGHT_POS:
        tics = -tics
    if c.MICRO_SHOULD_GO_LEFT:
        intermediate_position = get_servo_position(c.MICRO_SERVO) + tics
        move_servo_to(c.MICRO_SERVO, intermediate_position)
        if c.MICRO_LEFT_POS > c.MICRO_RIGHT_POS:
            if get_servo_position(c.MICRO_SERVO) > c.MICRO_LEFT_POS:
                c.MICRO_SHOULD_GO_RIGHT = True
                c.MICRO_SHOULD_GO_LEFT = False
        else:
            if get_servo_position(c.MICRO_SERVO) < c.MICRO_LEFT_POS:
                c.MICRO_SHOULD_GO_RIGHT = False
                c.MICRO_SHOULD_GO_LEFT = True
    elif c.MICRO_SHOULD_GO_RIGHT:
        intermediate_position = get_servo_position(c.MICRO_SERVO) - tics
        move_servo_to(c.MICRO_SERVO, intermediate_position)
        if c.MICRO_LEFT_POS > c.MICRO_RIGHT_POS:
            if get_servo_position(c.MICRO_SERVO) < c.MICRO_RIGHT_POS:
                c.MICRO_SHOULD_GO_RIGHT = False
                c.MICRO_SHOULD_GO_LEFT = True
        else:
            if get_servo_position(c.MICRO_SERVO) > c.MICRO_RIGHT_POS:
                c.MICRO_SHOULD_GO_RIGHT = False
                c.MICRO_SHOULD_GO_LEFT = True


def move_servo(servo_port, desired_servo_position, tics=3, ms=1):
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
        g.update_gyro()
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    msleep(30)
    print "Desired position reached. Curent position is %d" % get_servo_position(servo_port)
    print "Completed servo_slow\n"


def move_servo_to(servo_port, desired_servo_position):
    invalid_desired_servo_position = False
    print "Starting move_servo_to()"
    print "Servo current position = %d" % get_servo_position(servo_port)
    print "Servo desired position = %d" % desired_servo_position
    if desired_servo_position > c.MAX_SERVO_POS:
        print "Invalid desired servo position. Skipping movement...\n"
        invalid_desired_servo_position = True
    elif desired_servo_position < c.MIN_SERVO_POS:
        print "Invalid desired servo position. Skipping movement...\n"
        invalid_desired_servo_position = True
    if not(invalid_desired_servo_position):
        set_servo_position(servo_port, desired_servo_position)

#------------------------------ Servo Motors -------------------------------
# All these commands move the motors to a specified location at a specified speed.
# The more tics per second, the faster the motors moves.

def get_motor_tics(motor_port):
    return(gmpc(motor_port))
    #motor_tics = gmpc(motor_port)
    #while motor_tics > 2047:
    #    motor_tics -= 2047
    #while motor_tics < 0:
    #    motor_tics += 2047
    #return(motor_tics)


@print_function_name_with_arrows
def lift_ambulance_arm(desired_speed=c.BASE_AMBULANCE_ARM_POWER):
    move_ambulance_arm(c.AMBULANCE_ARM_HIGH_POS, desired_speed)


@print_function_name_with_arrows
def lower_ambulance_arm(desired_speed=c.BASE_AMBULANCE_ARM_POWER):
    if s.isLeftLimitSwitchNotPressed():
        mav(c.AMBULANCE_ARM_MOTOR, -c.BASE_AMBULANCE_ARM_POWER)
        s.wait_until_limit_switch_is_pressed()
        mav(c.AMBULANCE_ARM_MOTOR, 0)
    cmpc(c.AMBULANCE_ARM_MOTOR)
    #move_ambulance_arm(c.AMBULANCE_ARM_LOW_POS, desired_speed)


@print_function_name_with_arrows
def move_ambulance_arm(desired_tic_location, desired_speed=c.BASE_AMBULANCE_ARM_POWER):
    move_motor(c.AMBULANCE_ARM_MOTOR, desired_tic_location, desired_speed)


@print_function_name_with_arrows
def move_motor(motor_port, desired_tic_location, desired_speed):
    # 2047 tics in 360 degrees
    # while desired_tic_location > 2047:
    #    desired_tic_location -= 2047
    # while desired_tic_location < 0:
    #    desired_tic_location += 2047
    if desired_tic_location - get_motor_tics(motor_port) > 0:
        desired_speed = desired_speed
    elif desired_tic_location - get_motor_tics(motor_port) < 0:
        desired_speed = -desired_speed
    else:
        print "Boi you're bad. The desired location and the current location are the same."
    print "Current tic location: " + str(get_motor_tics(c.AMBULANCE_ARM_MOTOR))
    print "Desired tic location: " + str(desired_tic_location)
    sec = seconds() + 2000 / 1000.0
    while seconds() < sec and abs(desired_tic_location - get_motor_tics(motor_port)) > 5:
        speed = (desired_tic_location - get_motor_tics(motor_port)) * 20
        if speed > desired_speed:
            speed = desired_speed
        elif speed < desired_speed:
            speed = desired_speed
        elif speed >= 0 and speed < 11:
            speed = 11
        elif speed < 0 and speed > -11:
            speed = -11
        mav(motor_port, speed)
        msleep(1)
    mav(motor_port, 0)


#------------------------------- Bump Sensors -------------------------------

def bumpPressedRight():
    return(digital(c.RIGHT_BUMP_SENSOR) == 1)

def notBumpPressedRight():
    return(digital(c.RIGHT_BUMP_SENSOR) == 0)


def base_bumpfollow_right():
    if bumpPressedRight():
        activate_motors(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)
    else:
        activate_motors(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
    msleep(1)
    g.update_gyro()


@print_function_name_with_arrows
def bumpfollow_right_until_black_left(time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftOnWhite():
        base_bumpfollow_right()
    if should_stop:
        deactivate_motors()


@print_function_name_with_arrows
def bumpfollow_right_until_white_left(time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isLeftOnBlack():
        base_bumpfollow_right()
    if should_stop:
        deactivate_motors()


@print_function_name_with_arrows
def bumpfollow_right_until_black_right(time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnWhite():
        base_bumpfollow_right()
    if should_stop:
        deactivate_motors()


@print_function_name_with_arrows
def bumpfollow_right_until_white_right(time=c.SAFETY_TIME, should_stop=True):
    if time == 0:
        should_stop = False
        time = c.SAFETY_TIME
    sec = seconds() + time / 1000.0
    while seconds() < sec and s.isRightOnBlack():
        base_bumpfollow_right()
    if should_stop:
        deactivate_motors()
