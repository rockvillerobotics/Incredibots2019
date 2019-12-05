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
    s.forwards_until_white_lfcliff(0)
    s.forwards_until_black_lfcliff(0)
    m.turn_left()
    s.forwards_until_black_lfcliff()
    m.forwards(500)
    s.backwards_until_black_lfcliff()
    #s.turn_left_until_lfcliff_senses_black()
    m.turn_left()
    s.lfollow_lfcliff_until_rfcliff_senses_black_pid()
    s.forwards_until_white_lfcliff()
    m.forwards(600)
    m.turn_right()
    s.forwards_until_bump()
    
        
    
    
    
   
