from wallaby import *
from decorators import *
import constants as c

#-----------------------------Bump Sensors-------------------------

def isLimitSwitchBumped():
    return(digital(c.LIMIT_SWITCH) == 1)

def isLimitSwitchNotBumped():
    return(digital(c.LIMIT_SWITCH) == 0)

def isBumpSwitchBumped():
    return(digital(c.BUMP_SWITCH) == 1)

def isBumpSwitchNotBumped():
    return(digital(c.BUMP_SWITCH) == 0)

#-----------------------------Base Commands-------------------------

def base_forwards(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_left(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_turn_right(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))


def base_backwards(speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * -1 * c.BASE_LM_POWER), int(speed_multiplier * -1 * c.BASE_RM_POWER))


def base_veer_left(veer_multiplier=1, speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * veer_multiplier * 0.7 * c.BASE_LM_POWER), int(speed_multiplier * c.BASE_RM_POWER))


def base_veer_right(veer_multiplier=1, speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * c.BASE_LM_POWER), int(speed_multiplier * veer_multiplier * 0.7 * c.BASE_RM_POWER))

def base_veer(veer_multiplier_left=1, veer_multiplier_right=1, speed_multiplier=1.0):
    activate_motors(int(speed_multiplier * veer_multiplier_left * c.BASE_LM_POWER), int(speed_multiplier * veer_multiplier_right * c.BASE_RM_POWER))

#-----------------------------Basic Movement-------------------------

def activate_motors(left_motor_power=c.BASE_POWER, right_motor_power=c.BASE_POWER):
    if left_motor_power == c.BASE_POWER:
        left_motor_power = c.BASE_LM_POWER
    if right_motor_power == c.BASE_POWER:
        right_motor_power = c.BASE_RM_POWER
    if left_motor_power > 490:
        left_motor_power = 490
    elif left_motor_power < -490:
        left_motor_power = -490
    elif left_motor_power < 1 and left_motor_power >= 0:
        left_motor_power = 1
    elif left_motor_power > -1 and left_motor_power < 0:
        left_motor_power = -1
    if right_motor_power < -490:
        right_motor_power = -490
    elif right_motor_power > 490:
        right_motor_power = 490
    elif right_motor_power < 1 and right_motor_power >= 0:
        right_motor_power = 1
    elif right_motor_power > -1 and right_motor_power < 0:
        right_motor_power = -1
    if abs(left_motor_power - c.CURRENT_LM_POWER) > 150 or abs(right_motor_power - c.CURRENT_RM_POWER) > 150 or c.CURRENT_LM_POWER == 0 or c.CURRENT_RM_POWER == 0:
        left_velocity_change = (left_motor_power - c.CURRENT_LM_POWER) / 30
        right_velocity_change = (right_motor_power - c.CURRENT_RM_POWER) / 30
        while abs(c.CURRENT_LM_POWER - left_motor_power) > 10 and abs(c.CURRENT_RM_POWER - right_motor_power) > 10:
            create_drive_direct(int(c.CURRENT_LM_POWER), int(c.CURRENT_RM_POWER))
            c.CURRENT_LM_POWER += left_velocity_change
            c.CURRENT_RM_POWER += right_velocity_change
            msleep(1)
    create_drive_direct(int(left_motor_power), int(right_motor_power))
    c.CURRENT_LM_POWER = int(left_motor_power)
    c.CURRENT_RM_POWER = int(right_motor_power)


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
        create_drive_direct(int(motor_power), int(c.CURRENT_RM_POWER))
        c.CURRENT_LM_POWER = int(motor_power)
    elif motor_port == c.RIGHT_MOTOR:
        create_drive_direct(int(c.CURRENT_LM_POWER), int(motor_power))
        c.CURRENT_RM_POWER = int(motor_power)
    else:
        print "Error in determining motor port for av()"
        msleep(2000)

#-----------------------------Servos----------------------------

def lift_arm(tics=3, ms=1, servo_position=c.ARM_UP_POS):
    print "Lifting servo to: %d" % servo_position
    move_arm(servo_position, tics, ms)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)


def extend_wrist(tics=3, ms=1, servo_position=c.WRIST_OUT_POS):
    print "Extend servo to: %d" % servo_position
    move_wrist(servo_position, tics, ms)
    print "Wrist reached up position: %d" % get_servo_position(c.WRIST_SERVO)

            
def lower_arm(tics=3, ms=1, servo_position=c.ARM_DOWN_POS):
    print "Lowering arm to: %d" % servo_position
    move_arm(servo_position, tics, ms)
    print "Arm reached down position: %d" % get_servo_position(c.ARM_SERVO)
            

def lift_magnet_arm(tics=3, ms=1, servo_position=c.MAGNET_ARM_UP_POS):
    print "Lifting magnet arm to: %d" % servo_position
    move_magnet_arm(servo_position, tics, ms)
    print "Arm reached up position: %d" % get_servo_position(c.ARM_SERVO)

            
def lower_magnet_arm(tics=3, ms=1, servo_position=c.MAGNET_ARM_DOWN_POS):
    print "Lowering magnet arm to: %d" % servo_position
    move_magnet_arm(servo_position, tics, ms)
    print "Arm reached down position: %d" % get_servo_position(c.ARM_SERVO)

        
def retract_wrist(tics=3, ms=1, servo_position=c.WRIST_IN_POS):
    print "Retracting wrist to: %d" % servo_position
    move_wrist(servo_position, tics, ms)
    print "Wrist reached down position: %d" % get_servo_position(c.WRIST_SERVO)
        
      
def open_claw(tics=3, ms=1, servo_position=c.CLAW_OPEN_POS):
    print "Opening claw to: %d" % servo_position
    move_claw(servo_position, tics, ms)
    print "Claw reached close position: %d" % get_servo_position(c.CLAW_SERVO)


def close_claw(tics=3, ms=1, servo_position=c.CLAW_CLOSE_POS):
    print "Closing claw to: %d" % servo_position
    move_claw(servo_position, tics, ms)
    print "Claw reached close position: %d" % get_servo_position(c.CLAW_SERVO)


def lift_micro(tics=3, ms=1, servo_position=c.MICRO_UP_POS):
    print "Lifting micro to: %d" % servo_position
    move_micro(servo_position, tics, ms)
    print "Micro reached up position: %d" % get_servo_position(c.MICRO_SERVO)

            
def retract_micro(tics=3, ms=1, servo_position=c.MICRO_RETRACTED_POS):
    print "Retracting micro to: %d" % servo_position
    move_micro(servo_position, tics, ms)
    print "Micro reached down position: %d" % get_servo_position(c.MICRO_SERVO)


def move_arm(desired_arm_position=c.ARM_DOWN_POS, arm_tics=3, arm_ms=1):
    if desired_arm_position > c.MAX_ARM_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_arm_position < c.MIN_ARM_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.ARM_SERVO, desired_arm_position, arm_tics, arm_ms)


def move_wrist(desired_wrist_position=c.WRIST_IN_POS, wrist_tics=3, wrist_ms=1):
    if desired_wrist_position > c.MAX_WRIST_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_wrist_position < c.MIN_WRIST_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.WRIST_SERVO, desired_wrist_position, wrist_tics, wrist_ms)
            


def move_magnet_arm(desired_magnet_arm_position=c.MAGNET_ARM_DOWN_POS, magnet_arm_tics=3, magnet_arm_ms=1):
    if desired_magnet_arm_position > c.MAX_MAGNET_ARM_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_magnet_arm_position < c.MIN_MAGNET_ARM_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.MAGNET_ARM_SERVO, desired_magnet_arm_position, magnet_arm_tics, magnet_arm_ms)


def move_micro(desired_micro_position=c.MICRO_RETRACTED_POS, micro_tics=3, micro_ms=1):
    if desired_micro_position > c.MAX_MICRO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_micro_position < c.MIN_MICRO_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.MICRO_SERVO, desired_micro_position, micro_tics, micro_ms)


def move_claw(desired_claw_position=c.CLAW_CLOSE_POS, claw_tics=3, claw_ms=1):
    if desired_claw_position > c.MAX_CLAW_POS:
        print "Invalid desired servo position\n"
        exit(86)
    if desired_claw_position < c.MIN_CLAW_POS:
        print "Invalid desired servo position\n"
        exit(86)
    move_servo(c.CLAW_SERVO, desired_claw_position, claw_tics, claw_ms)
        
def move_servo(servo_port, desired_servo_position, tics=3, ms=1):
# Moves a servo slowly to a given position from its current position. The servo and desire
# Servo move speed = tics / msd position must be specified
# >18 tics is too high
    intermediate_position = get_servo_position(servo_port)
    print "Starting move_servo()"
    print "Servo current position = %d" % get_servo_position(servo_port)
    print "Servo desired position = %d" % desired_servo_position
    if desired_servo_position > c.MAX_SERVO_LIMIT:
        print "Invalid desired servo position. Its too high.\n"
        exit(86)
    if desired_servo_position < c.MIN_SERVO_LIMIT:
        print "Invalid desired servo position. Its too low.\n"
        exit(86)
    print "Speed = " + str(tics) + "/" + str(ms) + " tics per ms"
    if tics > 18:
        print "Tic value is too high\n"
        exit(86)
    while abs(get_servo_position(servo_port) - desired_servo_position) > 10:
        # Tolerance of +/- 10 included to account for servo value skipping
        if get_servo_position(servo_port) - desired_servo_position > 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position -= tics
        elif get_servo_position(servo_port) - desired_servo_position <= 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position += tics
        elif abs(get_servo_position(servo_port) - c.MAX_SERVO_LIMIT) < 30 or abs(get_servo_position(servo_port) - c.MIN_SERVO_LIMIT) < 30:
            break
        else:
            break
        msleep(ms)
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    msleep(30)
    print "Desired position reached. Curent position is %d" % get_servo_position(servo_port)
    print "Completed move_servo()\n"


def move_two_servos(servo_port, desired_servo_position, second_servo_port, second_desired_servo_position, tics=3, ms=1):
    # Moves a servo slowly to a given position from its current position. The servo and desire
    # Servo move speed = tics / msd position must be specified
    # >18 tics is too high
    intermediate_position = get_servo_position(servo_port)
    second_intermediate_position = get_servo_position(second_servo_port)
    print "Starting move_two_servos()"
    print "Servo current position = %d" % get_servo_position(servo_port)
    print "Servo desired position = %d" % desired_servo_position
    print "Second servo current position = %d" % get_servo_position(servo_port)
    print "Second servo desired position = %d" % desired_servo_position
    if desired_servo_position > c.MAX_SERVO_LIMIT:
        print "Invalid desired servo position. Its too high.\n"
        exit(86)
    elif desired_servo_position < c.MIN_SERVO_LIMIT:
        print "Invalid desired servo position. Its too low.\n"
        exit(86)
    if second_desired_servo_position > c.MAX_SERVO_LIMIT:
        print "Invalid desired servo position. Its too high.\n"
        exit(86)
    elif second_desired_servo_position < c.MIN_SERVO_LIMIT:
        print "Invalid desired servo position. Its too low.\n"
        exit(86)
    print "Speed = " + str(tics) + "/" + str(ms) + " tics per ms"
    steps = abs(desired_servo_position - intermediate_position) / tics
    second_servo_tics = abs(second_desired_servo_position - second_intermediate_position) / steps
    print "Second servo speed = " + str(second_servo_tics) + "/" + str(ms) + " tics per ms"
    if tics > 18:
        print "Tic value is too high\n"
        exit(86)
    while abs(get_servo_position(servo_port) - desired_servo_position) > 10:
        # Tolerance of +/- 10 included to account for servo value skipping
        if get_servo_position(servo_port) - desired_servo_position > 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position -= tics
        elif get_servo_position(servo_port) - desired_servo_position <= 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position += tics
        elif abs(get_servo_position(servo_port) - c.MAX_SERVO_LIMIT) < 30 or abs(get_servo_position(servo_port) - c.MIN_SERVO_LIMIT) < 30:
            break
        else:
            break
        if get_servo_position(second_servo_port) - desired_second_servo_position > 0:
            set_servo_position(second_servo_port, int(second_intermediate_position))
            second_intermediate_position -= second_servo_tics
        elif get_servo_position(second_servo_port) - desired_second_servo_position <= 0:
            set_servo_position(second_servo_port, int(second_intermediate_position))
            second_intermediate_position += second_servo_tics
        elif abs(get_servo_position(second_servo_port) - c.MAX_SERVO_LIMIT) < 30 or abs(get_servo_position(second_servo_port) - c.MIN_SERVO_LIMIT) < 30:
            break
        else:
            break
        msleep(ms)
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    set_servo_position(second_servo_port, second_desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    msleep(30)
    print "Desired position reached. Curent position is %d" % get_servo_position(servo_port)
    print "Completed move_servo()\n"
                
                
@print_function_name
def extend_arm():
    mav(c.ARM_MOTOR, c.BASE_ARM_MOTOR_POWER)
    while not(isBumpSwitchBumped()):
        msleep(1)
    mav(c.ARM_MOTOR, 0)
    msleep(25)
    ao()


@print_function_name
def retract_arm():
    mav(c.ARM_MOTOR, -c.BASE_ARM_MOTOR_POWER)
    while not(isLimitSwitchBumped()):
        msleep(1)
    mav(c.ARM_MOTOR, 0)
    msleep(25)
    ao()
            

def move_servo_while_activating_motors(servo_port, desired_servo_position, tics=3, ms=1, left_motor_power=c.BASE_POWER, right_motor_power=c.BASE_POWER):
# Moves a servo slowly to a given position from its current position. The servo and desire
# Servo move speed = tics / msd position must be specified
# >18 tics is too high
    intermediate_position = get_servo_position(servo_port)
    if left_motor_power == c.BASE_POWER:
        left_motor_power = c.BASE_LM_POWER
    if right_motor_power == c.BASE_POWER:
        right_motor_power = c.BASE_RM_POWER
    if left_motor_power > 490:
        left_motor_power = 490
    elif left_motor_power < -490:
        left_motor_power = -490
    elif left_motor_power < 1 and left_motor_power >= 0:
        left_motor_power = 1
    elif left_motor_power > -1 and left_motor_power < 0:
        left_motor_power = -1
    if right_motor_power < -490:
        right_motor_power = -490
    elif right_motor_power > 490:
        right_motor_power = 490
    elif right_motor_power < 1 and right_motor_power >= 0:
        right_motor_power = 1
    elif right_motor_power > -1 and right_motor_power < 0:
        right_motor_power = -1
    print "Starting move_servo()"
    print "Servo current position = %d" % get_servo_position(servo_port)
    print "Servo desired position = %d" % desired_servo_position
    if desired_servo_position > c.MAX_SERVO_LIMIT:
        print "Invalid desired servo position. Its too high.\n"
        exit(86)
    if desired_servo_position < c.MIN_SERVO_LIMIT:
        print "Invalid desired servo position. Its too low.\n"
        exit(86)
    print "Speed = " + str(tics) + "/" + str(ms) + " tics per ms"
    if tics > 18:
        print "Tic value is too high\n"
        exit(86)
    left_velocity_change = (left_motor_power - c.CURRENT_LM_POWER) / 30
    right_velocity_change = (right_motor_power - c.CURRENT_RM_POWER) / 30
    while abs(get_servo_position(servo_port) - desired_servo_position) > 10:
        # Tolerance of +/- 10 included to account for servo value skipping
        if get_servo_position(servo_port) - desired_servo_position > 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position -= tics
        elif get_servo_position(servo_port) - desired_servo_position <= 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position += tics
        elif abs(get_servo_position(servo_port) - c.MAX_SERVO_LIMIT) < 30 or abs(get_servo_position(servo_port) - c.MIN_SERVO_LIMIT) < 30:
            break
        else:
            break
        if abs(c.CURRENT_LM_POWER - left_motor_power) > 10 and abs(c.CURRENT_RM_POWER - right_motor_power) > 10:
            create_drive_direct(int(c.CURRENT_LM_POWER), int(c.CURRENT_RM_POWER))
            c.CURRENT_LM_POWER += left_velocity_change
            c.CURRENT_RM_POWER += right_velocity_change
            msleep(1)
        elif c.CURRENT_LM_POWER != left_motor_power or c.CURRENT_RM_POWER != right_motor_power:
            c.CURRENT_LM_POWER = left_motor_power
            c.CURRENT_RM_POWER = right_motor_power
            create_drive_direct(int(c.CURRENT_LM_POWER), int(c.CURRENT_RM_POWER))
        msleep(ms)
    if c.CURRENT_LM_POWER != left_motor_power or c.CURRENT_RM_POWER != right_motor_power:
        c.CURRENT_LM_POWER = left_motor_power
        c.CURRENT_RM_POWER = right_motor_power
        create_drive_direct(int(c.CURRENT_LM_POWER), int(c.CURRENT_RM_POWER))
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
    msleep(30)
    print "Motors revved to desired speed."
    print "Desired position reached. Curent position is %d" % get_servo_position(servo_port)
    print "Completed move_servo()\n"
