#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import sys
from math import sqrt
from time import sleep
import os
cores = { "sem":"\033[m",
	        "branco":"\033[90;1m",
          "vermelho":"\033[91;1m",
          "verde":"\033[92;1m",
          "amarelo":"\033[93;1m",
          "azul":"\033[94;1m",
          "lilas":"\033[95;1m",
          "azulclaro":"\033[96;1m",
          "cinza":"\033[97;1m"
          }
####////////////////////////#################

def reduced_sqrt(n):
    """Return most reduced form of square root
    of n as the couple (coefficient, reduced_form)
    """
    root = int(sqrt(n))

    for factor_root in range(root, 1, -1):
        factor = factor_root * factor_root
        if n % factor == 0:
            reduced = n // factor
            return (factor_root, reduced)

    return (1, n)


def my_sqrt(n):
    coefficient, reduced = reduced_sqrt(n)
    if coefficient == 1:
        # print('\u221A', reduced)
        return '\u221A{}'.format(reduced)
    elif reduced == 1:
        # print(coefficient)
        return coefficient
    else:
        # print(coefficient, '\u221A', reduced)
        return "{}{}{}".format(coefficient, '\u221A', reduced)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenha_cabecalho():
    print("=•" * 19)
    print("{}Resolução de equações do segundo grau{}".format(cores["verde"], cores["sem"]))
    print("=•" * 19)
    # sleep(0.6)
    print("==" * 19)
    print("Informe as variáveis: A, B e C de: \n{}A{}x² + {}B{}x + {}C{} = 0".format(cores["lilas"], cores["sem"],
                                                                                     cores["amarelo"], cores["sem"],
                                                                                     cores["azulclaro"], cores["sem"]))
    print("==" * 19)

def entrada_dados():
    # sleep(0.5)
    entrada_valida = False
    while not entrada_valida:
        try:
            a = int(input("Valor de \033[95;1mA:\033[m "))
            # sleep(0.5)
            b = int(input("valor de \033[93;1mB:\033[m "))
            # sleep(0.5)
            c = int(input("valor de \033[96;1mC:\033[m "))
            entrada_valida = True
        except ValueError:
            print("Erro ao converter para número...")
            entrada_valida = False
    return a,b,c

def delta(a, b, c):
    print("Calculando o delta...")
    return ((b**2) - 4*a*c)


def eq2grau(a = None, b = None, c = None):
    desenha_cabecalho()
    if not a and not b and not c:
        a,b,c = entrada_dados()
    x1,x2 =0,0
    ### Verifica se é de segundo grau:
    if a == 0:
        # bx + c = 0
        x = -c/b
        print("Equação de Primeiro Grau: X = {}".format(x))
        return x
    imaginario = False
    meu_delta = delta(a,b,c) # Procure calcular uma única vez, para não consumir muito processamento.
    if meu_delta < 0:
        #sleep(0.5)
        print("=="*19)
        print("{}Essa equação possui raízes complexas{}".format(cores["vermelho"], cores["sem"]))
        #sleep(0.5)
        print("{}Seu delta vale:{}{}{}{}".format(cores["verde"], cores["sem"], cores["lilas"], delta(a,b,c), cores["sem"]))
        print("=="*19)
        imaginario = True
        meu_delta *= -1 # Inverte o Delta.
    if sqrt(meu_delta) % 1 != 0:
        print("="*38)
        print("Delta sem raiz exata!")
        print("\033[93;1m==\033[m"*19)
        print("{}	O valor do delta é:{} {}{}{}".format(cores["azul"], cores["sem"], cores["azulclaro"], delta(a,b,c), cores["sem"]))
        print("\033[93;1m==\033[m"*19)
        print("\033[93;1m==\033[m"*19)
    else:
        print("{}	O valor do delta é:{} {}{}{}".format(cores["azul"], cores["sem"], cores["azulclaro"], delta(a,b,c), cores["sem"]))
        print("\033[93;1m==\033[m"*19)
        print("Continuando...")
    minha_raiz = my_sqrt(meu_delta)
    num, raiz = reduced_sqrt(meu_delta)
    eh_numerica = isinstance(minha_raiz, (int, float))
    if not imaginario and eh_numerica:
        x1 = "{}".format(-b/(2*a) + minha_raiz/(2*a))
        x2 = "{}".format(-b/(2*a) - minha_raiz/(2*a))
    if not imaginario and not eh_numerica:
        x1 = "{} + \u221A({})/{}".format(-b / (2 * a), raiz, num / (2 * a))
        x2 = "{} - \u221A({})/{}".format(-b / (2 * a), raiz, num / (2 * a))
    if imaginario:
        x1 = "{} + \u221A({}){}i{}{}/{}{}".format(-b/(2*a),raiz, cores['amarelo'],cores['sem'], cores["lilas"],num/(2*a),cores['sem'])
        x2 = "{} - \u221A({}){}i{}{}/{}{}".format(-b/(2*a), raiz, cores['amarelo'],cores['sem'],cores["lilas"], num/(2*a),cores['sem'])
    print("\n X1 vale: {}{}{}".format(cores["lilas"], x1, cores["sem"]))
    print("\n X2 vale: {}{}{}".format(cores["lilas"], x2, cores["sem"]))
    return [x1,x2]



if __name__ == "__main__":
    clear_screen()
    eq2grau()
# eq2grau(1,2,-3) # Caso queira chamar a função para calcular com a,b,c.



