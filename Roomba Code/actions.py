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
    s.wfollow_left_until_white_left_front(0)
    s.wfollow_left_until_white_left(0)
    s.wfollow_left_until_black_left_front(0)
    s.wfollow_left_until_white_left_front(0)
    s.wfollow_left_until_black_left(0)
    s.wfollow_left_until_white_left(0)
    s.align_far_cliffs()
    # Turns right and goes to top left coupler
    s.turn_right_until_rfcliff_senses_black(0)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_lfcliff_senses_black()
    g.forwards_gyro_until_black_lcliff(0)
    g.forwards_gyro_until_white_lcliff(0)
    g.forwards_gyro_until_black_lcliff()
    # Roomba at corner right now
    s.turn_right_until_lfcliff_senses_black()
    s.lfollow_lfcliff_inside_line_until_rfcliff_senses_black_pid()
    s.turn_right_until_lfcliff_senses_black()
    s.lfollow_lfcliff_until_bump_pid()
    g.backwards_gyro(100)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_rfcliff_senses_black()
    s.lfollow_rfcliff_until_lfcliff_senses_black_pid()
    m.lower_arm()
    g.turn_left_gyro(15)
    g.backwards_gyro_until_white_rcliff(0)
    g.backwards_gyro_until_black_rcliff(0)
    g.backwards_gyro_until_white_rcliff()
    #g.backwards_gyro(200)
    pick_up_coupler()


@print_function_name
def deliver_left_coupler():
    # Here, the Roomba goes to tne bottom left and bumps PVC
    #s.lfollow_rfcliff_until_lfcliff_senses_black_pid(0)
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
    s.wfollow_right_until_black_left_front(0)
    s.wfollow_right_until_black_left()
    s.align_close_cliffs()
    g.forwards_gyro_through_line_rcliff()
    s.turn_right_until_lfcliff_senses_black(0)
    s.turn_right_until_lfcliff_senses_white(0)
    s.turn_right_until_lcliff_senses_black(0)
    s.turn_right_until_lcliff_senses_white()
    # The Roomba starts delivering the left coupler.
    put_coupler_on_t()
    push_in_coupler()


@print_function_name
def get_right_coupler():
    #turns around and wall follows to bottom right box
    g.turn_right_gyro(180)
    m.lift_arm()
    s.wfollow_right_until_black_left_front(0)
    s.wfollow_right_through_line_rcliff()
    s.turn_left_until_rfcliff_senses_black(0)
    g.turn_left_gyro(5)
    #turns left and drives to middle black line to align
    g.forwards_gyro_until_white_lfcliff(0)
    g.forwards_gyro_through_line_lfcliff()
    s.align_far_fcliffs()
    s.align_far_fcliffs()
    #Drives forward until bumps PVC on top right
    #gets in position to get right coupler
    g.forwards_gyro_until_bump()
    g.backwards_gyro(100)
    g.turn_left_gyro(180)
    g.forwards_gyro_until_black_lfcliff()
    s.align_close_fcliffs()
    m.lower_arm()
    g.backwards_gyro(825)
    pick_up_coupler()
    # Grab right coupler here


@print_function_name
def get_to_magnets():
    # TODO: write skeleton of magnets code
    g.forwards_gyro_until_black_lcliff()
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
    m.lower_arm(3, 1)
    g.forwards_gyro_until_bump()
    g.backwards_gyro(15)
    g.turn_right_gyro()
    #wall follow until middle right box
    m.lift_arm(3,1)
    # Deliver second valve here.
    put_coupler_on_t()


@print_function_name
def pick_up_coupler():
    m.base_backwards(.25)
    m.lift_arm(3,1)
    m.deactivate_motors()


@print_function_name
def put_coupler_on_t():
    s.wfollow_left_until_second_depth_sensed()
    s.wfollow_left_until_second_depth_not_sensed()
    u.sd()
    s.wfollow_left(700)
    turn_right_until_depth()
    m.move_arm(765)
            
 
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
    m.base_turn_right()
    s.wait_for_depth()
    m.deactivate_motors()
        