# This is a meaningless value. It is meant to be a placeholder for old constants
# that aren't currently being used but may be used in the future.
NO_CURRENT_VALUE = 7

#---------------------------------------------Motors-------------------------------------------

# Motor Ports (Not real - made to be consistent with Legobot)
LEFT_MOTOR = 2
RIGHT_MOTOR = 3
ARM_MOTOR = NO_CURRENT_VALUE

# Running Motor Powers
CURRENT_LM_POWER = 0
CURRENT_RM_POWER = 0
#---------------------------------------------Servos-------------------------------------------

# Servo Port
ARM_SERVO = 2
MICRO_SERVO = NO_CURRENT_VALUE
CLAW_SERVO = NO_CURRENT_VALUE

# Servo Limits
MAX_SERVO_LIMIT = 2047
MIN_SERVO_LIMIT = 0
    
MAX_ARM_SERVO_POS = 1900
MIN_ARM_SERVO_POS = 100


# Servo Base Positions
ARM_UP_POS = 1394
ARM_DOWN_POS = 200
ARM_JUST_BARELY_ON_T_POS = 690
ARM_DELIVERY_POS = 500
ARM_JUST_BELOW_T_POS = 450
ARM_HALF_UP_POS = 575
ARM_TESTING_POS = ARM_UP_POS
ARM_SUPER_HIGH_POS = 1700
# The arm is perpindicular to the ground.
ARM_START_POS = ARM_UP_POS
    

CLAW_OPEN_POS = 1024
CLAW_CLOSE_POS = 1024
CLAW_START_POS = CLAW_OPEN_POS
# Micro Servo Positions
MICRO_RIGHT_POS = 1520
MICRO_LEFT_POS = 815
MICRO_STRAIGHT_POS = 1176
MICRO_START_POS = MICRO_STRAIGHT_POS

#---------------------------------------------Movement---------------------------------------------

# Turn Values
RIGHT_TURN_TIME = 980  # 1650
LEFT_TURN_TIME = 980  # 1650

# Motor Values
BASE_LM_POWER = 199
BASE_RM_POWER = 211
FULL_LM_POWER = BASE_LM_POWER
FULL_RM_POWER = BASE_RM_POWER
HALF_LM_POWER = int(BASE_LM_POWER) / 2
HALF_RM_POWER = int(BASE_RM_POWER) / 2
BASE_ARM_MOTOR_POWER = 100

# Default Drive Times
DEFAULT_DRIVE_TIME = 500
DEFAULT_BACKWARDS_TIME = 500

#----------------------------------------------Sensors---------------------------------------------

# Analog Sensor Ports
# Cliffs are built into the Roomba, no need for analog ports.
DEPTH_SENSOR = 0
SECOND_DEPTH_SENSOR = 1
LIGHT_SENSOR = 5

# Analog Sensor Values
LCLIFF_BW = 2000  # Min is 0, max is 4950
RCLIFF_BW = 2000  # If more white, if less black
LFCLIFF_BW = 2000
RFCLIFF_BW = 2000
LFOLLOW_REFRESH_RATE = 10

# Smooth Lfollow Motor Values
LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)

# Cliff Calibration Values
MIN_SENSOR_VALUE_LCLIFF = 90000
MAX_SENSOR_VALUE_LCLIFF = 0
MAX_SENSOR_VALUE_RCLIFF = 0
MIN_SENSOR_VALUE_RCLIFF = 90000
MAX_SENSOR_VALUE_LFCLIFF = 0
MIN_SENSOR_VALUE_LFCLIFF = 90000
MAX_SENSOR_VALUE_RFCLIFF = 0
MIN_SENSOR_VALUE_RFCLIFF = 90000

# PID Line Follow Values
KP = 2.222
KI = 0.0357
KD = 0.222

# Depth Sensor Values
DEPTH_CF = 1600
SECOND_DEPTH_CF = 2700

# Gyro Sensor Values
AVG_BIAS = 0
DEGREE_CONVERSION_RATE = -0.0001
ROBOT_ANGLE = 0
GYRO_TIME = 10

# Digital Sensors
LIMIT_SWITCH = NO_CURRENT_VALUE
BUMP_SWITCH = NO_CURRENT_VALUE

# Digital Variables
FIRST_BUMP = True

# Misc Values - Placeholder variables that imply the usage of another value
BASE_POWER = 99999
BASE_TIME = 999999999
SAFETY_TIME = 15000
SAFETY_TIME_NO_STOP = SAFETY_TIME + 1
