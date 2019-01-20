#---------------------------------------------Servos-------------------------------------------

# Servo Port
ARM_SERVO = 1
MICRO_SERVO = 2

# Servo Limits
MAX_ARM_SERVO_POS = 1850
MIN_ARM_SERVO_POS = 200
SERVO_DELAY = 600  # Time needed to move a servo (need more testing to find a golden value)

# Servo Base Positions
ARM_UP_POS = 1300 # 1347  # The arm is just above the poms but below the frisbee.
ARM_COLLECTION_POS = 1024  # The arm is low enough to collect the poms.
ARM_DOWN_POS = 239  # The arm is perpendicular to the ground.
ARM_FRISBEE_GRAB_POS = 1557  # The arm is in a position where it lifts the frisbee high up.
ARM_FRISBEE_DROP_POS = 715  # The arm is low enough to drop the frisbee but not low enough to hit the bins
ARM_FRISBEE_FARTHER_DROP_POS = 558 # The arm is as low as possible
ARM_START_POS = ARM_DOWN_POS

# Micro Servo Positions
MICRO_RIGHT_POS = 1520
MICRO_LEFT_POS = 815
MICRO_STRAIGHT_POS = 1176
MICRO_START_POS = MICRO_STRAIGHT_POS

#---------------------------------------------Movement---------------------------------------------

# Turn Values
RIGHT_TURN_TIME = 1582
LEFT_TURN_TIME = 1582
MULTIPLIER = 2

# Drive Values
DEFAULT_DRIVE_TIME = 500
DEFAULT_BACKWARDS_TIME = 500
BASE_LM_POWER = 109 # TBD
BASE_RM_POWER = 100  # TBD
LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)

# Spin Values
SPIN_CW_VALUE = 200
SPIN_CCW_VALUE = 200

#----------------------------------------------Sensors--------------------------------------------- 

# Analog Sensor Ports
DEPTH_SENSOR = 0
RIGHT_DEPTH_SENSOR = 1
LIGHT_SENSOR = 5

# Analog Sensor Values
LCLIFF_BW = 2451  # To do: Test actual values. Min is 0, max is 4950
RCLIFF_BW = 2533  # If more white, if less black
LFCLIFF_BW = 2350
RFCLIFF_BW = 2750
LFCLIFF_STRAIGHT = 945
RFCLIFF_STRAIGHT = 1130
DEPTH_CF = 1250
RIGHT_DEPTH_CF = 1000
LFOLLOW_REFRESH_RATE = 20 
