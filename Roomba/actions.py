from wallaby import *
from decorators import *
import constants as c
import sensors as s
import movement as m
import gyro as g
import utils as u

@print_function_name
def first_position():
    s.forwards_until_black_lfcliff()  
    s.align_far_fcliffs()
    s.forwards_until_white_lcliff()
    s.forwards_until_black_rcliff()
    m.turn_left()
    s.forwards_until_black_lfcliff()
    m.turn_left()
