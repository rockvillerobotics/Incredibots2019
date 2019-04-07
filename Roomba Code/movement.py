from wallaby import *
import constants as c

#-----------------------------Base Commands-------------------------

def base_forwards(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_left(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_right(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))


def base_backwards(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))

#-----------------------------Basic Movement-------------------------

def activate_motors(left_power=c.BASE_LM_POWER, right_power=c.BASE_RM_POWER):
    create_drive_direct(int(left_power),int(right_power))
    c.CURRENT_LM_POWER = left_power
    c.CURRENT_RM_POWER = right_power


def deactivate_motors():
    create_stop()
    c.CURRENT_LM_POWER = 0
    c.CURRENT_RM_POWER = 0


def forwards(time=c.DEFAULT_DRIVE_TIME, speed_multiplier=1.0):
    base_forwards(speed_multiplier)
    print "Drive forwards for %d ms" % time
    msleep(int(time))
    deactivate_motors()


def backwards(time=c.DEFAULT_BACKWARDS_TIME, speed_multiplier=1.0):
    base_backwards(speed_multiplier)
    print "Drive backwards for %d ms" % time
    msleep(int(time))
    deactivate_motors()


def turn_left(time=c.BASE_TIME, speed_multiplier=1.0):
    if time == c.BASE_TIME:
        time = c.LEFT_TURN_TIME
    base_turn_left(speed_multiplier)
    msleep(int(time))
    print "Turn left for %d ms" % time
    deactivate_motors()


def turn_right(time=c.BASE_TIME, speed_multiplier=1.0):
    if time == c.BASE_TIME:
        time = c.RIGHT_TURN_TIME
    base_turn_right(speed_multiplier)
    msleep(int(time))
    print "Turn right for %d ms" % time
    deactivate_motors()


def wait(time=1000):
    deactivate_motors()
    msleep(25)
    ao()
    msleep(time-25)


def av(motor_port, motor_power):
    # Moves one motor without affecting the other motor.
    if motor_port == c.LEFT_MOTOR:
        create_drive_direct(int(motor_power), c.CURRENT_RM_POWER)
        c.CURRENT_LM_POWER = motor_power
    elif motor_port == c.RIGHT_MOTOR:
        create_drive_direct(c.CURRENT_RM_POWER, int(motor_power))
        c.CURRENT_RM_POWER = motor_power
    else:
        print "Error in determining motor port for av()"
        msleep(2000)

#-----------------------------Servos----------------------------

def lift_arm(tics=3, ms=1, servo_position=c.ARM_UP_POS):
    print "Lifting servo to: %d" % servo_position
    if servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.ARM_SERVO, servo_position, tics, ms)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)


def lower_arm(tics=3, ms=1, servo_position=c.ARM_DOWN_POS):
    print "Lowering arm to: %d" % servo_position
    if servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.ARM_SERVO, servo_position, tics, ms)
    print "Arm reached down position: %d" % get_servo_position(c.ARM_SERVO)


def open_claw(tics=3, ms=1, servo_position=c.CLAW_OPEN_POS):
    print "Opening claw to: %d" % servo_position
    if servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, servo_position, tics, ms)
    print "Claw reached close position: %d" % get_servo_position(c.CLAW_SERVO)


def close_claw(tics=3, ms=1, servo_position=c.CLAW_CLOSE_POS):
    print "Closing claw to: %d" % servo_position
    if servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, servo_position, tics, ms)
    print "Claw reached close position: %d" % get_servo_position(c.CLAW_SERVO)


def move_arm(desired_arm_position=c.ARM_DOWN_POS, arm_tics=3, arm_ms=1):
    move_servo(c.ARM_SERVO, desired_arm_position, arm_tics, arm_ms)


def move_micro(desired_micro_position=c.MICRO_LEFT_POS, micro_tics=3, micro_ms=1):
    move_servo(c.MICRO_SERVO, desired_micro_position, micro_tics, micro_ms)


def move_claw(desired_claw_position=c.CLAW_CLOSE_POS, claw_tics=3, claw_ms=1):
    move_servo(c.CLAW_SERVO, desired_claw_position, claw_tics, claw_ms)


def move_servo(servo_port, desired_servo_position, tics=3, ms=1):
# Moves a servo slowly to a given position from its current position. The servo and desire
# Servo move speed = tics / msd position must be specified
# >18 tics is too high
    intermediate_position = get_servo_position(servo_port)
    print "Starting servo_slow()"
    print "Servo current position = %d" % get_servo_position(servo_port)
    print "Servo desired position = %d" % desired_servo_position
    if desired_servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_servo_position < c.MIN_ARM_SERVO_POS:
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
        elif (get_servo_position(servo_port) - desired_servo_position) <= 1:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position += tics
        else:
           break
        msleep(ms)
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    msleep(30)
    print "Desired position reached. Curent position is %d" % get_servo_position(servo_port)
    print "Completed servo_slow\n"