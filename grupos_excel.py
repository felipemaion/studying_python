from itertools import combinations

tarefas = {1:3, 2:4, 3:6, 4:5, 5:2}

def grupos(tarefas, grupos, criterio):
    comb = []
    for g in range(1,grupos):
        comb.append(list(combinations(tarefas.values(), g)) )
    print(comb)
    possiveis = []
    for c in comb:
        print(c)
        if sum(c) < criterio:
            possiveis.append(c)
    print(c)
    return c