#!/usr/bin/env python2
import os
import sys
from wallaby import *
import constants as c
import actions as a
import sensors as s
import movement as m
import webcam as w
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()
    a.deliver_ambulance()
    a.get_prism()
    a.deliver_prism_and_cube()
    u.sd()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()