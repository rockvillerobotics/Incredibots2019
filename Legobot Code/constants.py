#   When possible, make values into constants so they can be easily changed throughout the code at once. 
#   Constants are subject to change, so make sure to check the values to be certain that they are right.
#   Note: All constant timings are assumed to be in milliseconds unless otherwise specified.

from wallaby import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Bot Definitions~~~~~~~~~~~~~~~~~~~~~~~~
def MAIN_BOT_CHANNEL_COUNT(): 
    return(get_channel_count() == 3)

def CLONE_BOT_CHANNEL_COUNT():
    return(get_channel_count() == 4)  # If the bot has 4 camera channels, then it is the clone bot.

IS_MAIN_BOT = right_button() == 0 and MAIN_BOT_CHANNEL_COUNT() or left_button() == 1  # Left button for main

IS_CLONE_BOT = left_button() == 0 and CLONE_BOT_CHANNEL_COUNT() or right_button() == 1  # Right button for clone

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Motors, Servos, and Sensors~~~~~~~~~~~~~~~~~~~~~~~~
if IS_MAIN_BOT:
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Motors~~~~~~~~~~~~~~~~~~~~~~~~

    # Motor Ports
    LEFT_MOTOR = 2
    RIGHT_MOTOR = 3

    # Base Motor Powers
    BASE_LM_POWER = 880
    BASE_RM_POWER = -900
    LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
    LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)
    
    # Motor Power Trackers
    CURRENT_LM_POWER = 0
    CURRENT_RM_POWER = 0

    # Motor Timings
    RIGHT_TURN_TIME = 900  # Need to test turn timings periodically. They change as battery charge changes, or on new boards.
    LEFT_TURN_TIME = 900
    DEFAULT_DRIVE_TIME = 500
    DEFAULT_BACKWARDS_TIME = 500
    PIVOT_RIGHT_TURN_TIME = 3580  # Turns 180 degrees. Not currently used.
    PIVOT_LEFT_TURN_TIME = 3400  # Ditto above.
    MOVEMENT_REFRESH_RATE = 30

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Servos~~~~~~~~~~~~~~~~~~~~~~~~

    # Servo Limits
    MAX_SERVO_POS = 1900  # Cannot physically exceed 2047 or servo will break. Metal servos are more affected.
    MIN_SERVO_POS = 100  # Cannot physically exceed 0 or servo will break. Metal servos are more affected.
    SERVO_DELAY = 500  # Time needed to move a servo (need more testing to find a good value).

    # Arm Servo
    ARM_SERVO = 2
    MAX_ARM_SERVO_POS = MAX_SERVO_POS
    MIN_ARM_SERVO_POS = MIN_SERVO_POS
    ARM_UP_POS = 1762
    ARM_DOWN_POS = 1096

    # Cube Arm Servo
    CUBE_ARM_SERVO = 0
    MAX_CUBE_ARM_SERVO_POS = MAX_SERVO_POS
    MIN_CUBE_ARM_SERVO_POS = MIN_SERVO_POS
    CUBE_ARM_UP_POS = 955
    CUBE_ARM_DOWN_POS = 101
    CUBE_ARM_LESS_UP_POS = 470
    CUBE_ARM_HOLDING_POS = 1899

    # Claw Servo
    CLAW_SERVO = 1
    MAX_CLAW_SERVO_POS = MAX_SERVO_POS
    MIN_CLAW_SERVO_POS = MIN_SERVO_POS
    CLAW_OPEN_POS = 417  # Claw fingers form a 180 degree line
    CLAW_CLOSE_POS = 1298
    CLAW_TRUCK_CLOSE_POS = 1418
    CLAW_LESS_OPEN_POS = 928
    CLAW_CHECKING_POS = CLAW_CLOSE_POS

    # Micro Servo
    MICRO_SERVO = 3


    # Starting Positions
    STARTING_ARM_POS = ARM_DOWN_POS
    STARTING_CLAW_POS = CLAW_LESS_OPEN_POS
    STARTING_CUBE_ARM_POS = CUBE_ARM_HOLDING_POS

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Sensors~~~~~~~~~~~~~~~~~~~~~~~~

    # Analog Ports
    LIGHT_SENSOR = 5
    LEFT_TOPHAT = 0
    RIGHT_TOPHAT = 1
    THIRD_TOPHAT = 4

    # Analog Values
    LEFT_TOPHAT_BW = 721  # If more, black. If less, white.
    RIGHT_TOPHAT_BW = 785  # If more, black. If less, white.
    THIRD_TOPHAT_BW = 2083  # If more, black. If less, white.
    LFOLLOW_REFRESH_RATE = 30  # Default amount of time before tophats check their black/white status again.
    AVG_BIAS = 0

    # Digital Sensors
    RIGHT_BUMP_SENSOR = 0

    # Gryo Conversian Rates
    WALLAGREES_TO_DEGREES_RATE = 90 / 50000.0

    # Camera Colors
    YELLOW = 0
    RED = 1
    GREEN = 2

    # Camera Zones
    NEAR_ZONE = -1
    FAR_ZONE = 1
    FIRE_HOSPITAL = NEAR_ZONE
    SAFE_HOSPITAL = FAR_ZONE

    # PID Lfollow Values
    MAX_TOPHAT_VALUE_RIGHT = 3200
    MIN_TOPHAT_VALUE_RIGHT = 158
    MAX_TOPHAT_VALUE_LEFT = 3200
    MIN_TOPHAT_VALUE_LEFT = 158  # These values dont do anything unless calib command doesnt work right.
    KP = 10 # 5.75
    KI = 0.161
    KD = 1
    KP_SAFE = 7
    KI_SAFE = 0.061
    KD_SAFE = 1

    # Miscellaneous Values
    SAFETY_TIME = 15000  # This is the while loop time limit that ensures we don't have an infinite loop.
    SAFETY_TIME_NO_STOP = SAFETY_TIME + 1
    BASE_TIME = 9999
else:  # Clone Bot ----------------------------------------------------------------------------------------------------------------
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Motors~~~~~~~~~~~~~~~~~~~~~~~~

    # Clone Motor Ports
    LEFT_MOTOR = 3
    RIGHT_MOTOR = 2

    # Clone Base Motor Powers
    BASE_LM_POWER = 900  # 680 on plastic motor.
    BASE_RM_POWER = -900
    LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
    LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)
    
    # Clone Motor Power Trackers
    CURRENT_LM_POWER = 0
    CURRENT_RM_POWER = 0

    # Clone Motor Timings
    RIGHT_TURN_TIME = 900  # Need to test turn timings periodically. They change as battery charge changes, or on new boards.
    LEFT_TURN_TIME = 900  # 90 degrees
    DEFAULT_DRIVE_TIME = 500
    DEFAULT_BACKWARDS_TIME = 500
    PIVOT_RIGHT_TURN_TIME = 3900  # Turns 180 degrees. Not currently used.
    PIVOT_LEFT_TURN_TIME = 3900  # Ditto above.
    MOVEMENT_REFRESH_RATE = 30

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Servos~~~~~~~~~~~~~~~~~~~~~~~~

    # Clone Servo Limits
    MAX_SERVO_POS = 1900  # Cannot physically exceed 2047 or servo will break. Metal servos are more affected.
    MIN_SERVO_POS = 100  # Cannot physically exceed 0 or servo will break. Metal servos are more affected.
    SERVO_DELAY = 500  # Time needed to move a servo (need more testing to find a good value).

    # Clone Arm Servo
    ARM_SERVO = 0
    MAX_ARM_SERVO_POS = MAX_SERVO_POS
    MIN_ARM_SERVO_POS = MIN_SERVO_POS
    ARM_UP_POS = 1306
    ARM_DOWN_POS = 1024

    # Clone Cube Arm Servo
    CUBE_ARM_SERVO = 2
    MAX_CUBE_ARM_SERVO_POS = MAX_SERVO_POS
    MIN_CUBE_ARM_SERVO_POS = MIN_SERVO_POS
    CUBE_ARM_UP_POS = 1750
    CUBE_ARM_DOWN_POS = 1015

    # Clone Claw Servo
    CLAW_SERVO = 3
    MAX_CLAW_SERVO_POS = MAX_SERVO_POS
    MIN_CLAW_SERVO_POS = MIN_SERVO_POS
    CLAW_OPEN_POS = 1200  # Claw fingers form a 180 degree line
    CLAW_CLOSE_POS = 1652
    CLAW_CHECKING_POS = CLAW_CLOSE_POS

    # Clone Starting Positions
    STARTING_ARM_POS = ARM_UP_POS
    STARTING_CLAW_POS = CLAW_OPEN_POS
    STARTING_CUBE_ARM_POS = CUBE_ARM_UP_POS

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Sensors~~~~~~~~~~~~~~~~~~~~~~~~

    # Clone Analog Ports
    LIGHT_SENSOR = 5
    LEFT_TOPHAT = 0
    RIGHT_TOPHAT = 1
    THIRD_TOPHAT = 4

    # Clone Analog Values
    LEFT_TOPHAT_BW = 1627 #1800  # If more, black. If less, white.
    RIGHT_TOPHAT_BW = 1783  # If more, black. If less, white.
    THIRD_TOPHAT_BW = 2121 # If more, black. If less, white.
    LFOLLOW_REFRESH_RATE = 30  # Default amount of time before tophats check their black/white status again.
    AVG_BIAS = 0

    # Clone Digital Sensors
    RIGHT_BUMP_SENSOR = 0
    
    # Clone Gryo Conversian Rates
    WALLAGREES_TO_DEGREES_RATE = 90 / 580000

    # Clone Camera Colors
    YELLOW = 0
    RED = 1
    GREEN = 2
    
    # Clone Camera Zones
    NEAR_ZONE = -1
    FAR_ZONE = 1
    FIRE_HOSPITAL = NEAR_ZONE
    SAFE_HOSPITAL = FAR_ZONE
    
    # Clone PID Lfollow Values
    MAX_TOPHAT_VALUE_RIGHT = 3200
    MIN_TOPHAT_VALUE_RIGHT = 158
    MAX_TOPHAT_VALUE_LEFT = 3200
    MIN_TOPHAT_VALUE_LEFT = 158  # These values dont do anything unless calib command doesnt work right.
    KP = 5.75
    KI = 0.161
    KD = 1
    KP_SAFE = 7
    KI_SAFE = 0.061
    KD_SAFE = 1

    # Clone Miscellaneous Values
    SAFETY_TIME = 15000  # This is the time limit for all while loops that ensures we don't have an infinite loop.
    SAFETY_TIME_NO_STOP = SAFETY_TIME + 1
    BASE_TIME = 9999