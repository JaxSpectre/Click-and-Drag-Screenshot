import pyautogui
from PIL import Image
from pynput.mouse import Listener, Button
import detect_click



class abc:
    mouse_pos_p = (0,0)
    mouse_pos_r = (0,0)

    def on_click(x, y, button, pressed):
        if pressed:
            #get_mouse_position()
            x, y = pyautogui.position()
            print(f"Mouse position clicked: ({x}, {y})")

            abc.mouse_pos_p = (x,y)

        else:
            x, y = pyautogui.position()
            print(f"Mouse position released: ({x}, {y})")

            abc.mouse_pos_r = (x,y)

            listener.stop()
        #print("r",mouse_pos_r)
        #print("p",mouse_pos_p)
        print("end")


    def listen():
        # Create a listener for mouse events
        global listener

        with Listener(on_click=abc.on_click) as listener:
            listener.join()
        #return mouse_pos_p

def main():

    screen_size = pyautogui.size()
    my_screenshot = pyautogui.screenshot()
    mouse_pos_p = (0,0)
    mouse_pos_r = (0,0)
    detect_click.Mouse_Click.listen()

    mouse_pos_p = detect_click.Mouse_Click.mouse_pos_p

    print("Click mouse1: ", mouse_pos_p)
    #print(mouse_click.listen())
    
    my_screenshot = pyautogui.screenshot()

    print("mouse released")
    mouse_pos_r = detect_click.Mouse_Click.mouse_pos_r
    print("Click mouse2: ", mouse_pos_r)

    print("height", my_screenshot.height)
    print("width", my_screenshot.width)

    
    im_cropped = my_screenshot.crop((
                          mouse_pos_p[0], 
                          mouse_pos_p[1], 
                          mouse_pos_r[0], 
                          mouse_pos_r[1]
                          ))
    
    
    im_crop2 = my_screenshot.crop((0,0,100,100))

    im_cropped.show()
    #im = my_screenshot
    






if __name__ == "__main__":
    main()