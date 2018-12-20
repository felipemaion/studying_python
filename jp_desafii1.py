from math import sqrt
# Dados do Desafio:
 # Por exemplo, faça um programa para calcular a velocidade que um objeto em queda livre de uma altura h
 # Mgh = mv^2/2

def velocidade_final(h):
    # mgh = mv**2 / 2
    # v^2 = 2gh
    # v = sqrt(2gh)
    g = 9.81 # m/s^2  - Terra
    return sqrt(2*g*h) # m/s

# Objeto caindo de uma altura de 1 m:
print("A velocidade que um objeto atinge o solo ao cair de 1m de altura é: {} m/s".format(velocidade_final(1)))

h = float(input("\nQual altura deseja soltar o objeto?\n>> "))
print("A velocidade que um objeto atinge o solo ao cair de {}m de altura é: {} m/s".format(h, velocidade_final(h)))
