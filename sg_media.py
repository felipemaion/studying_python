#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Digite três valores:")
val1 = int(input(": "))
val2 = int(input(": "))
val3 = int(input(": "))

def media(arg1, arg2, arg3):
    lista = []
    lista.append(arg1)
    lista.append(arg2)
    lista.append(arg3)
    media = sum(lista) / len(lista)
    lista = sorted(lista)
    print(lista)
    print(media)

media(val1, val2, val3)


def my_media(tamanho):
    valores = []
    for i,_ in enumerate(range(tamanho)):
        val = int(input("valor["+ str(i) + "]:"))
        valores.append(val)
    media = sum(valores)/len(valores)
    valores.sort()
    print (valores)
    print (media)
    return valores, media

my_media(3)
