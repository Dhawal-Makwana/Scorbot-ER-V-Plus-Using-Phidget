from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.Encoder import *
import time


def Function(serial,):
    dcMotor0 = DCMotor()
    encoder0 = Encoder()
    dcMotor0.setDeviceSerialNumber(serial)
    encoder0.setDeviceSerialNumber(serial)
    position=encoder0.getPosition()

    
    dcMotor0.openWaitForAttachment(5000)
    encoder0.openWaitForAttachment(5000)
    dcMotor0.setTargetVelocity(1)
    
        
    dcMotor0.close()
    encoder0.close()


def onStateChange(self, state):
	print("State: " + str(state))