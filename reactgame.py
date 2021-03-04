import pyautogui
from PIL import ImageGrab
### CODE TO TRY TO CLICK FAST IN THE SITE: 
# https://humanbenchmark.com/tests/reactiontime
RGB_TRIGGER = (27, 219, 113, 255)

while True:
    pos = pyautogui.position()
    x, y = pos.x, pos.y
    # trigged = pyautogui.pixelMatchesColor(x, y, RGB_TRIGGER )
    # pix = pyautogui.pixel(x,y)
    bbox=(x,y,x+1,y+1)
    # print(f"{x}, {y}, { bbox }")
    pix = ImageGrab.grab(bbox=bbox).load()[0,0]
    # print(pix)
    if pix == RGB_TRIGGER: 
        pyautogui.mouseDown(x=x,y=y, button='left')
        pyautogui.mouseUp(x=x,y=y, button='left')
        # trigged = False
