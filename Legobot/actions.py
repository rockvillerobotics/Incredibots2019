## The bulk of commands should go here

from wallaby import *
from decorators import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w
import gyro as g

@print_function_name
def get_ambulance():
    m.lift_ambulance_arm()


@print_function_name
def get_blocks():
    g.backwards_gyro_until_black_left()
    s.align_far()
    g.backwards_gyro_through_line_left(0)
    g.backwards_gyro_until_black_left()
    s.align_far()
    g.backwards_gyro_through_line_left(0)
    g.backwards_gyro(300)
    g.turn_right_gyro(90)
    g.drive_gyro(2000, should_stop=False)
    g.drive_gyro_until_white_left(0)
    g.drive_gyro_until_black_left(0)
    g.drive_gyro(500, should_stop=False)
    g.drive_gyro_until_white_left(0)
    g.drive_gyro(950)
    s.turn_left_until_black()
    m.open_claw()
    m.lower_arm()
    #s.lfollow_left_pid(13000, bias=15, should_stop=False)
    s.lfollow_left_pid_until_black_third(time=21000, bias=10)
    m.close_claw()
    g.backwards_gyro(800)
    m.lift_arm(1, 1)
    s.lfollow_left_pid_until_black_right(bias=10)


@print_function_name
def deliver_ambulance_and_blocks():
    w.check_zones_hospital()
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        g.drive_gyro_through_line_right()
        s.align_far()
        m.open_claw(1, 1, c.CLAW_WAY_OPEN_POS)
        msleep(500)
        m.move_arm(c.ARM_HIGH_POS)
        #m.move_claw(c.CLAW_WAY_OPEN_POS)
        #w.close_graphics_window()
        g.turn_left_gyro(190)
    else:
        u.halve_speeds()
        g.drive_gyro_through_line_right()
        s.align_far()
        s.left_forwards_until_white(0)
        s.left_forwards_until_black()
        m.open_claw(1, 1, c.CLAW_WAY_OPEN_POS)
        msleep(500)
        m.move_arm(c.ARM_HIGH_POS)
        #m.move_claw(c.CLAW_WAY_OPEN_POS)
        u.normalize_speeds()
        #w.close_graphics_window()
        u.sd()
        g.turn_left_gyro(190)
    g.backwards_gyro_through_line_left(1100)
    m.lower_ambulance_arm()
    g.backwards_gyro(500)
    

@print_function_name
def get_firefighters():
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        g.drive_gyro_until_black_left()
        m.lift_ambulance_arm()
        g.drive_gyro_through_line_left()

    else:
        g.drive_gyro_until_black_left()
        m.lift_ambulance_arm()
        g.drive_gyro_through_line_left()
        s.lfollow_right_pid_until_black_left(bias=15)
        s.turn_right_until_black(0)
        s.turn_right_until_white()
        m.lower_arm()
    g.drive_gyro_through_line_left()
    s.turn_right_until_black_left()
    s.turn_right_until_white_left()
    g.turn_right_gyro(15)


@print_function_name
def deliver_firefighters():
    pass
