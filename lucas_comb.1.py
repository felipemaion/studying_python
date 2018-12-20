from itertools import permutations
lugares = [None]*4
lugares[0] = 1
lugares[2] = 2
all_comb = list(permutations(lugares,4))
cp = all_comb[:]
for comb in all_comb:
    if comb.index(1) == (comb.index(2) + 1) or comb.index(1) == (comb.index(2) - 1):
        print(cp.remove(comb))
        print("Removing:",comb)
    else:
        print(comb.index(1), comb.index(2))
print(len(cp))
print(cp)
