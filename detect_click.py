import pyautogui
from pynput.mouse import Listener



class Mouse_Click:

    mouse_pos_p = (0,0)
    mouse_pos_r = (0,0)


    def on_click(x, y, button, pressed):
        if pressed:
            #get_mouse_position()
            x, y = pyautogui.position()
            #print(f"Mouse position: ({x}, {y})")
            mouse_pos_p_x = x
            mouse_pos_p_y = y
            mouse_pos_p = (x,y)
        else:
            x, y = pyautogui.position()
            print(f"Mouse position: ({x}, {y})")
            mouse_pos_r_x = x
            mouse_pos_r_y = y
            mouse_pos_r = (x,y)

            listener.stop()


    def listen():
        # Create a listener for mouse events
        global listener
        with Listener(on_click=Mouse_Click.on_click) as listener:
            listener.join()
        
