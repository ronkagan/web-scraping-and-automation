import  pyautogui, time
	#time.sleep is going to allow the computer to wait five seconds before moving
	#onto the next action
time.sleep(5)
	#pyautogui.click makes the computer click, which focuses action on any newly
	#opened window
pyautogui.click()
	#this is the number of pixels in terms of a distance for a cursor to move
distance = 400
	#while the distance is strictly greater than 0, we will do a few things
	#dragRel is a function that defined by the pyautogui library, which takes 3 params:
	#the X and Y amounts of distance to move as well as the time in which to move
	#X position of distance is 400 pixels right, the Y will not move all in .2 seconds
	#Don't move along the X axis in the second isntance, just Y calling back to distance
	#then we decrease the distance VAR from 400 to 350 and repeat
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2)
	distance = distance - 50
	pyautogui.dragRel(0, distance, duration=0.2)
	pyautogui.dragRel(-distance, 0, duration=0.2)
	distance = distance - 50
	pyautogui.dragRel(0, -distance, duration=0.2)