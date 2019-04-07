#!/usr/bin/python
import os
import sys
from wallaby import *
import constants as c
import actions as a
import movement as m
import gyro as g
import sensors as s
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()  # You only need to include this command if you want the tophats to sense better at the cost of speed.
    a.get_gas_valve()
    print "Finished main\n"
    u.shutdown(86)

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
