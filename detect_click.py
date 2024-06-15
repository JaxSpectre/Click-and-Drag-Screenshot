import pyautogui
from pynput.mouse import Listener
import Main



class Mouse_Click:
    mouse_pos_p = (0,0)
    mouse_pos_r = (0,0)


    def on_click(x, y, button, pressed):
        if pressed:
            #get_mouse_position()
            x, y = pyautogui.position()
            print(f"Mouse position clicked: ({x}, {y})")

            Mouse_Click.mouse_pos_p = (x,y)
            Main.mouse_pos_p = (x,y)

        else:
            x, y = pyautogui.position()
            print(f"Mouse position released: ({x}, {y})")

            Mouse_Click.mouse_pos_r = (x,y)
            Main.mouse_pos_r = (x,y)

            listener.stop()
        #print("r",mouse_pos_r)
        #print("p",mouse_pos_p)
        print("end")


    def listen():
        # Create a listener for mouse events
        global listener

        with Listener(on_click=Mouse_Click.on_click) as listener:
            listener.join()
        #return mouse_pos_p
        
