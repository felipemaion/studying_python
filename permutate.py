# https://www.codewars.com/kata/find-all-the-possible-numbers-multiple-of-3-with-the-digits-of-a-positive-integer/train/python
from itertools import permutations

def find_mult_3(number):
    number = str(number)
    output = []
    # num = [permutations(number, i) for i in range(1, len(number) + 1)]
    for i in range(1, len(number) + 1):
        num = ["".join(a) for a in permutations(number, i) if int("".join(a)) %3 ==0 and int("".join(a)) != 0]
        output.append(num)
    output = [int(item) for sublist in output for item in sublist]
    output = sorted(list(set(output)))
#     print(output)
    return [len(output), max(output)]

print(find_mult_3("345"))
print(find_mult_3(7766553322))