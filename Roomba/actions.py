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
    
@print_function_name
def practice():
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.turn_right(2)
    s.forwards_until_white_lfcliff()
    s.forwards_until_black_lfcliff(0)
    s.forwards_until_white_lfcliff(0)
    s.turn_left_until_rcliff_senses_black()
    s.turn_left_until_rcliff_senses_white(0)
    s.turn_left_until_rfcliff_senses_black(0)
    u.sd()
    s.forwards_until_white_rcliff()
    s.forwards_until_black_rcliff(0)
    s.turn_left_until_rfcliff_senses_black()
    s.lfollow_rfcliff_smooth_until_rfcliff_senses_black()
        
