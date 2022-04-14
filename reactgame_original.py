from PIL import ImageGrab
import time
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt

while True:
    pos = queryMousePosition()
    rgb = ImageGrab.grab().load()[pos.x,pos.y]
    if rgb == (75, 219, 106):
        windll.user32.mouse_event(2,0,0,0,0)
        windll.user32.mouse_event(4,0,0,0,0)
        time.sleep(1)
