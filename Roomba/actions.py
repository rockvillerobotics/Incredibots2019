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
    g.forwards_gyro(600)
    s.turn_left_until_lfcliff_senses_black()
    s.lfollow_lfcliff_smooth_until_rfcliff_senses_black()
    g.turn_left_gyro(6)

 @print_function_name
 def first_position():
    g.forwards_gyro_until_black_rfcliff()
    g.forwards_gyro_until_white_rfcliff()
    g.forwards_gyro_until_bump()
    m.turn_left()
    g.forwards_gyro_wall_assisted_on_right()      
    
   
