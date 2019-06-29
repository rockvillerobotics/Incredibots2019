from wallaby import *
from decorators import *
import constants as c
import sensors as s
import movement as m
import gyro as g
import utils as u

@print_function_name
def get_left_coupler():
    # Gets to the bottom left square
    s.wfollow_left_until_black_left_front(0)
    s.wfollow_left_until_black_left(0)
    s.align_on_wall_left()
    s.wfollow_left_smooth_until_white_lfcliff(0)
    s.wfollow_left_smooth_until_white_lcliff(0)
    s.wfollow_left_smooth_until_black_lfcliff(0)
    s.wfollow_left_smooth_until_white_lfcliff(0)
    s.wfollow_left_until_black_left(0)
    s.wfollow_left_until_white_left()
    s.right_forwards_until_rcliff_senses_black()
    s.align_far_cliffs()
    # Turns right and goes to top left coupler
    s.turn_right_until_rfcliff_senses_black(0)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_lfcliff_senses_black()
    g.forwards_gyro_until_black_lcliff(0)
    g.forwards_gyro_until_white_lcliff(0)
    g.forwards_gyro_until_black_lcliff()
    # Roomba at corner right now
    s.turn_right_until_rfcliff_senses_black()
    s.lfollow_rfcliff_until_lfcliff_senses_black_pid()
    s.turn_right_until_rfcliff_senses_black(0)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_lfcliff_senses_black(0)
    s.turn_right_until_lfcliff_senses_white()
    s.lfollow_lfcliff_until_bump_pid()
    g.backwards_gyro(100)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_rfcliff_senses_black()
    s.lfollow_rfcliff_until_lfcliff_senses_black_pid()
    m.lower_arm()
    g.turn_left_gyro(20)
    g.backwards_gyro_until_pressed_bump_switch(1000)
    pick_up_coupler()


@print_function_name
def deliver_left_coupler():
    # Here, the Roomba goes to tne bottom left and bumps PVC
    g.forwards_gyro_until_black_lcliff(0)
    g.forwards_gyro_until_bump()
    g.backwards_gyro(10)
    # Turns left and wall follows until middle right box
    g.turn_left_gyro()
    s.wfollow_right_until_black_left(0)
    s.wfollow_right_until_white_left_front(0)
    s.wfollow_right_until_white_left(0)
    s.wfollow_right_until_black_left_front(0)
    s.wfollow_right_until_black_left(0)
    #gets in position to deliver 1st coupler.
    s.align_on_wall_right()
    s.wfollow_right_smooth_until_black_lfcliff(0)
    s.wfollow_right_smooth_until_black_rcliff()
    # Next to T
    s.turn_right_until_lfcliff_senses_black(0)
    s.turn_right_until_lfcliff_senses_white(0)
    g.turn_right_gyro(60)
    # The Roomba starts delivering the left coupler.
    put_coupler_on_t()
    push_in_coupler()
    if s.isBumpSwitchPressed():
        print "I still have the coupler. Better try and put it on again!"
        m.lift_arm()
        g.turn_left_gyro(20)
        g.backwards_gyro(2000)
        put_coupler_on_t()
        push_in_coupler()


@print_function_name
def get_right_coupler():
    #turns around and wall follows to bottom right box
    g.turn_right_gyro(180)
    m.lift_arm()
    s.wfollow_right_until_black_right_front(0)
    s.wfollow_right_until_black_right()
    s.turn_left_until_rfcliff_senses_black(0)
    s.turn_left_until_rfcliff_senses_white()
    #g.turn_left_gyro(10)
    #turns left and drives to middle black line to align
    g.forwards_gyro_until_white_lcliff(0)
    g.forwards_gyro_through_line_lcliff()
    # Needs to turn around to grab coupler
    s.turn_left_until_rfcliff_senses_black(0)
    g.turn_left_gyro(75)
    m.lower_arm()
    g.backwards_gyro_through_line_lcliff(0)
    g.backwards_gyro_until_white_rcliff()
    s.align_close_cliffs()
    g.backwards_gyro_until_pressed_bump_switch(1300)
    pick_up_coupler()
    # Grab right coupler here


@print_function_name
def go_to_magnets():
    # TODO: write skeleton of magnets code
    g.forwards_gyro_until_black_cliffs()
    s.align_close_cliffs()
    s.turn_left_until_rfcliff_senses_black(0)
    s.turn_left_until_rfcliff_senses_white()
    s.lfollow_rfcliff_until_bump_pid()
    g.backwards_gyro(400)


def do_magnets():
    msleep(2000)


@print_function_name
def deliver_right_coupler():
    #Turns right and drives until bumps PVC on Bottom Left
    g.turn_right_gyro()
    g.forwards_gyro_until_bump()
    g.backwards_gyro(15)
    g.turn_right_gyro()
    #wall follow until middle right box
    # Deliver second valve here.
    put_coupler_on_t()


@print_function_name
def pick_up_coupler():
    m.base_backwards(.25)
    m.lift_arm(3,1)
    m.deactivate_motors()


@print_function_name
def put_coupler_on_t():
    s.wfollow_left_smooth_slowly_until_second_depth(0, speed=1)
    s.wfollow_left(800)
    s.wfollow_left_smooth_slowly_until_second_depth(0)
    s.wfollow_left_smooth_slowly_until_not_second_depth()
    #m.move_arm(1300)
    turn_right_until_depth()
    #turn_right_until_not_depth()
    #g.forwards_gyro(10)
    m.move_arm(c.ARM_JUST_BARELY_ON_T_POS)
            
 
@print_function_name           
def push_in_coupler():
    m.base_forwards(.8)
    m.move_arm(558, 5, 1)
    m.deactivate_motors()
    msleep(500)
    g.backwards_gyro(300)
    msleep(500)
    m.move_arm(700, 10, 1)
    msleep(500)
    m.lower_arm(17, 1)
    g.turn_left_gyro(5)
    u.reset_roomba(2000)
        

@print_function_name
def backwards_until_second_depth(time=c.SAFETY_TIME):
    u.change_speeds_by(0.25)
    g.backwards_gyro_until_second_depth(time)
    u.normalize_speeds()


@print_function_name
def turn_right_until_depth():
    m.base_turn_right(0.5)
    s.wait_for_depth()
    m.deactivate_motors()


@print_function_name
def turn_right_until_not_depth():
    m.base_turn_right(0.3)
    s.wait_for_not_depth()
    m.deactivate_motors()


@print_function_name
def turn_left_until_depth(should_stop=True, depth_cf=c.DEPTH_CF):
    m.base_turn_left(0.3)
    full_depth_cf = c.DEPTH_CF
    c.DEPTH_CF = depth_cf
    s.wait_for_depth()
    c.DEPTH_CF = full_depth_cf
    if should_stop:
        m.deactivate_motors()


@print_function_name
def turn_left_until_not_depth(should_stop=True, depth_cf=c.DEPTH_CF):
    m.base_turn_left(0.5)
    full_depth_cf = c.DEPTH_CF
    c.DEPTH_CF = depth_cf
    s.wait_for_not_depth()
    c.DEPTH_CF = full_depth_cf
    if should_stop:
        m.deactivate_motors()
        