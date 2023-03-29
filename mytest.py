import time
from pyxboxcontroller import XboxController, XboxControllerState

REFRESH_INTERVAL:float = .5
# still_listen = True
# try:
#     controller = XboxController(0)  # Connect to controller

#     while still_listen:            
#         # Get current state of controller
#         state:XboxControllerState = controller.state
#         print(state)

#         # Check to exit loop
#         # THIS IS WERE YOU NEED TO ADD THE LOGIC
#         if state.y:  # Press start button to exit 
#            print("Y was Pressed Exiting")
#            still_listen = False

#         time.sleep(REFRESH_INTERVAL)

# # Controller not connected    
# except ConnectionError as exc:
#     raise ConnectionError("No Controller connected.") from exc

# # Something else went wrong
# except Exception as exc:
#     raise exc

# exit()

try:
	still_listen = True
	controller = XboxController(0)

	while still_listen:
		state:XboxControllerState = controller.state

		if state.y:
			print("Y was pressed. Exiting")
			still_listen = False

		while state.lb or state.rb:
			state:XboxControllerState = controller.state

			if state.lb:
				if state.lb and state.rb:
					print("Idle")
					break
				print("Rotating CCW")
			elif state.rb:
				if state.lb and state.rb:
					print("Idle")
					break
				print("Rotating CW")

			time.sleep(REFRESH_INTERVAL)

		if l_thumb_axial := state.l_thumb_x:
			print(f"Left thumbstick(axial direction): {l_thumb_axial}")

		time.sleep(REFRESH_INTERVAL)

except ConnectionError as exc:
    raise ConnectionError("No Controller connected.") from exc

# Something else went wrong
except Exception as exc:
    raise exc
	
exit()
