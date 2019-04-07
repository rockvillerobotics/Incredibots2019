## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w

def deliver_ambulance():
    print "Starting deliver_ambulance()"
    s.backwards_through_line_third()
    m.lift_arm()
    s.drive_until_black_third()
    s.turn_right_until_black()
    s.backwards_through_line_third(0)
    s.backwards_until_black_right()
    m.move_claw(c.CLAW_LESS_OPEN_POS)
    m.lower_cube_arm()
    m.open_claw()
    s.drive_through_line_third(0)
    s.drive_until_black_left()
    m.backwards(100)
    m.close_claw()
    m.move_cube_arm(c.CUBE_ARM_HOLDING_POS)
    m.move_claw(c.CLAW_LESS_OPEN_POS)
    #m.move_cube_arm(c.CUBE_ARM_UP_POS)
    m.turn_left(int(c.RIGHT_TURN_TIME/1.5))
    s.backwards_through_line_left(0)
    s.backwards_through_line_third()
    s.turn_right_until_left_senses_black(0)
    s.turn_right_until_left_senses_white()
    s.lfollow_left_until_right_senses_black_pid_cheeky()
    #s.lfollow_left_until_right_senses_black(1000)
    #s.lfollow_left_until_right_senses_black_smooth()
    s.turn_right_until_white(0)
    s.turn_right_until_black()
    m.lower_arm()
    w.check_zones_hospital()
    m.lift_arm()
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.backwards_through_line_third()
        m.lower_arm()
        m.backwards(500)
        s.drive_until_black_third()
        m.lift_arm()
    else:  # Safe hospital is far zone
        s.backwards_through_line_third()
        s.turn_right_until_left_senses_black(0)
        m.turn_right(c.RIGHT_TURN_TIME / 9)
        s.backwards_until_white_third(0)
        s.backwards_through_line_third(0)
        m.backwards(100)
        m.lower_arm()
        # Ambulance delivered
        s.drive_through_line_third()
        m.lift_arm()
        s.turn_right_until_left_senses_black(0)
        s.turn_right_until_left_senses_white()
    print "Finished delivering ambulance and yellow cube."


def get_prism():
    print "Starting get_prism()"
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.turn_right_until_left_senses_white(0)
        s.turn_right_until_left_senses_black(0)
        s.turn_right_until_black(0)
        s.turn_right_until_left_senses_white(0)
        s.turn_right_until_left_senses_black(0)
        s.turn_right_until_left_senses_white()
        s.lfollow_left_until_right_senses_black_smooth(0)
        s.drive_through_line_right()
        s.align_far()
        m.move_claw(c.CLAW_LESS_OPEN_POS)
        m.lower_cube_arm()
        m.open_claw()
        s.drive_until_white_right(0)
        s.drive_until_black_right(5000)
        m.move_claw(c.CLAW_TRUCK_CLOSE_POS)
        m.lift_cube_arm()
    else:  # Safe hospital is far zone
        s.lfollow_left_until_right_senses_black_smooth()
        m.move_claw(c.CLAW_LESS_OPEN_POS)
        m.lower_cube_arm()
        m.open_claw()
        s.drive_through_line_right(0)
        s.drive_until_black_right(7000)
        m.move_claw(c.CLAW_TRUCK_CLOSE_POS)
        m.lift_cube_arm()
    print "Finished getting yellow prism."


def deliver_prism_and_cube():
    print "Starting deliver_prism_and_cube()"
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.lfollow_right_until_left_senses_black_smooth(5000) 
        s.drive_through_line_left(5000)
        m.turn_left(100)
        m.lower_cube_arm()
        m.move_claw(c.CLAW_LESS_OPEN_POS)
        # Fire Truck delivered.
        m.move_cube_arm(c.CUBE_ARM_HOLDING_POS)
        m.close_claw()
        m.move_cube_arm(c.CUBE_ARM_LESS_UP_POS)
        m.move_claw(c.CLAW_LESS_OPEN_POS)
    else:  # Safe hospital is far zone
        s.align_close()
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        m.turn_left(50)
        m.lower_cube_arm()
        m.move_claw(c.CLAW_LESS_OPEN_POS)
        # Fire Truck is delivered.
        m.move_cube_arm(c.CUBE_ARM_HOLDING_POS)
        m.close_claw()
        m.move_cube_arm(c.CUBE_ARM_LESS_UP_POS)
        m.move_claw(c.CLAW_LESS_OPEN_POS)
    print "Finished delivering yellow prism and yellow cube."
    