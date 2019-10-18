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
    s.align_close_fcliffs()
    m.turn_right(3)
    s.forwards_until_white_lfcliff()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.turn_left()
    s.forwards_until_black_lfcliff()
    m.forwards(500)
    s.turn_left_until_lfcliff_senses_black()
    s.lfollow_lfcliff_smooth_until_rfcliff_senses_black()
    s.forwards_until_white_lfcliff()
    m.forwards(600)
    m.turn_right()
    s.forwards_until_bump()
    
         
