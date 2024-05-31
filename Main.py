import pyautogui
from PIL import Image
from pynput.mouse import Listener, Button
import detect_click




def main():

    mouse_click = detect_click.Mouse_Click

    print("Click mouse:")
    mouse_click.listen()

    my_screenshot = pyautogui.screenshot()

    print("mouse released")
    print("height", my_screenshot.height)
    print("width", my_screenshot.width)
    
    im_cropped = my_screenshot.crop((detect_click.mouse_pos_p[0], 
                          detect_click.mouse_pos_p[1], 
                          detect_click.mouse_pos_r[0], 
                          detect_click.mouse_pos_r[1]))

    
    im_crop2 = my_screenshot.crop((0,0,100,100))
    print("mouse",detect_click.mouse_pos_p[0])
    im_crop2.show()
    #im = my_screenshot
    






if __name__ == "__main__":
    main()