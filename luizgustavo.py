# -*- coding: utf-8 -*-
from tkinter import *



def calculo():
    try:
        print(en1.get())
        print(en2.get())
        M = float(en1.get())
        # 5.9722e24 == Terra
        N = 6.67408e-11
        d = float(en2.get())
        # 6371000 == Terra
        g = (N * M) / d ** 2
        la5 = Label(janela, text=g)
        la5.place(x=20, y=200)
        print(g)
        return M, N, d, g, la5
    except ValueError:
        la5 = Label(janela, text="Valor incorreto!")
        la5.place(x=20, y=200)

    return la5


janela = Tk()
janela.title("CAMPO GRAVITACIONAL")
janela["bg"] = "black"

la1 = Label(janela, text="Esse programa calcula o campo gravitacional de um astro")
la1.place(x=20, y=20)

la2 = Label(janela, text="Digite a massa do astro: (kg)")
la2.place(x=20, y=50)

en1 = Entry(janela, width=24)
en1.place(x=20, y=80)

la3 = Label(janela, text="Digite o raio equatorial do astro:(m)")
la3.place(x=20, y=110)

en2 = Entry(janela, width=24)
en2.place(x=20, y=140)

la4 = Label(janela, text="O campo gravitacional do astro é, em m/s2:")
la4.place(x=20, y=170)

bt1 = Button(janela, width=10, text="OK", command=calculo)
bt1.place(x=20, y=230)
bt1["bg"] = "yellow"

janela.configure(background="white")
janela.geometry("450x300+100+100")
janela.mainloop()