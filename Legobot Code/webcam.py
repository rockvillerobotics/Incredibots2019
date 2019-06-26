from wallaby import *
from decorators import *
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


def check_zones_hospital():
    print "Starting check_zones_hospital()"
    m.lift_arm()
    msleep(25)
    ao()
    # This fully turns of the motors instead of just stopping them. Do not remove.
    camera_open()
    print "Checking zones"
    initialize_camera()
    if get_object_area(c.YELLOW, 0) > 50:
        c.BURNING_HOSPITAL = c.NEAR_ZONE
        c.SAFE_HOSPITAL = c.FAR_ZONE
    else:
        c.BURNING_HOSPITAL = c.FAR_ZONE
        c.SAFE_HOSPITAL = c.NEAR_ZONE
    m.lower_arm()
    print "Fire Hospital Zone: " + str(c.BURNING_HOSPITAL)
    print "Safe Hospital Zone: " + str(c.SAFE_HOSPITAL)


def graphics():
    console_clear()
    max_length = 480
    max_height = 260
    middle_length = max_length / 2
    graphics_open(max_length, max_height)  # Creates the graphics array with the given size
    graphics_fill(255, 255, 255)  # Fills screen with white
    graphics_rectangle_fill(0, 0, middle_length, max_height, 255, 255, 0)  # Fills left with yellow.
    graphics_rectangle_fill(middle_length / 2, max_height / 3, 3 * middle_length / 4, 2 * max_height / 3, 255, 0, 0)  # Fills right with red.
    graphics_update()
