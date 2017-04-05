#!/usr/bin/python
#
# Status script for INDI Dome Scripting Gateway
#
# Arguments: file name to save current state and coordinates (parked ra dec)
# Exit code: 0 for success, 1 for failure
#

import sys
import pifacedigitalio as p

script, path = sys.argv

p.init()
roof_status = p.digital_read(0)
dome_status = str(roof_status) + ' 0 0'

status = open(path, 'w')
status.truncate()
status.write(dome_status)
status.close()

sys.exit(0)

