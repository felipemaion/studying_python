import random
def rolar_dados(lados=6, quantidade=1):
    dados = []
    for dado in range(quantidade):
        dados.append(random.randrange(1,lados))
    return dados

print(rolar_dados())
print(rolar_dados(8,1))
print(rolar_dados(8,2))
print(rolar_dados(8,3))
print(rolar_dados(10,3))
