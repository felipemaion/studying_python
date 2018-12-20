class Mobile:
    def __init__(self, brand=None, color=None, screen=None):
        self.brand = brand
        self.color = color

    def keypad(self):
        if self.brand and self.color:
            print("I am a keypad mobile\nmy name is :{}\nmy color is :{}".format(self.brand, self.color))
        else:
            print("I am a keypad mobile but I don't have any name and color")

class Smart(Mobile):
    def __init__(self, screen = None,*args, **kwargs):
        Mobile.__init__(self, *args, **kwargs)
        self.screen = screen
    def touch(self):
        # self.screen = screen
        if self.brand and self.color and self.screen:
            print("I am a smart phone\nmy name is :{}\nmy color is :{}\nmy screen is :{}".format(self.brand, self.color, self.screen))

        else:
            print("I am a smart phoen, without any other information")


d = Smart(brand="iPhone", color="Grey",screen="Smart Touch")
d.touch()