import pyautogui
import time

# Uses PyWin32 http://timgolden.me.uk/pywin32-docs/win32clipboard.html
import win32clipboard
import win32con

def get_clipboard():
	win32clipboard.OpenClipboard()
    # 
	if (win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB)):
		data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
		data_format = win32clipboard.GetClipboardFormatName(win32clipboard.CF_DIB)
	else:
		try:
			data = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
			data_format = win32clipboard.GetClipboardFormatName(win32con.CF_UNICODETEXT)
		except:
			data = ""
	win32clipboard.CloseClipboard()
	return data, data_format

def set_clipboard(text, data_t=None):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	if data_t:
		win32clipboard.SetClipboardData(data_t, text)
	else:
		win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, str(text))
	# win32clipboard.SetClipboardData(str(text), win32clipboard.CF_UNICODETEXT)
	win32clipboard.CloseClipboard()

while True:
    bcc = pyautogui.locateOnScreen('C:\\OneDrive\\Documentos\\Documentos Felipe\\programs\\ruby\\Python\\PyCharmProjects\\testes\\pyautogui\\bcc8.png', grayscale = True)
    # print(bcc)
    if bcc:
        current_clipboard, current_format = get_clipboard()
        # print(current_clipboard)
        current_pos = pyautogui.position()
        pyautogui.moveTo(bcc[0]+150,bcc[1]+15)
        pyautogui.click()
        # pyautogui.typewrite('fmaionbollhoff@gmail.com', interval=0)
        set_clipboard("fmaionbollhoff@gmail.com")
        pyautogui.keyDown('ctrl')
        pyautogui.press(['v'])
        pyautogui.keyUp('ctrl')
        pyautogui.moveTo(current_pos)
        set_clipboard(current_clipboard)
    # pyautogui.PAUSE = 0.5
    # time.sleep(0.5)
    