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

    
    im_cropped = my_screenshot.crop((mouse_click.mouse_pos_p[0], 
                          mouse_click.mouse_pos_p[1], 
                          mouse_click.mouse_pos_r[0], 
                          mouse_click.mouse_pos_r[1]))

    my_screenshot.show()
    #im = my_screenshot
    


    # Size of the image in pixels (size of original image)
    #width, height = im.size
    '''
    # Setting the points for cropped image
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4
    '''
    # Cropped image of above dimension
    # (It will not change original image)
    #im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    #im1.show()






if __name__ == "__main__":
    main()