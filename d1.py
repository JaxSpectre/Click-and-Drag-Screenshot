import pyautogui
from pynput.mouse import Listener

# Function to get mouse position when clicked
def get_mouse_position():
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})")

# Call the function to start getting mouse position


mouse_pos_p = (0,0)
mouse_pos_r = (0,0)

mouse_released = False

def on_click(x, y, button, pressed):
    if pressed:
        #get_mouse_position()
        x, y = pyautogui.position()
        #print(f"Mouse position: ({x}, {y})")
        mouse_pos_p = (x,y)
        print(mouse_pos_p)
    else:
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})")
        mouse_pos_r = (x,y)
        mouse_released = True
        Listener.stop()


def listen():
    # Create a listener for mouse events
    with Listener(on_click=on_click) as listener:
        listener.join()
    
