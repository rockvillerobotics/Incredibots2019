from wallaby import *
from decorators import *
import constants as c
import sensors as s
import movement as m
import gyro as g
import utils as u

 
@print_function_name
def first_position():
    g.forwards_gyro_until_black_rfcliff()
    g.forwards_gyro_until_white_rfcliff(0)
    g.forwards_gyro_until_black_rfcliff(0)
    #s.align_close_fcliffs()
    msleep(100)
    g.turn_left_gyro()
    g.forwards_gyro_until_black_lfcliff()
    g.forwards_gyro(700)
    g.backwards_gyro_until_black_rfcliff()
    g.turn_left_gyro()
    s.lfollow_lfcliff_until_lfcliff_senses_black_pid()
    s.forwards_gyro_until_white_lfcliff()
    g.forwards_gyro(600)
    g.turn_right_gyro()
    s.forwards_gyro_until_bump()
    
        
    
    
    
   
