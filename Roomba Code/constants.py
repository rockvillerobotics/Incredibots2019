#---------------------------------------------Motors-------------------------------------------

# Motor Ports (Not real - made to be consistent with Legobot)
LEFT_MOTOR = 2
RIGHT_MOTOR = 3

# Running Motor Powers
CURRENT_LM_POWER = 0
CURRENT_RM_POWER = 0
#---------------------------------------------Servos-------------------------------------------

# Servo Port
ARM_SERVO = 1
MICRO_SERVO = 2

# Servo Limits
MAX_ARM_SERVO_POS = 1850
MIN_ARM_SERVO_POS = 200

# Servo Base Positions
ARM_UP_POS = 639
ARM_DOWN_POS = 1670
ARM_DELIVERY_POS = 1340
ARM_HALF_UP_POS = 1150
ARM_TESTING_POS = 1812  # The arm is just barely touching the ground.
ARM_START_POS = 351
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
RIGHT_TURN_TIME = 1900  # 1650
LEFT_TURN_TIME = 1900  # 1650

# Motor Values
BASE_LM_POWER = 109
BASE_RM_POWER = 104
#104- Right
#109- Left
# Default Drive Times
DEFAULT_DRIVE_TIME = 500
DEFAULT_BACKWARDS_TIME = 500
BASE_TIME = 999999999

#----------------------------------------------Sensors--------------------------------------------- 

# Analog Sensor Ports
# Cliffs are built into the Roomba, no need for analog ports.
DEPTH_SENSOR = 0
LIGHT_SENSOR = 5

# Analog Sensor Values
LCLIFF_BW = 2451  # Min is 0, max is 4950
RCLIFF_BW = 2533  # If more white, if less black
LFCLIFF_BW = 2350
RFCLIFF_BW = 2750
LFOLLOW_REFRESH_RATE = 20 

# Smooth Lfollow Motor Values
LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)

# Depth Sensor Values
DEPTH_CF = 1250

# Gyro Sensor Values
AVG_BIAS = 0
WALLAGREES_TO_DEGREES_RATE = -0.0001
ROBOT_ANGLE = 0
GYRO_TIME = 10

