#monta a matriz
linha = 4
coluna = 3

matriz = []
for i in range(linha):
    matriz.append([])
#preenche a matriz
for index, chave in enumerate(matriz):
    for i in range(coluna):
        matriz[index].append(round(uniform(a1, a2), 3))


