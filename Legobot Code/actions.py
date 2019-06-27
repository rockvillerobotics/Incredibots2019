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
def get_ambulance_and_blocks():
    g.drive_gyro_through_line_left()
    s.align_far()
    g.drive_gyro_until_black_third()
    s.turn_left_until_black(0)
    s.turn_left_until_white()
    g.drive_gyro_until_white_third(0)
    g.drive_gyro_through_line_third()
    s.turn_left_until_black()
    s.lfollow_left_until_right_senses_black_pid(0)
    g.drive_through_line_right()
    s.align_far()
    w.check_zones_hospital()


@print_function_name
def deliver_ambulance_and_blocks():
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        m.lift_arm()
        # move forward a certain amount
        m.open_claw()

    else:
        m.lift_arm()
        s.left_forwards_until_white(should_stop=False)
        s.left_forwards_until_black(should_stop=False)
        s.left_forwards_until_white()
        g.drive_gyro_through_line_third()
        # move forward a certain amount
        m.open_claw()

@print_function_name
def get_firefighters():
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        g.backwards_gyro_through_line_right()
        s.right_forwards_until_black(should_stop=False)
        s.right_forwards_until_white()


    else:
        g.backwards_gyro_through_line_left(should_stop=False)
        g.backwards_gyro_until_black_left(should_stop=False)
        g.backwards_gyro(50)
        s.turn_left_until_white(should_stop=False)
        s.turn_left_until_black(should_stop=False)
        s.turn_left_until_black_right(should_stop=False)
        s.turn_left_until_white_right()


"""
@print_function_name
def get_ambulance_and_blocks():
    g.drive_gyro_through_line_right()
    s.align_far()
    g.drive_gyro_until_white_right(should_stop=False)
    g.drive_gyro_until_black_right()
    s.align_close()
    g.drive_gyro_until_black_third(should_stop=False)
    g.drive_gyro(100)
    # Some cheeky maneuvers are done here to ensure that we get out of the starting box 100% of the time.
    g.turn_left_gyro()
    m.move_windshield_wiper(c.WINDSHIELD_WIPER_MIDDLE_POS)
    g.drive_gyro_until_white_left(should_stop=False)
    g.drive_gyro_through_line_left(should_stop=False)
    g.drive_gyro_through_line_third()
    s.turn_left_until_black()
    s.lfollow_left_until_black_right_pid(should_stop=False)
    g.drive_gyro_through_line_right()
    # We're aligned on the T near the hospital zones. We're just about ready to sense the hospital zones.
    s.align_far()
    m.swipe_right_windshield_wiper()
    w.check_zones_hospital()


def deliver_ambulance_and_blocks():
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        g.drive_gyro_through_line_third()

    else:
        s.left_forwards_until_white(should_stop=False)
        s.left_forwards_until_black(should_stop=False)
        s.left_forwards_until_white()
        g.drive_gyro_until_black_third(should_stop=False)
        g.drive_gyro(200)


@print_function_name
def get_firefighters():
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        g.backwards_gyro_through_line_right()
        m.swipe_left_windshield_wiper()
        s.right_forwards_until_black(should_stop=False)
        s.right_forwards_until_white()
        go_to_firefighters()
        wipe_firefighters()


    else:
        g.backwards_gyro_through_line_left(should_stop=False)
        g.backwards_gyro_until_black_left(should_stop=False)
        g.backwards_gyro(50)
        m.swipe_left_windshield_wiper()
        s.turn_left_until_white(should_stop=False)
        s.turn_left_until_black(should_stop=False)
        s.turn_left_until_black_right(should_stop=False)
        s.turn_left_until_white_right()
        go_to_firefighters()
        wipe_firefighters()


@print_function_name
def go_to_firefighters():
    g.drive_gyro_until_black_fourth(should_stop=False)
    g.drive_gyro_until_white_fourth(should_stop=False)
    g.drive_gyro_until_black_right_or_fourth()
    if s.isFourthOnBlack():
        print "\n\nOnly Fourth is on black.\n\n"
        g.drive_gyro(100)
        s.turn_right_until_black_left()
        g.drive_gyro_until_black_third()

    elif s.isLeftOnBlack():
        print "\n\nLeft sensor is on black. Clearly its angled the the left a bit.\n\n"
        g.drive_gyro_through_line_right()
        s.turn_left_until_black(should_stop=False)
        s.turn_left_until_white()
        g.drive_gyro_until_black_third()
        s.turn_right_until_white(should_stop=False)

    else:
        print "\n\nRight sensor is on black but Left sensor is not.\n\n"
        g.drive_gyro_through_line_fourth()
        s.turn_right_until_black_left()
        g.drive_gyro_until_black_third()
        s.turn_right_until_white(should_stop=False)
    s.turn_right_until_black(should_stop=False)
    s.turn_right_until_white()
    s.lfollow_right_inside_line_until_black_third_pid()


@print_function_name
def deliver_firefighters():
    g.backwards_gyro_through_line_left()
    s.align_close()
    g.turn_right_gyro(85)
    g.drive_gyro_until_white_left(should_stop=False)
    g.drive_gyro_until_black_left()
    s.turn_right_until_left_senses_white()
    s.lfollow_left_until_third_senses_black_pid(should_stop=False)
    s.lfollow_left_until_third_senses_white_pid()
    # Now the robot is in front of the near zone hospital. The firefighters need to go to the burning hospital.
    if c.BURNING_HOSPITAL == c.NEAR_ZONE:
        g.turn_left_gyro()
        g.drive_gyro_through_line_third()


    else:
        s.right_forwards_until_black()
        g.drive_gyro_until_black_third(should_stop=False)
        g.drive_gyro(50)
        g.backwards_gyro_until_black_left()
        s.turn_left_until_black(0)
        s.turn_left_until_white()



@print_function_name
def wipe_firefighters():
    swipes = 0
    left_pos = c.WINDSHIELD_WIPER_LEFT_POS
    right_pos = c.WINDSHIELD_WIPER_RIGHT_POS
    while swipes < 7:
        # Swipes left on even rotations and swipes right on odd.
        if swipes % 2 == 0:
            m.swipe_left_windshield_wiper(3, 1, left_pos)
            s.turn_left_until_black_right()
            left_pos += 50
        else:
            m.swipe_right_windshield_wiper(3, 1, right_pos)
            s.turn_right_until_black_left()
            right_pos -= 50
        swipes += 1
"""