import pyautogui

# Depending on your program, pyautogui can "go rogue".
# As a failsafe, we may move the mouse to the upper-left
# corner of the screen to halt.
pyautogui.FAILSAFE = True

# The location of th emouse cursor is provided as an (x,y) pair.
# This value of x/y is based on monitor resolution.

# Obtain the coordinates of computer screen via:
#print(pyautogui.size())

# Moving the mouse to a specific location:
#pyautogui.moveTo(100, 100, duration=0.25)

# Moving the mouse to a specific location (in a loop):
#for i in range(10):
# 	pyautogui.moveTo(100, 100, duration=0.25)
# 	pyautogui.moveTo(200, 100, duration=0.25)
# 	pyautogui.moveTo(200, 200, duration=0.25)
# 	pyautogui.moveTo(100, 200, duration=0.25)

# Move the mouse relative to a specific location:
#pyautogui.moveRel(100, 0, duration=0.25)

# Getting the mouse position.
print(pyautogui.position())

# Clicking the mouse:
# The click function takes two arguments (x,y) that
# correspond to the (x,y) positions on the screen.
#pyautogui.click(167, 38)

# Dragging the mouse (moving the mouse while simultaneously clicking).
# moveTo and moveRel
# dragTo and dragRel
#pyautogui.moveTo(103, 211, duration=0.25)
#pyautogui.dragTo(303, 211, duration=0.25)

# Scrolling the mouse
pyautogui.scroll(200)
