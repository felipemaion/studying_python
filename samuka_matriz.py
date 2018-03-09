# Programinha para gerar resultados aleatórios em um jogo de Loteca.
# 14 jogos, cada linha um jogo... resultados Time A, Time B, ou Empate.


import random

def cria_matriz():
     return list("1"*42)

def imprimi_matriz(matriz, visiveis = []):
    for i in range(0,len(matriz)-2, 3):
        a,b,c = matriz[i], matriz[i + 1], matriz[i + 2]
        a = "_" if i in visiveis else a
        b = "_" if i+1 in visiveis else b
        c = "_" if i+2 in visiveis else c

        print("{} {} {}".format(a,b,c))

def gerar_aleatorios():
    aleatorios = []
    bias = 0

    for i in range(14):
        chute = random.sample(range(0+bias,3+bias),2)
        aleatorios.append(chute)
        bias += 3
    return [item for sublist in aleatorios for item in sublist]


matriz = cria_matriz()
# imprimi_matriz(matriz)
aleatorios = gerar_aleatorios()
# print(aleatorios)
imprimi_matriz(matriz, aleatorios)