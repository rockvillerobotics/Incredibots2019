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
    # Turns right and goes to top left coupler
    s.turn_right_until_rfcliff_senses_black(0)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_lfcliff_senses_black()
    m.base_forwards()
    msleep(200)
    g.forwards_gyro_until_white_lfcliff(0)
    g.forwards_gyro_through_line_lfcliff(0)
    msleep(200)
    # Roomba at corner right now
    m.base_turn_left()
    msleep(200)
    s.turn_left_until_rfcliff_senses_white()
    s.lfollow_rfcliff_until_lfcliff_senses_black_pid(0)
    s.lfollow_rfcliff_until_lfcliff_senses_white_pid()
    s.turn_right_until_rfcliff_senses_black(0)
    s.turn_right_until_rfcliff_senses_white(0)
    msleep(200)
    s.turn_right_until_lfcliff_senses_white()
    s.lfollow_lfcliff_until_bump_pid()
    g.backwards_gyro(100)
    s.turn_right_until_rfcliff_senses_white(0)
    s.turn_right_until_rfcliff_senses_black()
    s.lfollow_rfcliff_until_lfcliff_senses_black_pid()
    m.lower_arm()
    g.turn_left_gyro(18)
    g.backwards_gyro_until_item_is_in_claw(1100)
    g.backwards_gyro(100)
    pick_up_coupler()


@print_function_name
def deliver_left_coupler():
    # Here, the Roomba goes to tne bottom left and bumps PVC
    g.forwards_gyro_until_black_lcliff(0)
    g.forwards_gyro_until_bump()
    g.backwards_gyro(10)
    # Turns left and wall follows until middle right box
    g.turn_left_gyro()
    m.move_wrist(853, 3, 1)
    m.move_arm(105, 3, 1)
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
    s.turn_right_until_rfcliff_senses_black(0)
    s.turn_right_until_rfcliff_senses_white(0)
    g.turn_right_gyro(60)
    #The Roomba starts delivering the left coupler.
    put_coupler_on_t()


@print_function_name
def get_right_coupler():
    #turns around and wall follows to bottom right box
    deposit_attempts = 0
    while s.isItemInClaw() and deposit_attempts < 3:
        print "I still have the coupler. Better try and put it on again!"
        m.lift_arm()
        m.retract_wrist()
        s.wfollow_right_until_black_right_front(0)
        s.wfollow_right_until_black_right()
        s.turn_right_until_lfcliff_senses_black(0)
        s.turn_right_until_lfcliff_senses_white(0)
        g.turn_right_gyro(60)
        put_coupler_on_t()
        deposit_attempts += 1
    m.lift_arm()
    m.retract_wrist()
    s.wfollow_right_until_black_right_front(0)
    s.wfollow_right_until_black_right()
    s.turn_left_until_rfcliff_senses_black(0)
    s.turn_left_until_rfcliff_senses_white()
    #turns left and drives to middle black line to align
    g.forwards_gyro_until_white_lcliff(0)
    g.forwards_gyro_through_line_lcliff()
    #Needs to turn around to grab coupler
    s.turn_left_until_rfcliff_senses_black(0)
    g.turn_left_gyro(75)
    m.lower_arm()
    g.backwards_gyro_through_line_lcliff(0)
    g.backwards_gyro_until_white_rcliff()
    s.align_close_cliffs()
    g.backwards_gyro_until_item_is_in_claw(1400)
    pick_up_coupler()


@print_function_name
def go_to_magnets():
    # TODO: write skeleton of magnets code
    g.forwards_gyro_until_black_cliffs()
    s.align_close_cliffs()
    s.turn_left_until_rfcliff_senses_black(0)
    s.turn_left_until_rfcliff_senses_white()
    s.lfollow_rfcliff_until_bump_pid()
    g.backwards_gyro(15)


@print_function_name
def do_magnets():
    g.turn_left_gyro()
    g.backwards_gyro_until_black_lcliff()
    m.lift_micro()
    m.lift_magnet_arm()
    s.align_on_wall_right()
    s.wfollow_right_smooth_until_black_rcliff()
    g.backwards_gyro_until_white_rcliff(0)
    g.backwards_gyro(50)
    m.lower_magnet_arm()
    m.retract_micro()
    g.backwards_gyro_until_black_lfcliff()
    s.align_far_fcliffs()
    g.backwards_gyro(60)
    m.lift_micro()
    m.lift_magnet_arm()
    g.backwards_gyro(1500)
    msleep(1000)
    g.forwards_gyro(50)
    m.lower_magnet_arm()
    m.retract_micro()
    


@print_function_name
def deliver_right_coupler():
    #Turns right and drives until bumps PVC on Bottom Left
    g.turn_left_gyro(180)
    g.forwards_gyro_until_bump()
    g.backwards_gyro(15)
    g.turn_right_gyro()
    #wall follow until middle right box
    # Deliver second valve here.
    put_coupler_on_t()


@print_function_name
def pick_up_coupler():
    m.base_backwards(.3)
    m.lift_arm(3,1)
    m.deactivate_motors()


@print_function_name
def put_coupler_on_t():
    s.wfollow_left_until_second_depth(0, speed=1.0)
    s.wfollow_left(1000)
    s.wfollow_left_smooth_slowly_until_second_depth(0)
    s.wfollow_left_smooth_slowly(1200)
    s.wfollow_left_smooth_slowly_until_not_second_depth(0)
    s.wfollow_left_smooth_slowly(500)
    m.move_wrist(1376, 3, 1)
    m.move_arm(366, 3, 1)
    msleep(1000)
    u.halve_speeds()
    g.backwards_gyro(500)
    g.turn_left_gyro(50)
    u.normalize_speeds()
    u.reset_roomba()


@print_function_name
def dance_while_lowering_arm(desired_servo_position, servo_port=c.ARM_SERVO, tics=3, ms=1):
    ms_since_last_direction_change = 0
    left = 1
    right = -1
    direction = right
    intermediate_position = get_servo_position(servo_port)
    while abs(get_servo_position(servo_port) - desired_servo_position) > 10:
        # Tolerance of +/- 10 included to account for servo value skipping
        if get_servo_position(servo_port) - desired_servo_position > 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position -= tics
        elif get_servo_position(servo_port) - desired_servo_position <= 0:
            set_servo_position(servo_port, intermediate_position)
            intermediate_position += tics
        elif abs(get_servo_position(servo_port) - c.MAX_SERVO_LIMIT) < 30 or abs(get_servo_position(servo_port) - c.MIN_SERVO_LIMIT) < 30:
            break
        else:
            break
        msleep(ms)
        ms_since_last_direction_change += ms
        if ms_since_last_direction_change > 20:
            ms_since_last_direction_change = 0
            if direction == left:
                m.base_turn_right()
                direction = right
            else:
                m.base_turn_left()
                direction = left
    set_servo_position(servo_port, desired_servo_position)  # Ensures actual desired value is reached. Should be a minor point change
        


@print_function_name
def backwards_until_second_depth(time=c.SAFETY_TIME):
    u.change_speeds_by(0.25)
    g.backwards_gyro_until_second_depth(time)
    u.normalize_speeds()


@print_function_name
def turn_right_until_depth():
    m.base_turn_right(0.2)
    s.wait_for_depth()
    m.deactivate_motors()
        
        
@print_function_name
def turn_left_until_depth():
    m.base_turn_left(0.5)
    s.wait_for_depth()
    m.deactivate_motors()


@print_function_name
def turn_right_until_not_depth():
    m.base_turn_right(0.3)
    s.wait_for_not_depth()
    m.deactivate_motors()
        
        
@print_function_name
def turn_left_until_not_depth():
    m.base_turn_left(0.3)
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


@print_function_name
def test_coupler_delivery():
    g.forwards_gyro(100)
