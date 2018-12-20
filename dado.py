from tkinter import *
import random

jan = Tk()
jan.geometry('200x200')
jan['bg'] = 'black'

def dado():
    n = int(lado.get())
    r = random.randint(1,n)
    lab['text']= r

lab = Label(jan,text = 'Resultado')
lab.place(x = 10, y = 50)
lado = Entry(jan)
lado.place(x = 10, y = 10)

lado.bind('<Return>',lambda event: dado())

jan.mainloop()
