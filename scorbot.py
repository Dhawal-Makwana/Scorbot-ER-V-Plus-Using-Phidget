import keyboard
from homing import homing
from manual import manual
from by_angles import by_angles,draw
from functions import gripper_close, gripper_open
from digonal import Run
from digonal2 import Run2
from digonal3 import Run3
from digonal4 import Run4

import sys

print("=== ScorBot-ER V + ===")
print("_______Welcome_______")

print("Key H :Home Position")
print("Key M :Manual Mode")
print("Key P :Pick and Place by Angles")
print("Key S :Draw a Square")
print("Key K: Draw a Kite")


# ScorBot Start Code: Final Program
while True:

	if keyboard.read_key() == "H":
			print("Home")
			homing()
			print("Press M for Manual Mode")
			# sys.exit()
	
	if keyboard.read_key() == "M":
			print("Manual Mode")
			manual()
			
			# sys.exit()
	
	if keyboard.read_key() == "P":
			print("Pick and Place by Angles\n")
			print("Pick Position Define:")
			gripper_open()
			by_angles()
			gripper_close()
			print("Place Position Define:\n")
			by_angles()
			gripper_open()
			homing()
			sys.exit()
   
	if keyboard.read_key() == "S":
		print("Draw a Square")
		draw()
	
	if keyboard.read_key() == "K":
		print("Draw a kite")
		Run()
		Run2()
		Run3()
		Run4()
