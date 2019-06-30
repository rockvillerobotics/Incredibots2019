## The bulk of commands should go here

from wallaby import *
from decorators import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w
import gyro as g

@print_function_name
def get_ambulance():
    g.backwards_gyro_until_black_left()
    #pick up ambulance
        
@print_function_name
def get_blocks():
    g.backwards_gyro_until_black_left()
    s.align_far()
    g.backwards_gyro_through_line_left()
    g.backwards_gyro_until_black_left()
    s.align_far()
    g.turn_right_gyro(90)
    g.drive_gyro(1500, stop=False)
    g.drive_gyro_until_white_left(0)
    g.drive_gyro_through_line_left(0)
    g.drive_gyro(1000)
    s.turn_left_until_black()
    #put down big boy claw and open it
    #s.lfollow_left_until_third_senses_middle_pid()
    #m.close_claw()
    #m.lift_arm()
    #s.lfollow_left_pid(1000)
    #m.lower_arm()
    #m.open_claw()
    #s.lfollow_left_until_black_third_pid()
    #m.close_claw()
    #m.lift_arm()
    s.lfollow_left_until_black_right_pid(20000)
    
        
    
@print_function_name
def deliver_ambulance_and_blocks():
    w.check_zones_hospital()
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        g.drive_gyro_through_line_right()
        m.open_claw(1, 1)
    else:
        s.left_forwards_until_white(0)
        s.left_forwards_until_black()
        g.drive_gyro_through_line_left()
        m.open_claw(1, 1)
        
    #drop the blockz
    s.turn_right_until_black(0)
    s.turn_right_until_white(0)
    s.turn_right_until_black()
    g.backwards_gyro_through_line_left()
    #drop ambulance
        
@print_function_name
def get_firefighters():
    g.drive_gyro_through_line_left()
    s.turn_right_until_black_left()
    s.turn_right_until_white_left()
    g.turn_right_gyro(15)


@print_function_name
def deliver_firefighters():
    pass