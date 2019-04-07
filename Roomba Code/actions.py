from wallaby import *
import constants as c
import sensors as s
import movement as m
import gyro as g
import utils as u

def nuclearfusion():
    s.wfollow_left_until_black_right_front()


def get_gas_valve():
    s.wfollow_right_until_black_left_front()
    s.wfollow_right_until_white_left_front()
    s.wfollow_right_until_black_left_front()
    s.wfollow_right_until_black_right()
    s.wfollow_right_until_white_right()
    s.turn_left_until_rfcliff_senses_white()
    s.turn_left_until_rfcliff_senses_black()
    m.turn_left(c.LEFT_TURN_TIME / 4.8)
    # This turns the robot closer to 90 degrees
    s.forwards_until_white_lfcliff()
    s.forwards_through_line_lfcliff()
    s.align_far_fcliffs()
    s.align_far_fcliffs()
    s.forwards_until_bump()
    m.backwards(1000)
    #g.turn_left_gyro(180)
    m.turn_left()
    m.turn_left()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()    
    s.align_close_fcliffs()
    #m.turn_left(250)    
    m.lower_arm()
    msleep(500)
    m.backwards(900)
    m.lift_arm(3, 1, c.ARM_HALF_UP_POS)
    m.backwards(300)
    m.lift_arm()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()    
    s.forwards_until_bump()
    m.backwards(100)
    #g.turn_right_gyro()
    m.turn_right(c.RIGHT_TURN_TIME / 1.2)
    s.wfollow_left_until_white_right_front(9999)
    s.wfollow_left_until_black_right_front(9999)
    s.wfollow_left_until_white_right_front(9999)
    s.align_far_fcliffs()
    s.align_far_fcliffs()
    m.backwards(500)
    #g.turn_right_gyro(30)
    m.turn_right(c.RIGHT_TURN_TIME / 3.5 )
    m.backwards(400)
    m.lower_arm(1, 1, c.ARM_DELIVERY_POS)
    shut_down_in(118)

def magnet():
    m.turn_left()
    s.forwards_until_black_rfcliff_safe()
    s.forwards_until_white_rfcliff_safe()
    s.forwards_until_black_rfcliff_safe()
    s.align_close_fcliffs()    
    m.turn_right()
    s.align_close_fcliffs()    
    m.turn_right()
    s.lfollow_lfcliff_smooth_until_bump()
