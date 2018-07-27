import pyautogui
import time
while True:
    bcc = pyautogui.locateOnScreen('bcc7.png')
    # print(bcc)
    if bcc:
        current_pos = pyautogui.position()
        pyautogui.moveTo(bcc[0]+150,bcc[1]+15)
        pyautogui.click()
        pyautogui.typewrite('fmaionbollhoff@gmail.com')
        pyautogui.moveTo(current_pos)
    # pyautogui.PAUSE = 0.5
    # time.sleep(1)
    