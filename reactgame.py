import pyautogui
### CODE TO TRY TO CLICK FAST IN THE SITE: 
# https://humanbenchmark.com/tests/reactiontime
RGB_TRIGGER = [27, 219, 113]

while True:
    pos = pyautogui.position()
    x, y = pos.x, pos.y
    # trigged = pyautogui.pixelMatchesColor(x, y, RGB_TRIGGER )
    pix = pyautogui.pixel(x,y)
    if [pix.red, pix.green, pix.blue] == RGB_TRIGGER: 
        pyautogui.mouseDown(x=x,y=y, button='left')
        pyautogui.mouseUp(x=x,y=y, button='left')
        trigged = False
