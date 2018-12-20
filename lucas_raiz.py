def raiz(n, grau=2):
    # Função que irá mostrar a raiz bonitinha...

    # Para mostrar mais bonitinho as raizes
    if grau == 2:
        simbolo = "\u00B2\u221A"
    elif grau == 3:
        simbolo = "\u00B3\u221A"
    elif grau == 4:
        simbolo = "\u2074\u221A"
    elif grau == 5:
        simbolo = "\u2075\u221A"
    elif grau == 6:
        simbolo = "\u2076\u221A"
    elif grau == 7:
        simbolo = "\u2077\u221A"
    elif grau == 8:
        simbolo = "\u2078\u221A"
    elif grau == 9:
        simbolo = "\u2079\u221A"
    else:
        simbolo = '\u221A'
    # reduzir() irá retornar o número de fora e dentro da raiz n:
    coeficiente, reduzido = reduzir(n,grau)
    if coeficiente == 1:
        return '{}{}'.format(simbolo,reduzido)
    elif reduzido == 1:
        return coeficiente
    else:
        return "{} {}({})".format(coeficiente, simbolo, reduzido)

def fatorar(fator):
    # função para fatorar 
    lista = []
    for fa in range(2, fator+1):
        while fator % fa == 0:
            fator = fator / fa
            lista.append(fa)
    return lista

def reduzir(numero,grau=2):
    # Função que irá agrupar os fatores em grupos de "grau"
    lista_fatores = fatorar(numero)
    lista_unica = list(set(lista_fatores))
    fora = []
    dentro = []
    for fator in lista_unica:
        multiplicidade = lista_fatores.count(fator)
        fora.append(fator**(multiplicidade // grau))
        dentro.append(fator**(multiplicidade % grau))
    # Calcula o produto da lista:
    fora = eval('*'.join(str(item) for item in fora))
    dentro = eval('*'.join(str(item) for item in dentro))
    return fora, dentro


print("Testes:")
print(raiz(1024))
print(raiz(1024,3))
print(raiz(1024,4))
print(raiz(1024,5))
print(raiz(1024,6))
print(raiz(1024,7))
print(raiz(1024,8))
print(raiz(1024,9))
print(raiz(8,3))
print(raiz(8,2))
print(raiz(10,2))

print("ok... \n")
x = int(input('Digite o número: '))
try: 
    grau = int(input("Digita o grau da raiz (padrão = 2):"))
except ValueError:
    grau = 2


print(raiz(x,grau))




# from math import sqrt

# def reduced_sqrt(n):
#     root = int(sqrt(n))
#     for factor_root in range(root, 1, -1):
#         factor = factor_root * factor_root
#         if n % factor == 0:
#             reduced = n // factor
#             return (factor_root, reduced)
#     return (1, n)


# def my_sqrt(n):
#     coefficient, reduced = reduced_sqrt(n)
#     if coefficient == 1:
#         return '\u221A{}'.format(reduced)
#     elif reduced == 1:
#         return coefficient
#     else:
#         return "{}{}{}".format(coefficient, '\u221A', reduced)