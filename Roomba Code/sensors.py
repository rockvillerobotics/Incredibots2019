from wallaby import *
import constants as c
import movement as m

#---------------------------------------------States-------------------------------------------

def BlackLeft():
    return(get_create_lcliff_amt() < c.LCLIFF_BW)


def NotBlackLeft():
    return(get_create_lcliff_amt() > c.LCLIFF_BW)


def BlackRight():
    return(get_create_rcliff_amt() < c.RCLIFF_BW)


def NotBlackRight():
    return(get_create_rcliff_amt() > c.RCLIFF_BW)


def BlackFrontLeft():
    return(get_create_lfcliff_amt() < c.LFCLIFF_BW)


def NotBlackFrontLeft():
    return(get_create_lfcliff_amt() > c.LFCLIFF_BW)


def BlackFrontRight():
    return(get_create_rfcliff_amt() < c.RFCLIFF_BW)


def NotBlackFrontRight():
    return(get_create_rfcliff_amt() > c.RFCLIFF_BW)


def BumpedLeft():
    return(get_create_lbump() == 1)


def BumpedLightLeft():
    return(get_create_lclightbump() == 1)

        
def BumpedLightFrontLeft():
    return(get_create_lflightbump() == 1)
 
       
def BumpedLightFrontRight():
    return(get_create_rflightbump() == 1)


def NotBumpedLeft():
    return(get_create_lbump() == 0)


def BumpedRight():
    return(get_create_rbump() == 1)


def BumpedLightRight():
    return(get_create_rclightbump() == 1)


def NotBumpedRight():
    return(get_create_rbump() == 0)


def DepthSensesObject():
    return(analog(c.DEPTH_SENSOR) > c.DEPTH_CF)


def NotDepthSensesObject():
    return(analog(c.DEPTH_SENSOR) < c.DEPTH_CF)


def RightDepthSensesObject():
    return(analog(c.RIGHT_DEPTH_SENSOR) > c.RIGHT_DEPTH_CF)


def NotRightDepthSensesObject():
    return(analog(c.RIGHT_DEPTH_SENSOR) < c.RIGHT_DEPTH_CF)

#---------------------------------------------Driving Sensor Functions-------------------------------------------

def forwards_until_black_lcliff():
    print "Start drive_until_black_lcliff"
    m.base_forwards()
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def forwards_until_white_lcliff():
    print "Start forwards_until_white_lcliff"
    m.base_forwards()
    while BlackLeft():
        pass
    m.deactivate_motors()


def forwards_until_black_rcliff():
    print "Start drive_until_black_rcliff"
    m.base_forwards()
    while NotBlackRight():
        pass
    m.deactivate_motors()


def forwards_until_white_rcliff():
    print "Start drive_until_black_rcliff"
    m.base_forwards()
    while BlackRight():
        pass
    m.deactivate_motors()


def forwards_until_black_lfcliff():
    print "Start forwards_until_black_lfcliff"
    m.base_forwards()
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def forwards_until_white_lfcliff():
    print "Start forwards_until_white_lfcliff"
    m.base_forwards()
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def forwards_until_black_rfcliff():
    print "Start forwards_until_black_rfcliff"
    m.base_forwards()
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def forwards_until_white_rfcliff():
    print "Start forwards_until_white_rfcliff"
    m.base_forwards()
    while BlackFrontRight():
        pass
    m.deactivate_motors()


def backwards_until_black_lcliff():
    print "Start drive_until_black_lcliff"
    m.base_backwards()
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def backwards_until_white_lcliff():
    print "Start drive_until_black_lcliff"
    m.base_backwards()
    while BlackLeft():
        pass
    m.deactivate_motors()


def backwards_until_black_rcliff():
    print "Start drive_until_black_rcliff"
    m.base_backwards()
    while NotBlackRight():
        pass
    m.deactivate_motors()


def backwards_until_white_rcliff():
    print "Start drive_until_black_rcliff"
    m.base_backwards()
    while BlackRight():
        pass
    m.deactivate_motors()


def backwards_until_black_lfcliff():
    print "Start drive_until_black_lfcliff"
    m.base_backwards()
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def backwards_until_white_lfcliff():
    print "Start backwards_until_white_lfcliff"
    m.base_backwards()
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def backwards_until_black_rfcliff():
    print "Start backwards_until_black_rfcliff"
    m.base_backwards()
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def backwards_until_white_rfcliff():
    print "Start backwards_until_white_rfcliff"
    m.base_backwards()
    while BlackFrontRight():
        pass
    m.deactivate_motors()


def forwards_until_black_cliffs():
#  Goes forwards until both sensors have sensed black.
    print "Starting forwards_until_black_cliffs()"
    m.base_forwards()
    while NotBlackLeft() and NotBlackRight():
        pass
    if BlackLeft():
        while NotBlackRight():
            pass
    else:
        while NotBlackLeft():
            pass
    m.deactivate_motors()


def forwards_until_black_fcliffs():
    print "Starting forwards_until_black_fcliffs()"
    m.base_forwards()
    while NotBlackFrontLeft() and NotBlackFrontRight():
        pass
    if BlackFrontLeft():
        while NotBlackFrontRight():
            pass
    else:
        while NotBlackFrontLeft():
            pass
    m.deactivate_motors()


def backwards_until_black_cliffs():
#  Goes backwards until both sensors have sensed black.
    print "Starting backwards_until_black_cliffs()"
    m.base_backwards()
    while NotBlackLeft() and NotBlackRight():
        pass
    m.deactivate_motors()


def backwards_until_black_fcliffs():
    print "Starting backwards_until_black_fcliffs()"
    m.base_backwards()
    while NotBlackFrontLeft() and NotBlackFrontRight():
        pass
    if BlackFrontLeft():
        while NotBlackFrontRight():
            pass
    else:
        while NotBlackFrontLeft():
            pass
    m.deactivate_motors()


def forwards_through_line_lcliff():
    forwards_until_black_lcliff()
    forwards_until_white_lcliff()


def forwards_through_line_rcliff():
    forwards_until_black_rcliff()
    forwards_until_white_rcliff()


def forwards_through_line_lfcliff():
    forwards_until_black_lfcliff()
    forwards_until_white_lfcliff()


def forwards_through_line_rfcliff():
    forwards_until_black_rcliff()
    forwards_until_white_rfcliff()


def backwards_through_line_lcliff():
    backwards_until_black_lcliff()
    backwards_until_white_lcliff()


def backwards_through_line_rcliff():
    backwards_until_black_rcliff()
    backwards_until_white_rcliff()


def backwards_through_line_lfcliff():
    backwards_until_black_lfcliff()
    backwards_until_white_lfcliff()


def backwards_through_line_rfcliff():
    backwards_until_black_rfcliff()
    backwards_until_white_rfcliff()

#---------------------------------------------Line Follow Functions-------------------------------------------

def lfollow_left(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):  # Line follow with the left cliff for time
    print "Starting lfollow_left()\n"
    sec = seconds() + time
    while seconds() < sec:
        if BlackLeft():
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackLeft():
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        msleep(refresh_rate)
    deactivate_motors()


def lfollow_left_front(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):  # Line follow with the left cliff for time
    print "Starting lfollow_left()\n"
    sec = seconds() + time
    while seconds() < sec:
        if BlackFrontLeft():
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackFrontLeft():
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        msleep(refresh_rate)
    deactivate_motors()


def lfollow_left_inside_line(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    sec = seconds() + time
    while seconds() < sec:
        if BlackLeft():
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
        else:
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    deactivate_motors()


def lfollow_right(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):  # Line follow with the right cliff for time
    print "Starting lfollow_right()\n"
    sec = seconds() + time
    while seconds() < sec:
        if BlackRight():
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
        elif not BlackRight():
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
        msleep(refresh_rate)
    deactivate_motors()


def lfollow_lfcliff_smooth_until_rfcliff_senses_black():
    print "Starting lfollow_lfcliff_smooth_until_rfcliff_senses_black()"
    while NotBlackFrontRight():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)


def lfollow_lfcliff_smooth(time):
    print "Starting lfollow_lfcliff_smooth_until_rfcliff_senses_black()"
    sec = seconds() + time
    while seconds() < sec:
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)

def lfollow_lfcliff_smooth_until_rfcliff_senses_white():
    print "Starting lfollow_lfcliff_smooth_until_rfcliff_senses_white()"
    while BlackFrontRight():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)

#---------------------------------------------Depth Functions-------------------------------------------

def backwards_until_depth():
    m.base_backwards()
    while NotDepthSensesObject():
        pass
    m.deactivate_motors()


def backwards_until_not_depth():
    m.base_backwards()
    while DepthSensesObject():
        pass
    m.deactivate_motors()


def forwards_until_depth():
    m.base_forwards()
    while NotDepthSensesObject():
        pass
    m.deactivate_motors()


def lfollow_lfcliff_smooth_until_depth():
    print "Starting lfollow_lfcliff_smooth_until_rfcliff_senses_black()"
    while NotDepthSensesObject():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)


def wait_for_depth(time=15):
    print "Starting wait_for_depth()"
    sec = seconds() + time
    while NotRightDepthSensesObject() and seconds() < sec:
        pass


def wait_for_not_depth(time=7):
    print "Starting wait_for_empty()"
    sec = seconds() + time
    while RightDepthSensesObject() and seconds() < sec:
        pass

#----------------------------------------------Bump-------------------------------------------

def forwards_until_bump():
    print "Starting forwards_until_bump()"
    m.base_forwards()
    while NotBumpedLeft() and NotBumpedRight():
        pass
    m.deactivate_motors()


def wfollow_left(time, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_left()"
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BumpedLeft() or BumpedLightLeft() or BumpedLightFrontLeft():
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6))
        else:
            m.activate_motors(int(c.LFOLLOW_SMOOTH_LM_POWER * 0.5), c.BASE_RM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()

def wfollow_left_until_black_right_front(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_left_until_black_right_front()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackFrontRight():  
        if BumpedLeft() or BumpedLightLeft() or BumpedLightFrontLeft():
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6))
        else:
            m.activate_motors(int(c.LFOLLOW_SMOOTH_LM_POWER * 0.5), c.BASE_RM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()



def wfollow_left_until_white_right_front(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_left_until_white_right_front()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackFrontRight():  
        if BumpedLeft() or BumpedLightLeft() or BumpedLightFrontLeft():
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6))
        else:
            m.activate_motors(int(c.LFOLLOW_SMOOTH_LM_POWER * 0.5), c.BASE_RM_POWER)
        msleep(refresh_rate)
    m.deactivate_motors()

    
def wfollow_right_until_black_left_front(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_right_until_black_left_front()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackFrontLeft():  
        if BumpedRight() or BumpedLightRight() or BumpedLightFrontRight():
            m.activate_motors(int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6), c.BASE_RM_POWER)
        else:
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.5))
        msleep(refresh_rate)
    m.deactivate_motors() 


def wfollow_right_until_white_left_front(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_right_until_white_left_front()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackFrontLeft():  
        if BumpedRight() or BumpedLightRight() or BumpedLightFrontRight():
            m.activate_motors(int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6), c.BASE_RM_POWER)
        else:
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.5))
        msleep(refresh_rate)
    m.deactivate_motors()  


def wfollow_right_until_black_left(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_right_until_black_left()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():  
        if BumpedRight() or BumpedLightRight() or BumpedLightFrontRight():
            m.activate_motors(int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6), c.BASE_RM_POWER)
        else:
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.5))
        msleep(refresh_rate)
    m.deactivate_motors()


def wfollow_right_until_white_left(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_right_until_white_left()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():  
        if BumpedRight() or BumpedLightRight() or BumpedLightFrontRight():
            m.activate_motors(int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6), c.BASE_RM_POWER)
        else:
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.5))
        msleep(refresh_rate)
    m.deactivate_motors() 



def wfollow_right_until_black_right(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_right_until_black_right()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():  
        if BumpedRight() or BumpedLightRight() or BumpedLightFrontRight():
            m.activate_motors(int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6), c.BASE_RM_POWER)
        else:
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.5))
        msleep(refresh_rate)
    m.deactivate_motors()


def wfollow_right_until_white_right(time=15000, refresh_rate=c.LFOLLOW_REFRESH_RATE):
    print "Starting wfollow_right_until_white_right()"
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():  
        if BumpedRight() or BumpedLightRight() or BumpedLightFrontRight():
            m.activate_motors(int(c.LFOLLOW_SMOOTH_RM_POWER * 0.6), c.BASE_RM_POWER)
        else:
            m.activate_motors(c.BASE_LM_POWER, int(c.LFOLLOW_SMOOTH_RM_POWER * 0.5))
        msleep(refresh_rate)
    m.deactivate_motors() 


       
#----------------------------------------------Align Functions-------------------------------------------

def align_close_fcliffs():
    left_front_forwards_until_black()
    right_front_forwards_until_black()
    left_front_backwards_until_white()
    right_front_backwards_until_white()


def align_far_fcliffs():
    left_front_forwards_until_white()
    right_front_forwards_until_white()
    left_front_backwards_until_black()
    right_front_backwards_until_black()


def align_close_cliffs():
    left_backwards_until_lcliff_senses_white()
    right_backwards_until_rcliff_senses_white()
    left_forwards_until_lcliff_senses_black()
    right_forwards_until_rcliff_senses_black()


def align_far_cliffs():
    left_forwards_until_lcliff_senses_white()
    right_forwards_until_rcliff_senses_white()
    left_backwards_until_lcliff_senses_black()
    right_backwards_until_rcliff_senses_black()

#----------------------------------Single Motor Align Functions--------------

def left_front_backwards_until_white():  # Left motor goes back until the left front cliff senses white
    print "Starting left_front_backwards_until_white()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def right_front_backwards_until_white():  # Right motor goes back until right front cliff senses white
    print "Starting right_front_backwards_until_white()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    while BlackFrontRight():
        pass
    m.deactivate_motors()


def left_front_backwards_until_black():  # Left motor goes back until left front cliff senses black
    print "Starting left_front_backwards_until_black()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def right_front_backwards_until_black():  # Right motor goes back until right front cliff senses black
    print "Starting right_front_backwards_until_black()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def left_front_forwards_until_white():  # Left motor goes forwards until the left front cliff senses white
    print "Starting left_front_forwards_until_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def right_front_forwards_until_white():  # Right motor goes forwards until right front cliff senses white
    print "Starting right_front_forwards_until_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    while BlackFrontRight():
        pass
    m.deactivate_motors()


def left_front_forwards_until_black():  # Left motor goes forwards until left front cliff senses black
    print "Starting left_front_forwards_until_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def right_front_forwards_until_black():  # Right motor goes forwards until left front cliff senses black
    print "Starting right_front_forwards_until_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()

#----------------------------------Turning Align Functions--------------

def turn_left_until_lcliff_senses_black(multiplier=1):
    print "Starting turn_left_until_lcliff_senses_black()"
    m.base_turn_left(multiplier)
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def turn_left_until_rcliff_senses_black(multiplier=1):
    print "Starting turn_left_until_rcliff_senses_black()"
    m.base_turn_left(multiplier)
    while NotBlackRight():
        pass
    m.deactivate_motors()


def turn_left_until_lfcliff_senses_black(multiplier=1):
    print "Starting turn_left_until_lfcliff_senses_black"
    m.base_turn_left(multiplier)
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def turn_left_until_rfcliff_senses_black(multiplier=1):
    print "Starting turn_left_until_rfcliff_senses_black"
    m.base_turn_left(multiplier)
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def turn_left_until_lcliff_senses_white(multiplier=1):
    print "Starting turn_left_until_lcliff_senses_white()"
    m.base_turn_left(multiplier)
    while BlackLeft():
        pass
    m.deactivate_motors()


def turn_left_until_rcliff_senses_white(multiplier=1):
    m.base_turn_left(multiplier)
    while BlackRight():
        pass
    m.deactivate_motors()


def turn_left_until_lfcliff_senses_white(multiplier=1):
    print "Starting turn_left_until_lfcliff_senses_white"
    m.base_turn_left(multiplier)
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def turn_left_until_rfcliff_senses_white(multiplier=1):
    print "Starting turn_left_until_rfcliff_senses_white"
    m.base_turn_left(multiplier)
    while BlackFrontRight():
        pass
    m.base_turn_left(multiplier)
    m.deactivate_motors()


def turn_right_until_lcliff_senses_black(multiplier=1):
    print "Starting turn_right_until_lcliff_senses_black()"
    m.base_turn_right(multiplier)
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def turn_right_until_rcliff_senses_black(multiplier=1):
    print "Starting turn_right_until_rcliff_senses_black()"
    m.base_turn_right(multiplier)
    while NotBlackRight():
        pass
    m.deactivate_motors()


def turn_right_until_lfcliff_senses_black(multiplier=1):
    print "Starting turn_right_until_lfcliff_senses_black"
    m.base_turn_right(multiplier)
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def turn_right_until_rfcliff_senses_black(multiplier=1):
    print "Starting turn_right_until_rfcliff_senses_black"
    m.base_turn_right(multiplier)
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def turn_right_until_lcliff_senses_white(multiplier=1):
    print "Starting turn_right_until_lcliff_senses_white()"
    m.base_turn_right(multiplier)
    while BlackLeft():
        pass
    m.deactivate_motors()


def turn_right_until_rcliff_senses_white(multiplier=1):
    m.base_turn_right(multiplier)
    while BlackRight():
        pass
    m.deactivate_motors()


def turn_right_until_lfcliff_senses_white(multiplier=1):
    print "Starting turn_right_until_lfcliff_senses_white"
    m.base_turn_right(multiplier)
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def turn_right_until_rfcliff_senses_white(multiplier=1):
    print "Starting turn_right_until_rfcliff_senses_white"
    m.base_turn_right(multiplier)
    while BlackFrontRight():
        pass
    m.deactivate_motors()


#----------------------------------Driving Back Cliff Align Functions----------------------

def left_backwards_until_lcliff_senses_white():  # Left motor goes back until the left cliff senses white
    print "Starting left_backwards_until_lcliff_senses_white()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    while BlackLeft():
        pass
    m.deactivate_motors()


def right_backwards_until_rcliff_senses_white():  # Right motor goes back until right cliff senses white
    print "Starting right_backwards_until_rcliff_senses_white()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    while BlackRight():
        pass
    m.deactivate_motors()


def left_backwards_until_lcliff_senses_black():  # Left motor goes back until left cliff senses black
    print "Starting left_backwards_until_lcliff_senses_black()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def right_backwards_until_rcliff_senses_black():  # Right motor goes back until left cliff senses black
    print "Starting right_backwards_until_rcliff_senses_black()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
    while NotBlackRight():
        pass
    m.deactivate_motors()


def left_forwards_until_lcliff_senses_white():  # Left motor goes forwards until the left cliff senses white
    print "Starting left_forwards_until_lcliff_senses_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    while BlackLeft():
        pass
    m.deactivate_motors()


def right_forwards_until_rcliff_senses_white():  # Right motor goes forwards until right cliff senses white
    print "Starting right_forwards_until_rcliff_senses_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    while BlackRight():
        pass
    m.deactivate_motors()


def left_forwards_until_lcliff_senses_black():  # Left motor goes forwards until left cliff senses black
    print "Starting left_forwards_until_lcliff_senses_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER)
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def right_forwards_until_rcliff_senses_black():  # Right motor goes forwards until left cliff senses black
    print "Starting right_forwards_until_rcliff_senses_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER)
    while NotBlackRight():
        pass
    m.deactivate_motors()

#-------------------------------------------New Stuff ---------------------------------------
# TODO organize these commands into their actual places

def forwards_until_black_rfcliff_safe():
    print "Start drive_until_black_rfcliff_safe"
    m.base_forwards()
    while NotBlackFrontRight():
        if BumpedRight():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    m.deactivate_motors()


def forwards_until_white_rfcliff_safe():
    print "Start drive_until_white_rfcliff_safe"
    m.base_forwards()
    while BlackFrontRight():
        if BumpedRight():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    m.deactivate_motors()


def forwards_until_black_lfcliff_safe():
    print "Start drive_until_black_lfcliff_safe"
    m.base_forwards()
    while NotBlackFrontLeft():
        if BumpedRight():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    m.deactivate_motors()


def forwards_until_white_lfcliff_safe():
    print "Start drive_until_white_lfcliff_safe"
    m.base_forwards()
    while BlackFrontLeft():
        if BumpedRight():
            m.turn_left(100)
            msleep(100)
            m.base_forwards()
    m.deactivate_motors()


def lfollow_lfcliff_until_bump():
# This command won't work right. It will just drive straight forwards.
     print "Starting lfollow_lfcliff_until_bump()"
     while leftIsNotBumped and NotBumpedRight():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.BASE_RM_POWER)
        else:
            create_drive_direct(c.BASE_LM_POWER, c.BASE_RM_POWER)


def lfollow_lfcliff_smooth_until_bump():
     print "Starting smooth_lfcliff_until_bump()"
     while leftIsNotBumped and NotBumpedRight():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)


def lfollow_rfcliff_smooth_until_bump():
     print "Starting smooth_rfcliff_until_bump()"
     while leftIsNotBumped and NotBumpedRight():
        if BlackFrontRight():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)


def lfollow_rfcliff_until_bump():
     print "Starting lfollow_rfcliff_until_bump()"
     while leftIsNotBumped and NotBumpedRight():
        if BlackFrontRight():
            create_drive_direct(c.BASE_LM_POWER, c.BASE_RM_POWER)
        else:
            create_drive_direct(c.BASE_LM_POWER, c.BASE_RM_POWER)

#---------------------------------------------Debug-------------------------------------------

def debug_lcliff():
    if BlackLeft():
            print "Left cliff sees black: " + str(get_create_lcliff_amt())
    elif NotBlackLeft():
            print "Left cliff sees white: " + str(get_create_lcliff_amt())
    else:
            print "Error in defining BlackLeft and NotBlackLeft"
            exit(86)


def debug_lfcliff():
    if BlackFrontLeft():
            print "Left front cliff sees black: " + str(get_create_lfcliff_amt())
    elif NotBlackFrontLeft():
            print "Left front cliff sees white: " + str(get_create_lfcliff_amt())
    else:
            print "Error in defining BlackLeft and NotBlackLeft"
            exit(86)


def debug_rcliff():
    if BlackRight():
            print "Right cliff sees black: " + str(get_create_rcliff_amt())
    elif NotBlackRight():
            print "Right cliff see white: " + str(get_create_rcliff_amt())
    else:
            print "Error in defining BlackRight and NotBlackRight"
            exit(86)


def debug_rfcliff():
    if BlackFrontRight():
            print "Right front cliff sees black: " + str(get_create_rfcliff_amt())
    elif NotBlackFrontRight():
            print "Right front cliff see white: " + str(get_create_rfcliff_amt())
    else:
            print "Error in defining BlackRight and NotBlackRight"
            exit(86)

