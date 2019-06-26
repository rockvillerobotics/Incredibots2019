#!/usr/bin/env python2
import os
import sys
from wallaby import *
import constants as c
import actions as a
import sensors as s
import movement as m
import gyro as g
import webcam as w
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()
    m.drive(stop=False)
    s.wait_until(s.isRightOnBlack)
    u.shutdown(0)
    u.calibrate()
    a.get_ambulance_and_blocks()
    a.deliver_ambulance_and_blocks()
    a.get_firefighters()
    a.deliver_firefighters()
    u.shutdown()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()