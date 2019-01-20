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

def leftIsBumped():
    return(get_create_lbump() == 1)

def leftIsNotBumped():
    return(get_create_lbump() == 0)

def rightIsBumped():
    return(get_create_rbump() == 1)

def rightIsNotBumped():
    return(get_create_rbump() == 0)

def DepthSensesObject():
    return(analog(c.DEPTH_SENSOR) > c.DEPTH_CF)

def NotDepthSensesObject():
    return(analog(c.DEPTH_SENSOR) < c.DEPTH_CF)

def RightDepthSensesObject():
    return(analog(c.RIGHT_DEPTH_SENSOR) > c.RIGHT_DEPTH_CF)

def NotRightDepthSensesObject():
    return(analog(c.RIGHT_DEPTH_SENSOR) < c.RIGHT_DEPTH_CF)

#---------------------------------------------Line Follow Functions-------------------------------------------

def backwards_until_black_lcliff():
    print "Start drive_until_black_lcliff"
    m.activate_motors()
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def backwards_until_white_lcliff():
    print "Start drive_until_black_lcliff"
    m.activate_motors()
    while BlackLeft():
        pass
    m.deactivate_motors()


def backwards_through_line_cliff():
    backwards_until_black_lcliff()
    backwards_until_white_lcliff()


def forwards_until_black_lcliff():
    print "Start drive_until_black_lcliff"
    m.activate_motors(1)
    while NotBlackLeft():
        pass
    m.deactivate_motors()


def forwards_until_white_lcliff():
    print "Start drive_until_black_lcliff"
    m.activate_motors(1)
    while BlackLeft():
        pass
    m.deactivate_motors()


def forwards_until_line_cliffs():
    m.activate_motors(1)
    while NotBlackLeft() and NotBlackRight():
        pass
    m.deactivate_motors()


def forwards_until_line_fcliffs():
    m.activate_motors(1)
    while NotBlackFrontLeft() and NotBlackFrontRight():
        pass
    m.deactivate_motors()


def forwards_through_line_lcliff():
    forwards_until_black_lcliff()
    forwards_until_white_lcliff()



def forwards_until_black_rcliff():
    print "Start drive_until_black_rcliff"
    m.activate_motors(1)
    while NotBlackRight():
        pass
    m.deactivate_motors()


def forwards_until_white_rcliff():
    print "Start drive_until_black_rcliff"
    m.activate_motors(1)
    while BlackRight():
        pass
    m.deactivate_motors()


def backwards_until_black_lfcliff():
    print "Start drive_until_black_lfcliff"
    m.activate_motors()
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def backwards_until_white_lfcliff():
    print "Start backwards_until_white_lfcliff"
    m.activate_motors()
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def backwards_until_black_rfcliff():
    print "Start backwards_until_black_rfcliff"
    m.activate_motors()
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def backwards_until_white_rfcliff():
    print "Start backwards_until_white_rfcliff"
    m.activate_motors()
    while BlackFrontRight():
        pass
    m.deactivate_motors()


def backwards_through_line_lfcliff():
    backwards_until_black_lfcliff()
    backwards_until_white_lfcliff()


def forwards_until_black_lfcliff():
    print "Start forwards_until_black_lfcliff"
    m.activate_motors(1)
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def forwards_until_white_lfcliff():
    print "Start forwards_until_white_lfcliff"
    m.activate_motors(1)
    while BlackFrontLeft():
        pass
    m.deactivate_motors()


def forwards_until_white_rfcliff():
    print "Start forwards_until_white_rfcliff"
    m.activate_motors(1)
    while BlackFrontRight():
        pass
    m.deactivate_motors()


def forwards_until_black_rfcliff():
    print "Start forwards_until_black_rfcliff"
    m.activate_motors(1)
    while NotBlackFrontRight():
        pass
    m.deactivate_motors()


def forwards_through_line_lfcliff():
    forwards_until_black()
    forwards_until_white()


def lfollow_left(time, refresh_rate = c.LFOLLOW_REFRESH_RATE):  # Line follow with the left tophat for time
    print "Starting lfollow_left()\n"
    sec = seconds() + time
    while seconds() < sec:
        if BlackLeft():
            create_drive_direct(0, 200)
        elif NotBlackLeft():
            create_drive_direct(200, 0)
        msleep(refresh_rate)
        create_stop()

        
def lfollow_left_front(time, refresh_rate = c.LFOLLOW_REFRESH_RATE):  # Line follow with the left tophat for time
    print "Starting lfollow_left()\n"
    sec = seconds() + time
    while seconds() < sec:
        if BlackFrontLeft():
            create_drive_direct(0, 200)
        elif NotBlackFrontLeft():
            create_drive_direct(200, 0)
        msleep(refresh_rate)
        create_stop()

def lfollow_left_bstop_smooth(time = 10, refresh_rate = c.LFOLLOW_REFRESH_RATE):
    print "Starting lfollow_left_bstop_smooth()\n"
    sec = seconds() + time
    while seconds() < sec:
        if  NotBlackLeft():
            create_drive_direct(200, 148)
        elif BlackLeft():
            create_drive_direct(148, 200)
        else:
            exit(86)
        msleep(refresh_rate)
        create_stop()


def lfollow_right_backwards_bstop_smooth(time = 10, refresh_rate = c.LFOLLOW_REFRESH_RATE):
    print "Starting lfollow_right_backwards_bstop_smooth()\n"
    sec = seconds() + time
    while seconds() < sec:
        if  NotBlackRight():
            create_drive_direct(-175, -200)
        elif BlackRight():
            create_drive_direct(-200, -175)
        msleep(refresh_rate)
        create_stop()


def lfollow_left_opposite(time, refresh_rate = c.LFOLLOW_REFRESH_RATE):
    sec = seconds() + time
    while seconds() < sec:
        if BlackLeft():
            create_drive_direct(200, 0)
        else:
            create_drive_direct(0, 200)
        msleep(refresh_rate)
        create_stop()


def lfollow_right(time, refresh_rate = c.LFOLLOW_REFRESH_RATE):  # Line follow with the right cliff for time
    print "Starting lfollow_right()\n"
    sec = seconds() + time
    while seconds() < sec:
        if BlackRight():
            create_drive_direct(0, -1 * c.BASE_RM_POWER)
        elif not BlackRight():
            create_drive_direct(-1 * c.BASE_LM_POWER, 0)
        msleep(refresh_rate)
        create_stop()
                
def both_lfollow(time,refresh_rate = c.LFOLLOW_REFRESH_RATE):  # Line follow using both tophats until time is reached
    print "Starting both_lfollow()\n"
    sec = seconds() + time
    while seconds() < sec:
        if NotBlackRight() and BlackLeft():
            create_drive_direct(200, 200)
        elif BlackRight() and NotBlackLeft():
            create_drive_direct(200, 200)
        elif NotBlackRight() and NotBlackLeft():
            create_drive_direct(200, 0)
        elif BlackRight and NotBlackLeft():
            create_drive_direct(0,200)
        msleep(refresh_rate)
        create_stop()


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

#---------------------------------------------Depth Functions-------------------------------------------

def backwards_until_depth_senses_object():
    m.activate_motors()
    while NotDepthSensesObject():
        pass
    m.deactivate_motors()


def backwards_until_depth_senses_nothing():
    m.activate_motors()
    while DepthSensesObject():
        pass
    m.deactivate_motors()


def forwards_until_depth_senses_object():
    m.activate_motors(1)
    while NotDepthSensesObject():
        pass
    m.deactivate_motors()


def lfollow_lfcliff_smooth_until_depth_senses_object():
    print "Starting lfollow_lfcliff_smooth_until_rfcliff_senses_black()"
    while NotDepthSensesObject():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)


def lfollow_lfcliff_smooth_until_right_depth_senses_object():
    print "Starting lfollow_lfcliff_smooth_until_right_depth_senses_object()"
    while NotRightDepthSensesObject():
        if BlackFrontLeft():
            create_drive_direct(c.BASE_LM_POWER, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            create_drive_direct(c.LFOLLOW_SMOOTH_LM_POWER, c.BASE_RM_POWER)


def wait_for_depth(time = 15):
    print "Starting wait_for_depth()"
    sec = seconds() + time
    while NotRightDepthSensesObject() and seconds() < sec:
        pass
        

def wait_for_empty(time = 7):
    print "Starting wait_for_empty()"
    sec = seconds() + time
    while RightDepthSensesObject() and seconds() < sec:
        pass
#----------------------------------------------Bump-------------------------------------------

def bump_left():
    while get_create_lbump() == 0:
        m.drive(50)
                
def bump_right():
    while get_create_rbump() == 0:
        m.drive(50)
            
def begin_pom_conquest(time):
    sec = seconds() + time
    while seconds() < sec:
        if get_create_lbump() == 1:
            create_stop()
            m.backwards(80, -100, -100)
            m.pivot_left(20)
        else:
            create_drive_direct(-100,-100)
    create_stop()
    front_forwards_align_until_black(4)
    #m.backwards(800, -100, -100)


def forwards_until_bump():
    print "Starting forwards_until_bump()"
    m.activate_motors(1)
    while leftIsNotBumped() and rightIsNotBumped():
        pass
    m.deactivate_motors()

#----------------------------------Driving Front Cliff Align Functions--------------

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
    left_back_backwards_until_white()
    right_back_backwards_until_white()
    left_back_forwards_until_black()
    right_back_forwards_until_black()    


def align_far_cliffs():
    left_back_forwards_until_white()
    right_back_forwards_until_white()
    left_back_backwards_until_black()
    right_back_backwards_until_black()


def left_point_turn_until_rcliff_senses_black():
    m.activate_motors(1, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
    while NotBlackRight():
        pass
    m.deactivate_motors()


def left_point_turn_until_lfcliff_senses_black():
    m.activate_motors(1, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
    while NotBlackFrontLeft():
        pass
    m.deactivate_motors()


def left_front_backwards_until_white():  # Left motor goes back until the left front tophat senses white
    print "Starting left_front_backwards_until_white()"
    create_drive_direct(-1 * c.BASE_LM_POWER, 0)
    while BlackFrontLeft():
        pass
    create_drive_direct(0,0)
            
            
def right_front_backwards_until_white():  # Right motor goes back until right front tophat senses white
    print "Starting right_front_backwards_until_white()"
    create_drive_direct(0, -1 * c.BASE_RM_POWER)
    while BlackFrontRight():
        pass
    create_drive_direct(0,0)

            
def left_front_backwards_until_black():  # Left motor goes back until left front tophat senses black
    print "Starting left_front_backwards_until_black()"
    create_drive_direct(-1 * c.BASE_LM_POWER, 0)
    while NotBlackFrontLeft():
        pass
    create_drive_direct(0,0)

            
def right_front_backwards_until_black():  # Right motor goes back until right front tophat senses black
    print "Starting right_front_backwards_until_black()"
    create_drive_direct(0, -1 * c.BASE_RM_POWER)
    while NotBlackFrontRight():
        pass
    create_drive_direct(0,0)

            
def left_front_forwards_until_white():  # Left motor goes forwards until the left front tophat senses white
    print "Starting left_front_forwards_until_white()"
    create_drive_direct(c.BASE_LM_POWER, 0)
    while BlackFrontLeft():
        pass
    create_drive_direct(0,0)
            
            
def right_front_forwards_until_white():  # Right motor goes forwards until right front tophat senses white
    print "Starting right_front_forwards_until_white()"
    create_drive_direct(0, c.BASE_RM_POWER)
    while BlackFrontRight():
        pass
    create_drive_direct(0,0)
            
            
def left_front_forwards_until_black():  # Left motor goes forwards until left front tophat senses black
    print "Starting left_front_forwards_until_black()"
    create_drive_direct(c.BASE_LM_POWER, 0)
    while NotBlackFrontLeft():
        pass
    create_drive_direct(0,0)

            
def right_front_forwards_until_black():  # Right motor goes forwards until left front tophat senses black
    print "Starting right_front_forwards_until_black()"
    create_drive_direct(0, c.BASE_RM_POWER)
    while NotBlackFrontRight():
        pass
    create_drive_direct(0,0)


def right_point_turn_until_rfcliff_senses_black(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(multiplier * left_power), int(-1 * multiplier * right_power))
    while NotBlackFrontRight():
        pass
    create_drive_direct(0,0)


def right_point_turn_until_rfcliff_senses_white(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(multiplier * left_power), int(-1 * multiplier * right_power))
    while BlackFrontRight():
        pass
    create_drive_direct(0,0)


def right_point_turn_until_lfcliff_senses_black(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(multiplier * left_power), int(-1 * multiplier * right_power))
    while NotBlackFrontLeft():
        pass
    create_drive_direct(0,0)


def right_point_turn_until_lfcliff_senses_white(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(multiplier * left_power), int(-1 * multiplier * right_power))
    while BlackFrontLeft():
        pass
    create_drive_direct(0,0)


def left_point_turn_until_rfcliff_senses_black(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(-1 * multiplier * left_power), int(multiplier * right_power))
    while NotBlackFrontRight():
        pass
    create_drive_direct(0,0)


def left_point_turn_until_rfcliff_senses_white(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(-1 * multiplier * left_power), int(multiplier * right_power))
    while BlackFrontRight():
        pass
    create_drive_direct(0,0)


def left_point_turn_until_lfcliff_senses_black(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(-1 * multiplier * left_power), int(multiplier * right_power))
    while NotBlackFrontLeft():
        pass
    create_drive_direct(0,0)


def left_point_turn_until_lfcliff_senses_white(multiplier = 1, left_power = c.BASE_LM_POWER, right_power = c.BASE_RM_POWER):
    create_drive_direct(int(-1 * multiplier * left_power), int(multiplier * right_power))
    while BlackFrontLeft():
        pass
    create_drive_direct(0,0)

#----------------------------------Driving Back Cliff Align Functions----------------------            
        
def left_back_backwards_until_white():  # Left motor goes back until the left tophat senses white
    print "Starting left_back_backwards_until_white()"
    create_drive_direct(-1 * c.BASE_LM_POWER, 0)
    while BlackLeft():
        pass
    create_drive_direct(0,0)
            
            
def right_back_backwards_until_white():  # Right motor goes back until right tophat senses white
    print "Starting right_back_backwards_until_white()"
    create_drive_direct(0, -1 * c.BASE_RM_POWER)
    while BlackRight():
        pass
    create_drive_direct(0,0)

            
def left_back_backwards_until_black():  # Left motor goes back until left tophat senses black
    print "Starting left_back_backwards_until_black()"
    create_drive_direct(-1 * c.BASE_LM_POWER, 0)
    while NotBlackLeft():
        pass
    create_drive_direct(0,0)

            
def right_back_backwards_until_black():  # Right motor goes back until left tophat senses black
    print "Starting right_back_backwards_until_black()"
    create_drive_direct(0, -1 * c.BASE_RM_POWER)
    while NotBlackRight():
        pass
    create_drive_direct(0,0)

            
def left_back_forwards_until_white():  # Left motor goes forwards until the left tophat senses white
    print "Starting left_back_forwards_until_white()"
    create_drive_direct(c.BASE_LM_POWER, 0)
    while BlackLeft():
        pass
    create_drive_direct(0,0)
            
            
def right_back_forwards_until_white():  # Right motor goes forwards until right tophat senses white
    print "Starting right_back_forwards_until_white()"
    create_drive_direct(0, c.BASE_RM_POWER)
    while BlackRight():
        pass
    create_drive_direct(0,0)
            
            
def left_back_forwards_until_black():  # Left motor goes forwards until left tophat senses black
    print "Starting left_back_forwards_until_black()"
    create_drive_direct(c.BASE_LM_POWER, 0)
    while NotBlackLeft():
        pass
    create_drive_direct(0,0)

            
def right_back_forwards_until_black():  # Right motor goes forwards until left tophat senses black
    print "Starting right_back_forwards_until_black()"
    create_drive_direct(0, c.BASE_RM_POWER)
    while NotBlackRight():
        pass
    create_drive_direct(0,0)
            
#----------------------------------Driving Back Cliff Align Functions------------------------
            
def both_back_backwards_until_white():
    print "Starting both_back_backwards_until_white()"
    create_drive_direct(-100, -100)
    while BlackLeft() and BlackRight():
        pass
    create_drive_direct(0,0)
            
            
def both_back_backwards_until_black():
    print "Starting both_back_backwards_until_black()"
    create_drive_direct(-100, -100)
    while NotBlackLeft() and NotBlackRight():
        pass
    create_drive_direct(0,0)
            
def both_front_backwards_until_white():
    print "Starting both_front_backwards_until_white()"
    create_drive_direct(-100, -100)
    while BlackFrontLeft() and BlackFrontRight():
        pass
    create_drive_direct(0,0)
            
def both_front_backwards_until_black():
    print "Starting both_front_backwards_until_black()"
    create_drive_direct(-100, -100)
    while NotBlackLeft() and NotBlackRight():
        pass
    create_drive_direct(0,0)
            
#--------------------------------------------Align----------------------------------------------                         
                    

def front_backwards_align_until_black(time):
    print "start front_backwards_align_until_black()"
    sec = seconds() + time
    while seconds() < sec:
        if NotBlackFrontLeft():
            create_drive_direct(-100,-100)
        else: 
            create_stop()
    msleep(10)
    create_stop()
               
         
def front_forwards_align_until_black(time):
    print "start front_forwards_align_until_black()"
    sec = seconds() + time
    while seconds() < sec:
        if NotBlackFrontLeft():
            print "it works with left?"
            if get_create_lbump() == 1:
                m.backwards(80, -100, -100)
                m.pivot_left(20)
            else: 
                create_drive_direct(-100,-100)
        elif NotBlackFrontRight():
            print "it works with right?"
            if get_create_lbump() == 1:
                m.backwards(80, -100, -100)
                m.pivot_left(20)
            else: 
                create_drive_direct(-100,-100)
        elif BlackFrontLeft():
            print "sensed black with left cliff"
            exit(86)
        elif BlackFrontRight():
            print "sensed black with right cliff"
            exit(86)
    msleep(100)
    create_stop()
                
def front_backwards_align_until_white(time):
    print "start front_backwards_align_until_white()"
    sec = seconds() + time
    while seconds() < sec:
        if BlackFrontLeft() or BlackFrontRight():
            create_drive_direct(-100,-100)
        else: 
            create_stop()
    msleep(10)
    create_stop()
       
                
def back_backwards_align_until_white(time):
    print "start back_backwards_align_until_white()"
    sec = seconds() + time
    while seconds() < sec:
        if BlackLeft() or BlackRight():
            create_drive_direct(-100,-100)
        else: 
            create_stop()
    msleep(10)
    create_stop()
            
                
def back_backwards_align_until_black(time):
    print "start back_backwards_align_until_black()"
    sec = seconds() + time
    while seconds() < sec:
        if NotBlackLeft() or NotBlackRight():
            create_drive_direct(-150,-150)
            print "Running first_align"
        else: 
            create_stop()
            print "Not Moving"
        msleep(1)
    msleep(10)
    create_stop()
            
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
