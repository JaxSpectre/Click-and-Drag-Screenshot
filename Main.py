import pyautogui
from PIL import Image
from pynput.mouse import Listener, Button
import detect_click
from pytesseract import pytesseract

def main():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract
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

    #bw
    thresh = 200
    fn = lambda x: 255 if x > thresh else 0
    im_cropped_bw = im_cropped.convert('L').point(fn, mode='1')

    im_cropped.show()
    im_cropped_bw.show()

    text = pytesseract.image_to_string(im_cropped_bw)

    print("*****************************************")
    print(text[:-1])

    






if __name__ == "__main__":
    main()