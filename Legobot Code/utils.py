from wallaby import *
import constants as c
import actions as a
import sensors as s
import movement as m

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~States~~~~~~~~~~~~~~~~~~~~~~~~

def left_pressed():
    return(left_button() == 1)

def not_left_pressed():
    return(left_button() == 0)

def right_pressed():
    return(right_button() == 1)

def not_right_pressed():
    return(right_button() == 0)

def bumped():
    return(digital(c.BUMP_SENSOR) == 1)

def not_bumped():
    return(digital(c.BUMP_SENSOR) == 0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~

def wait_for_button():
    print "Press Right Button..."
    while not_right_pressed():
        pass
    print "Right button pressed\n"
    msleep(500)


def setup():
# Enables servos and sets them to predefined starting positions. This goes before every run
    print "Starting setup()"
    if c.IS_MAIN_BOT:
        print "I am the main bot"
    elif c.IS_CLONE_BOT:
        print "I am the clone bot"
    else:
        print "Error in bot determination"
        exit(86)
    if c.STARTING_CLAW_POS > c.MAX_SERVO_POS or c.STARTING_CLAW_POS < c.MIN_SERVO_POS or c.STARTING_ARM_POS > c.MAX_SERVO_POS or c.STARTING_ARM_POS < c.MIN_SERVO_POS :
        print "Invalid desired servo position\n"
        exit(86)
    graphics_close()
    ao()
    enable_servo(c.CLAW_SERVO)
    enable_servo(c.ARM_SERVO)
    enable_servo(c.CUBE_ARM_SERVO)
    c.STARTING_ARM_POS = get_servo_position(c.ARM_SERVO)
    print "STARTING_ARM_POS now: " + str(c.ARM_DOWN_POS)
    m.move_claw(c.STARTING_CLAW_POS)
    m.move_arm(c.STARTING_ARM_POS)
    m.move_cube_arm(c.STARTING_CUBE_ARM_POS)
    msleep(1000)
    #print "Set claw to starting position of %d" % c.STARTING_CLAW_POS
    #print "Set arm to starting position of %d" % c.STARTING_ARM_POS
    #m.move_claw(c.CLAW_CHECKING_POS)
    #m.wait()
    #m.move_claw(c.STARTING_CLAW_POS)
    #m.wait()
    console_clear()
    print "Setup complete\n\n"


def calibrate():
# Code to calibrate the bw values. This goes before every run. Ends with light sensor calibration.
    max_sensor_value_right = 0
    min_sensor_value_right = 90000
    max_sensor_value_left = 0
    min_sensor_value_left = 90000
    max_sensor_value_third = 0
    min_sensor_value_third = 90000
    cmpc(c.LEFT_MOTOR)
    cmpc(c.RIGHT_MOTOR)
    if c.IS_MAIN_BOT:
        calibrate_tics = -2000
    else: # Clone bot
        calibrate_tics = -2500
    print "Running calibrate()"
    m.activate_motors(int (c.BASE_LM_POWER / 2 * -1), int(c.BASE_RM_POWER / 2 * -1))
    while gmpc(c.LEFT_MOTOR) > calibrate_tics:
        if analog(c.RIGHT_TOPHAT) > max_sensor_value_right:
            max_sensor_value_right = analog(c.RIGHT_TOPHAT)
        if analog(c.RIGHT_TOPHAT) < min_sensor_value_right:
            min_sensor_value_right = analog(c.RIGHT_TOPHAT)
        if analog(c.LEFT_TOPHAT) > max_sensor_value_left:
            max_sensor_value_left = analog(c.LEFT_TOPHAT)
        if analog(c.LEFT_TOPHAT) < min_sensor_value_left:
            min_sensor_value_left = analog(c.LEFT_TOPHAT)
        if analog(c.THIRD_TOPHAT) > max_sensor_value_third:
            max_sensor_value_third = analog(c.THIRD_TOPHAT)
        if analog(c.THIRD_TOPHAT) < min_sensor_value_third:
            min_sensor_value_third = analog(c.THIRD_TOPHAT)
        msleep(1)
    m.deactivate_motors()
    c.LEFT_TOPHAT_BW = int(((max_sensor_value_left + min_sensor_value_left) / 2)) - 1000
    c.RIGHT_TOPHAT_BW = int(((max_sensor_value_right + min_sensor_value_right) / 2)) - 1000
    if c.IS_MAIN_BOT:
        c.THIRD_TOPHAT_BW = int(((max_sensor_value_third + min_sensor_value_third) / 2)) + 1000
    else: # Clone bot
        c.THIRD_TOPHAT_BW = int(((max_sensor_value_third + min_sensor_value_third) / 2))  + 1000
    print "max_sensor_value_left: " + str(max_sensor_value_left)
    print "min_sensor_value_left: " + str(min_sensor_value_left)
    print "LEFT_TOPHAT_BW: " + str(c.LEFT_TOPHAT_BW)
    print "max_sensor_value_right: " + str(max_sensor_value_right)
    print "min_sensor_value_right: " + str(min_sensor_value_right)
    print "RIGHT_TOPHAT_BW: " + str(c.RIGHT_TOPHAT_BW)
    print "max_sensor_value_third: " + str(max_sensor_value_third)
    print "min_sensor_value_third: " + str(min_sensor_value_third)
    print "THIRD_TOPHAT_BW: " + str(c.THIRD_TOPHAT_BW)
    c.MAX_TOPHAT_VALUE_RIGHT = max_sensor_value_right
    c.MIN_TOPHAT_VALUE_RIGHT = min_sensor_value_right
    c.MAX_TOPHAT_VALUE_LEFT = max_sensor_value_left
    c.MIN_TOPHAT_VALUE_LEFT = min_sensor_value_left
    print "Finished Calibrating. Moving back into starting box...\n"
    s.drive_until_black_left()
    s.align_close()
    s.drive_through_line_third(0)
    m.drive(1050)
    msleep(25)
    ao()
    msleep(2000)
    wait_for_light(c.LIGHT_SENSOR)
    shut_down_in(118)  # URGENT: PUT BACK IN BEFORE COMPETITION


def calibrate_manually(base_time = 60):
# A calibration that requires manually pressing the button. It will print directions on how to do it correctly.
    sec = seconds() + base_time
    exit_function = False    
    print "Running calibrate_manually()"
    print "You have %d seconds until calibration ends" % base_time
    print "Press the L(eft) button to continue to third tophat calibration"
    print "Press the R(ight) button to set the tophat bw values\n"
    print "Waiting for user input...\n"
    while seconds() < sec and exit_function == False:
        if left_pressed():
            sec += 30
            print "Left button pressed. Continuing to third tophat calibration"
            print "Right tophat bw = %d for the actual code" % c.RIGHT_TOPHAT_BW
            print "Left tophat bw = %d for the actual code\n" % c.LEFT_TOPHAT_BW
            msleep(3000)
            print "Now calibrating third tophat"
            print "Press the L(eft) button to exit calibration"
            print "Press the R(ight) button to set the third tophat bw values\n"
            print "Waiting for user input...\n\n\n"
            while not_left_pressed():
                if right_pressed():
                    sec += 30
                    print "Right button pressed"
                    print "Calculating third tophat bw value...\n\n"
                    c.THIRD_TOPHAT_BW = analog(c.THIRD_TOPHAT)
                    msleep(1000)
                    print "Third tophat bw = %d now" % c.THIRD_TOPHAT_BW
            print "Left pressed"
            exit_function = True
        elif right_pressed():
            sec += 30
            print "Right button pressed"
            print "Calculating bw values...\n\n"
            c.RIGHT_TOPHAT_BW = analog(c.RIGHT_TOPHAT)
            c.LEFT_TOPHAT_BW = analog(c.LEFT_TOPHAT)
            msleep(1000)
            print "Right tophat bw = %d now" % c.RIGHT_TOPHAT_BW
            print "Left tophat bw = %d now\n" % c.LEFT_TOPHAT_BW
            print "If you are satisfied with the above bw values, press the L(eft) button"
            print "If not, press the R(ight) button again"
            print "Waiting for user input...\n"
    print "Left button pressed. Continuing to actual code.\n"
    print "Tophat bw calibration complete"
    print "To user: Now put the robot in its starting position"
    print "Starting light sensor calibration in 5 seconds"
    print " ~~~~~~~~~~~ \n\n\n"
    ao()
    msleep(5000)
    wait_for_light(c.LIGHT_SENSOR)
    shut_down_in(118)


def shutdown(value = 256):
# Shuts down code without exit by default. Will exit if number is put in parantheses.
    print "Starting shutdown()"
    mav(c.LEFT_MOTOR, 0)
    mav(c.RIGHT_MOTOR, 0)
    msleep(25)
    ao()
    disable_servos()
    graphics_close()
    print "Shutdown complete\n"
    if value < 255:
        print "Exiting...\n"
        exit(value)


def sd(value = 86):
# Shortcut to end a run early.
    shutdown(value)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Debug~~~~~~~~~~~~~~~~~~~~~~~~

def test_movement(exit = True):
# Used to see if movements and their defaults function as intended.
    print "Testing movement\n"
    m.turn_left()
    msleep(500)
    m.turn_right()
    msleep(500)
    m.drive(5000)
    msleep(500)  # Using msleep() instead of wait() to make sure each command turns off its wheels.
    m.backwards(5000)
    msleep(500)
    print "Testing complete."
    if exit == True:
        print "Exiting...\n"
        exit(86)


def test_movement_extensive(exit = True):
    print "Extensively testing movement"
    mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    msleep(c.PIVOT_RIGHT_TURN_TIME)
    mav(c.RIGHT_MOTOR,0)
    msleep(500)
    mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
    msleep(c.PIVOT_LEFT_TURN_TIME)
    mav(c.LEFT_MOTOR,0)
    msleep(500)
    m.turn_left()
    msleep(500)
    m.turn_right()
    msleep(500)
    m.drive(1000)
    msleep(500)  # Using msleep() instead of wait() to make sure each command turns off its wheels.
    m.backwards(1000)
    msleep(500)
    if exit == True:
        print "Exiting...\n"
        exit(86)


def test_servos(exit = True):
# Used to see if basic servo commands and constants function as intended.
    print "Testing servos\n"
    m.close_claw()
    m.wait()  # Using wait() instead of msleep() to make sure wheels are off.
    m.open_claw()
    m.wait()
    m.lift_arm()
    m.wait()
    m.lower_arm()
    m.wait()
    print "Testing complete."
    if exit == True:
        print "Exiting...\n"
        exit(86)


def test_servos_extensive(exit = True):  # Runs all constant servo positions for arm and claw. Not updated.
    print "Testing servos extensively\n"
    m.claw_slow(c.STARTING_CLAW_POS)
    m.arm_slow(c.STARTING_ARM_POS)
    m.wait()
    m.claw_slow(c.CLAW_OPEN_POS)
    m.wait()
    m.claw_slow(c.CLAW_CLOSE_POS)
    m.wait()
    m.claw_slow(c.CLAW_SECOND_CRATE_GRAB_POS)
    m.wait()
    m.claw_slow(c.BOTGUY_CLAW_CLOSE_POS)
    m.wait()
    m.arm_slow(c.ARM_UP_POS)
    m.wait()
    m.arm_slow(c.ARM_DOWN_POS)
    m.wait()
    m.arm_slow(c.ARM_SECOND_CRATE_UP_POS)
    m.wait()
    m.arm_slow(c.ARM_SECOND_CRATE_GRAB_POS)
    m.wait()
    m.arm_slow(c.ARM_DOWN_POS)
    m.wait()
    print "Testing complete."
    if exit == True:
        print "Exiting...\n"
        exit(86)
