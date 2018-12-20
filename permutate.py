# https://www.codewars.com/kata/find-all-the-possible-numbers-multiple-of-3-with-the-digits-of-a-positive-integer/train/python
from itertools import permutations, combinations

def find_mult_3(number):
    number = list(str(number))
    candidates, output = [], []
    # Find all combinations mult. of 3.
    for i in range(1, len(number) + 1):
        candidates.append(["".join(a) for a in combinations(number, i)
                           if int("".join(list(a))) % 3 == 0 and int("".join(list(a))) != 0])
    # Remove subitems [[], [[],[],[],[]],[]] -> Flatten:
    candidates = [item for sublist in candidates for item in sublist]
    # Now permute those numbers to get all numbers.
    for candidate in candidates:
        c = str(candidate)
        output.append(["".join(list(a)) for a in permutations(c, len(c))])
    # Flatten list:
    output = [int(item) for sublist in output for item in sublist]
    # Remove Duplicates:
    output = list(set(output))
    return [len(output), max(output)]
#########################################


def find_mult_3a(number):
    number = str(number)
    output = []
    # num = [permutations(number, i) for i in range(1, len(number) + 1)]
    for i in range(1, len(number) + 1):
        num = ["".join(a) for a in permutations(number, i) if int("".join(a)) % 3 ==0 and int("".join(a)) != 0]
        output.append(num)
    output = [int(item) for sublist in output for item in sublist]
    output = sorted(list(set(output)))
    # print(output)
    return [len(output), max(output)]



#########################################

def find_mult_3b(num):
    num_list = tuple(map(int, str(num)))

    poss = set()
    for i in range(1, len(num_list) + 1):
        poss |= set(permutations(num_list, i))

    res = set()
    for p in poss:
        if p[0] != 0 and sum(p) % 3 == 0:
            res.add(p)

    res = [sum(x * 10 ** n for n, x in enumerate(p[::-1])) for p in res]
    return [len(res), max(res)]

#########################################
from collections import Counter
from functools import reduce
from itertools import combinations
from math import factorial
from operator import mul

def find_mult_3c(n):
    mul_count, digits = 0, sorted(map(int, str(n)))
    for r in range(1, len(digits) + 1):
        for comb in sorted({c for c in combinations(digits, r) if not sum(c) % 3}):
            dig_count = Counter(comb)
            mul_count += (r - dig_count.get(0, 0)) * factorial(r) // reduce(mul, map(factorial, dig_count.values()), r)
    return [mul_count, int(''.join(map(str, comb[::-1])))]
#########################################
def find_mult_3d(num):
    # your code here
    st=str(num)
    val=[ int("".join(i)) for j in range(1,len(st)+1) for i in set(permutations(st,j)) if int("".join(i))>0 and int("".join(i))%3==0  ]
    return [len(set(val)),max(val)]
#########################################

def find_mult_3e(num):
    n = [int(c) for c in str(num)]
    r = set()
    for i in range(1, len(n) + 1):
        for c in combinations(n, i):
            if sum(c) % 3 == 0:
                r |= set([int(''.join([str(i) for i in p])) for p in permutations(c) if p[0] != 0])

    return [len(r), max(r)]
#########################################
import itertools

def find_mult_3f(num):
    comblist = []
    snum = str(num)
    for i in range(1,len(snum)+1):
        #comblist.append(set(itertools.permutations(snum, i)))
        comblist.append(itertools.permutations(snum, i))
    fset = set()
    for elem in comblist:
        for e in elem:
            fset.add(e)

    result = []
    for element in fset:
        rez = ''
        for e in element:
            rez+=e
        if int(rez)%3 == 0:
            if int(rez) == 0:
                continue
            else:
                result.append(int(rez))
    a = len(list(set(result)))
    b = max(list(set(result)))
    return [a,b]
#########################################
from itertools import permutations as P

def find_mult_3g(num):
    num = str(num)
    a = set()
    for i in range(1, len(num)+1):
        for p in P(num, i):
            x = int(''.join(p))
            if x and x % 3 == 0:
                a.add(x)
    return [len(a), max(a)]
##########################################
from itertools import *

def find_mult_3h(num):
  num=str(num)
  result=[]
  div3=[]
  for i in range(1,len(num)+1):
   result.extend(list((map("".join,permutations(num,i)))))
   map(int,result)
   result = [s.lstrip("0") for s in result]
   result=list(filter(None,result))
   result=list(set(result))

  for k in result:
    if int(k)%3==0:
      div3.append((int(k)))
  return [len(div3),max(div3)]
#########################################


from functools import reduce

# get a len = 10 array with occurrences of digits
def num_to_arr(num):
    s = str(num)
    arr = [0] * 10
    for c in s:
        arr[int(c)] += 1
    return arr

# get an array of distinctive digits in an array as above
def dist_digits(arr):
    dist = []
    for i in range(0,10):
        if arr[i] > 0:
            dist.append(i)
    return dist

# get all combos given number of digits (m) and an array as above
def all_combos(arr, m):
    combos = []
    if m == 1:
        for i in range(1,10):
            if arr[i] > 0:
                combos.append([i])
        return combos

    if m > sum(arr):
        return []

    digits = dist_digits(arr)
    for d in digits:
        nextArr = [0] * 10
        for i in range(0,10):
            if i == d:
                nextArr[i] = arr[i] - 1
            if i > d:
                nextArr[i] = arr[i]
        nextCombos = all_combos(nextArr, m - 1)
        for nextComb in nextCombos:
            nextComb.append(d)
        combos.extend(nextCombos)
    return combos

# now give all combos with all possible numbers of digits that % 3 == 0
def complete_combos(arr):
    combos = []
    for i in range(1, len(arr)):
        combos.extend(all_combos(arr,i))
    return list(filter(lambda arr: sum(arr) % 3 == 0, combos))

def fact(n, zeros = 0):
    if n == 0: return 1
    if n == 1: return 1
    return (n - zeros) * fact(n - 1)

def permus(combo):
    arr = [0] * 10
    for digit in combo:
        arr[digit] += 1
    duplicates = 1
    for i in range(0,10):
        if arr[i] > 1:
            duplicates *= fact(arr[i])
    return fact(len(combo), zeros = arr[0]) // duplicates

def find_mult_3i(num):
    # your code here
    comp_combos = complete_combos(num_to_arr(num))
    return [sum(map(permus,comp_combos)), reduce(lambda x,y: x * 10 + y, comp_combos[-1])]


#########################################
#########################################
#########################################


import time

def test_time(*functions):
    for func in functions:
        start = time.time()
        func(345)
        func(7766553322)
        func(80607042)
        end = time.time()
        print("Total Time Elapsed: {} to function {}: ".format(end - start, func))
#
funcs = [find_mult_3,find_mult_3a ,find_mult_3b,find_mult_3c, find_mult_3d, find_mult_3e, find_mult_3f, find_mult_3g,
         find_mult_3h, find_mult_3i]
test_time(*funcs)
