from wallaby import *
import constants as c
import sensors as s
import movement as m

#-----------------------------ARM----------------------------

def arm_slow(desired_arm_position = c.ARM_DOWN_POS, arm_tics = 1, arm_ms = 1):
    servo_slow(c.ARM_SERVO, desired_arm_position, arm_tics, arm_ms)


def micro_slow(desired_micro_position = c.MICRO_LEFT_POS, micro_tics = 1, micro_ms = 1):
    servo_slow(c.MICRO_SERVO, desired_micro_position, micro_tics, micro_ms)


def servo_slow(servo_port, desired_servo_position, tics = 1, ms = 1):
# Moves a servo slowly to a given position from its current position. The servo and desired position must be specified
# Servo move speed = tics / ms
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


def lift_arm(servo_position = c.ARM_UP_POS, time = 300):
    print "Set lift servo to desired up position: %d" % servo_position
    if servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    set_servo_position(c.ARM_SERVO, servo_position)
    msleep(time)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)


def lower_arm(servo_position = c.ARM_DOWN_POS, time = 300):
    print "Set lift servo to desired down position: %d" % servo_position
    if servo_position > c.MAX_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if servo_position < c.MIN_ARM_SERVO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    set_servo_position(c.ARM_SERVO, servo_position)
    msleep(time)
    print "Arm reached down position: %d" % get_servo_position(c.ARM_SERVO)

#-----------------------------Driving-------------------------

def activate_motors(direction = -1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    print "Activate motors."
    create_drive_direct(direction * left_power, direction * right_power)


def deactivate_motors():
    print "Deactivate motors."
    create_stop()


def drive(time=c.DEFAULT_DRIVE_TIME, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(left_power, right_power)
    print "Drive forwards for %d ms" % time
    msleep(time)
    create_stop()    


def backwards(time = c.DEFAULT_BACKWARDS_TIME, backwards_left_motor_power = -1 * c.BASE_LM_POWER, backwards_right_motor_power = -1 * c.BASE_RM_POWER):
    create_drive_direct(backwards_left_motor_power, backwards_right_motor_power)
    print "Drive backwards for %d ms" % time
    msleep(time)
    create_stop()


def wait(time=1000):
    ao()
    create_stop()    
    msleep(time)

#-------------------------------Turns------------------------

def turn_left(time=c.LEFT_TURN_TIME, left_power = -1 * c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(left_power, right_power)
    msleep(time)
    print "Turn left for %d ms" % time
    create_stop()

        
def turn_right(time=c.RIGHT_TURN_TIME, left_power = c.BASE_LM_POWER, right_power = -1 * c.BASE_RM_POWER):
    create_drive_direct(left_power, right_power)
    msleep(time)
    print "Turn right for %d ms" % time
    create_stop()
