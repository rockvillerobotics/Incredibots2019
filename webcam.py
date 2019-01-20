from wallaby import *
import constants as c
import movement as m
import actions as a
import sensors as s

def initialize_camera():
    # Wait two seconds for camera to initialize
    print "Initializing Camera"
    i = 0  # Counter
    print "Starting Step 1..."
    while i < 55:
        camera_update()
        i += 1
        msleep(1)
    print "Finished Step 100\n"


def check_zones_full():
    print "Checking zones"
    msleep(25)
    ao()
    m.arm_slow(c.ARM_HIGH_POS, 2, 1)
    camera_open()
    initialize_camera()
    console_clear()
    graphics_open(480, 260)
    graphics_fill(255, 255, 255)
    graphics_update()
    a.crate_zone = 30
    a.botguy_zone = 30
    if get_object_area(c.YELLOW, 0) > 50:  # Testing to see if middle zone is yellow
        print "The middle zone is yellow.\n"
        a.crate_zone = c.MIDDLE
        graphics_rectangle_fill(160, 0, 320, 260, 255, 255, 0)  # Yellow
        graphics_update()
    elif get_object_area(c.RED, 0) > 50:
        a.botguy_zone = c.MIDDLE
        graphics_rectangle_fill(160, 0, 320, 260, 255, 0, 0)  # Red
        graphics_update()
        print "The middle zone is red.\n" 
    else:
        print "The middle is not red nor yellow.\n"
        graphics_rectangle_fill(160, 0, 320, 260, 0, 255, 0)  # Green
        graphics_update()
    m.turn_left(400)  # Checking the left zone
    msleep(25)
    ao()
    initialize_camera()
    if get_object_area(c.YELLOW, 0) > 100:  # Testing to see if left zone is yellow
        print "The left zone is yellow.\n"
        graphics_rectangle_fill(0, 0, 160, 260, 255, 255, 0)  # Yellow
        graphics_update()
        if a.crate_zone == 30: 
            a.crate_zone = c.LEFT
        else:
            print "ERROR. The wallaby sensed yellow for the left zone and the middle zone.\n"
    elif get_object_area(c.RED, 0) > 100:
        print "The left zone is red\n"
        graphics_rectangle_fill(0, 0, 160, 260, 255, 0, 0)  # Red
        graphics_update()
        if a.botguy_zone == 30: 
            a.botguy_zone = c.LEFT
        else:
            print "ERROR. The wallaby sensed red for the left zone and the middle zone.\n"
    else:
        print "The left zone is neither red nor yellow.\n"
        graphics_rectangle_fill(0, 0, 160, 260, 0, 255, 0)  # Green
        graphics_update()
    if a.crate_zone == 30:  # If the crate zone has not been set yet.
        a.crate_zone = c.RIGHT
        graphics_rectangle_fill(320, 0, 480, 260, 255, 255, 0)  # Yellow
        graphics_update()
        print "The right zone is yellow.\n"
    elif a.botguy_zone == 30:
        if a.crate_zone == c.RIGHT:
            print "Code failure"
        else:
            a.botguy_zone = c.RIGHT
            graphics_rectangle_fill(320, 0, 480, 260, 255, 0, 0)  # Red
            graphics_update()
        print "The right zone is red. \n"
    else:
        print "The right zone is neither red nor yellow."
        graphics_rectangle_fill(320, 0, 480, 260, 0, 255, 0)  # Green
        graphics_update()
    if a.botguy_zone == 30:
        if a.crate_zone == c.RIGHT:
            a.botguy_zone = c.LEFT
            graphics_rectangle_fill(0, 0, 160, 260, 255, 0, 0)  # Red
            graphics_update()
            print "We are guessing that the left zone is red. \n"
        else:
            a.botguy_zone = c.RIGHT
            graphics_rectangle_fill(320, 0, 480, 260, 255, 0, 0)
            graphics_update()
            print "We are guessing that the right zone is red. \n"
    s.left_forwards_until_black()  # The left tophat can end up on white - Jet 6-27-18 
    s.align_far()
    camera_close()
    graphics_close()
    print "Crate zone: " + str(a.crate_zone)
    print "Botguy zone: " + str(a.botguy_zone)
    print "~fin~\n\n\n"


"""
#    Psuedocode:
#    check zone on middle, if it is yellow set variable "zone" to be equal to middle
#    check zone on left, if it is yellow set variable "zone" to be equal to left
#    check zone on right, if it is yellow set variable "zone" to be equal to right
#    go back to middle
"""
