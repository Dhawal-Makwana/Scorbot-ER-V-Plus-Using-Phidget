from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.DigitalInput import *
import time
from functions import control, home


def onStateChange(self, state):
	print("State: " + str(state))

def homing():
	# shoulder link 1
	home(146627, 1)
	# elbow link 2
	home(146520, 1)
	#  base link 0
	home(146552, -0.3)
	# Gripper Close
	control(146491, 1, 2)
	print("Home Position")
	
	
	
	
