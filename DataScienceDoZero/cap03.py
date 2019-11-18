#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from collections import defaultdict, Counter
import re
import random


### Gráfico de Linha Simples
years = [1950, 1960, 1970, 1980,1990,2000,2010]
gdp =[300.2, 543.3, 1075.9, 2862.5, 5962.5, 10289.7, 14958.3]



plt.title('GDP Nominal')

plt.ylabel("Bilhões de $")
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')


plt.show()



### Gráfico de Barra

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

# Barras possuem o tamanho padrao de 0.8, então adicionar 0.1 as 
# coordenadas à esquerda para q cada barra seja centralizada

xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)

plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")

# nomear o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()

## Histograma:

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10*10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([ x- 4 for x in histogram.keys()],
       histogram.values(),
       8)
plt.axis([-5,105,0,5])
plt.xticks([10*i for i in range(11)])
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas do Teste 1")
plt.show()