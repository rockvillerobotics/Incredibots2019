#!/usr/bin/env python2
import os
import sys
from wallaby import *
import constants as c
import actions as a
import movement as m
import sensors as s
import gyro as g
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()  # You only need to include this command if you want the cliffs to sense better at the cost of speed.
    a.first_position()
    print "Finished main\n"
    u.shutdown()
    

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
