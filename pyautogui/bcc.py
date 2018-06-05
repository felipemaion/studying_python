import pyautogui

bcc = pyautogui.locateOnScreen('bcc2.png')
print(bcc)
pyautogui.moveTo(bcc[0]+150,bcc[1]+60)
pyautogui.click()