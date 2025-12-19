from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import time
import sys
import keyboard
from functions import control
from homing import homing
def manual():
	# Start Manual Mode
    
	print("===Manual Mode Activated===\n")
	print("Key R/r: Right Turn")
	print("Key L/l: Left Turn")
	print("Key U/u: moving Up")
	print("Key D/d: moving Down")
	print("Key F/f: moving Forward")
	print("Key B/b: moving Backward")
	print("Key o/c: Open or Close Gripper")
	print("Key 0: End Manual Mode\n")
	print("Key Q/q: Gripper forward")
	print("Key W/w: gripper backward")

	while True:
		# Base Movement: Left Right
		if keyboard.read_key() == "L":
			print("go Left")
			control(146552, -1, 2)
			# sys.exit()
		if keyboard.read_key() == "R":
			print("go Right")
			control(146552, 1, 2)
			# sys.exit()
		if keyboard.read_key() == "l":
			print("go little Left")
			control(146552, -1, 1)
			# sys.exit()
		if keyboard.read_key() == "r":
			print("go little Right")
			control(146552, 1, 1)
			# sys.exit()
		
		# Elbow Movement: Up Down
		if keyboard.read_key() == "U":
			print("go Up")
			control(146520, 1, 2)
			# sys.exit()
		if keyboard.read_key() == "D":
			print("go Down")
			control(146520, -1, 2)
			# sys.exit()
		if keyboard.read_key() == "u":
			print("go little Up")
			control(146520, 1, 1)
			# sys.exit()
		if keyboard.read_key() == "d":
			print("go little Down")
			control(146520, -1, 1)
			# sys.exit()

		# Shoulder Movement: Forward Backward
		if keyboard.read_key() == "F":
			print("go Forward")
			control(146627, -1, 2)
			# sys.exit()
		if keyboard.read_key() == "B":
			print("go Backward")
			control(146627, 1, 4)
			# sys.exit()
		if keyboard.read_key() == "f":
			print("go little Forward")
			control(146627, -1, 1)
			# sys.exit()
		if keyboard.read_key() == "b":
			print("go little Backward")
			control(146627, 1, 1)
			# sys.exit()

		# Gripper: Open Close
		if keyboard.read_key() == "o":
			print("Open Gripper")
			control(146491, -1, 2)
			# sys.exit()
		if keyboard.read_key() == "c":
			print("Close Gripper")
			control(146491, 1, 2)
			# sys.exit()
		if keyboard.read_key() == "O":
			print("Open Gripper")
			control(146491, -1, 2)
			# sys.exit()
		if keyboard.read_key() == "C":
			print("Close Gripper")
			control(146491, 1, 2)
			# sys.exit()
		
		if keyboard.read_key() == "H":
				print("Home")
				homing()
				# sys.exit()
    # Wrist Movement: Forward Backward
		if keyboard.read_key() == "Q":
			print("go Forward")
			control(146680, -1, 2)
			# sys.exit()
		if keyboard.read_key() == "W":
			print("go Backward")
			control(146680, 1, 2)
			# sys.exit()
		if keyboard.read_key() == "q":
			print("go little Forward")
			control(146680, -1, 1)
			# sys.exit()
		if keyboard.read_key() == "w":
			print("go little Backward")
			control(146680, 1, 1)
			# sys.exit()

		
		# End Program
		if keyboard.read_key() == "0":
			print("Finish Program")
			sys.exit()
