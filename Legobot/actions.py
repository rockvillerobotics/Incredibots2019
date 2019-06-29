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
    s.backwards_through_line_third()
    #pick up ambulance
        
@print_function_name
def get_blocks():
    s.backwards_until_back_left()
    s.align_far()
    g.turn_right_gyro(90)
    s.drive_through_line_left()
    s.drive_through_line_third()
    s.turn_left_until_black()
    #put down big boy claw and open it
    s.lfollow_left_until_black_right_pid()
    
@print_function_name
def place_ambulance_and_blocks():
    w.check_zones_hospital()
    #drop the blockz
    g.turn_left_gyro(180)
    #drop ambulank
        
@print_function_name
def get_firefighters():
    pass
