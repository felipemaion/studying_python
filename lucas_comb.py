#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
lugares = [0]*10
lugares[0] = 1
lugares[2] = 2
all_comb = list(permutations(lugares,10))
all_comb = list(set(all_comb))
print("Possibilidades Totais:",len(all_comb))
cp = all_comb[:]
for comb in sorted(all_comb[:]):
    
    if comb.index(1) == (comb.index(2) + 1) or comb.index(1) == (comb.index(2) - 1):
        cp.remove(comb)
        print("Remover:",comb)
    # input()
    else:
        print("\t",comb)
print("Possibilidades com pelo menos 1 espaço entre os carros:", len(cp))
# print(cp)
