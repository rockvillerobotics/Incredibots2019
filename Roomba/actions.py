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
    msleep(100)
    g.turn_left_gyro()
    g.forwards_gyro_until_black_lfcliff()
    g.forwards_gyro(500)
    g.turn_left_gyro(60)
    s.lfollow_lfcliff_until_rfcliff_senses_black_pid()
    g.turn_left_gyro(6)
    
    
    
   
