import random
def jogar():
    numeros = [num for num in range(1,61)]
    random.shuffle(numeros)
    return numeros[:6]


print ("Sugestão de jogo para a Mega Sena:", jogar())