import pyautogui
from PIL import Image
from pynput.mouse import Listener, Button
import d1




def main():
    print("Click mouse:")
    d1.Mouse_Click.listen()

    my_screenshot = pyautogui.screenshot()

    print("mouse released")

    #im = pyautogui.screenshot(region=(click_p.x,click_p.y, click_r.x, click_r.y))
    #im.show()
    #im = my_screenshot
    



    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
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