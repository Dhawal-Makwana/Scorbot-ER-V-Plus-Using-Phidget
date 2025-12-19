from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.DigitalInput import *
import time

def control(serial, velocity, duration):
	#Create your Phidget channels
	dcMotor0 = DCMotor()

	#Set addressing parameters to specify which channel to open (if any)
	dcMotor0.setDeviceSerialNumber(serial)

	#Open your Phidgets and wait for attachment
	dcMotor0.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.
	dcMotor0.setTargetVelocity(velocity)
	time.sleep(duration)

	#Close your Phidgets once the program is done.
	dcMotor0.close()
	
def home(serial, velocity):
	#Create your Phidget channels
	dcMotor0 = DCMotor()
	digitalInput0 = DigitalInput()

	#Set addressing parameters to specify which channel to open (if any)
	dcMotor0.setDeviceSerialNumber(serial)
	digitalInput0.setDeviceSerialNumber(serial)

	#Assign any event handlers you need before calling open so that no events are missed.
	digitalInput0.setOnStateChangeHandler(onStateChange)

	#Open your Phidgets and wait for attachment
	dcMotor0.openWaitForAttachment(5000)
	digitalInput0.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.
	while digitalInput0.getState() != 1:
		dcMotor0.setTargetVelocity(velocity)
		time.sleep(0.5)
		
	#Close your Phidgets once the program is done.
	dcMotor0.close()
	digitalInput0.close()

# Digital Input State Check
def onStateChange(self, state):
	print("State: " + str(state))

def gripper_open():
	control(146491, -1, 2)

def gripper_close():
	control(146491, 1, 2)