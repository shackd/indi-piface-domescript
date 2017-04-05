#!/usr/bin/python
#
# Connect script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#
import sys
from time import sleep

import pifacedigitalio as p

p.init()

roof_status = p.digital_read(0) 

if roof_status == 0:
	p.digital_write(0,1)
	sleep(1)
	p.digital_write(0,0)

sys.exit(0)
