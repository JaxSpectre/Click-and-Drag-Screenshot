import pyautogui
from PIL import Image
from pynput.mouse import Listener, Button
import detect_click

mouse_pos_p = (0,0)
mouse_pos_r = (0,0)

def on_click(x, y, button, pressed):
    if pressed:
        #get_mouse_position()
        x, y = pyautogui.position()
        print(f"Mouse position clicked: ({x}, {y})")

        mouse_pos_p = (x,y)

    else:
        x, y = pyautogui.position()
        print(f"Mouse position released: ({x}, {y})")

        mouse_pos_r = (x,y)

        listener.stop()
    #print("r",mouse_pos_r)
    #print("p",mouse_pos_p)
    print("end")


def listen():
    # Create a listener for mouse events
    global listener

    with Listener(on_click=on_click) as listener:
        listener.join()
    #return mouse_pos_p

def main():

    mouse_click = detect_click.Mouse_Click

    print("Click mouse:")
    #print(mouse_click.listen())
    
    my_screenshot = pyautogui.screenshot()

    print("mouse released")
    print("height", my_screenshot.height)
    print("width", my_screenshot.width)
    '''
    im_cropped = my_screenshot.crop((detect_click.mouse_pos_p[0], 
                          detect_click.mouse_pos_p[1], 
                          detect_click.mouse_pos_r[0], 
                          detect_click.mouse_pos_r[1]))
    '''
    
    im_crop2 = my_screenshot.crop((0,0,100,100))
    print("mouse pos",mouse_pos_p[0])
    im_crop2.show()
    #im = my_screenshot
    






if __name__ == "__main__":
    main()