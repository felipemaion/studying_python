import pyautogui
import time
import timeit

RGB_TRIGGER = [27, 219, 113]

# trigger_time = 0.1
# pyautogui.PAUSE = 0.01
# pos = pyautogui.position()
# x, y = pos.x, pos.y
# trigged = pyautogui.pixelMatchesColor(x, y, RGB_TRIGGER )
while True:
    # while not trigged:
    pos = pyautogui.position()
    x, y = pos.x, pos.y
    trigged = pyautogui.pixelMatchesColor(x, y, RGB_TRIGGER )
    # print(x,y,trigged, pyautogui.pixel(x,y ) )
    # time.sleep(trigger_time)
    if trigged:
        # start = timeit.default_timer()
        # print("TRIGGED!")

        # rgb(75, 219, 106)
        # pyautogui.click(x=x,y=y, button='left')
        pyautogui.mouseDown(x=x+1,y=y+1, button='left')
        pyautogui.mouseUp(x=x+2,y=y+2, button='left')

        # stop = timeit.default_timer()
        # print('Time: ', stop - start) 
        # pyautogui.click(x=x,y=y)
        # # print("TRIGGED!")
        # time.sleep(2)
        trigged = False
    # trigger_time += 0.1
    # print(f"Trigger:{trigger_time}")