# https://www.codewars.com/kata/find-all-the-possible-numbers-multiple-of-3-with-the-digits-of-a-positive-integer/train/python
from itertools import permutations, combinations

def find_mult_3(number):
    number = str(number)
    output = []
    # num = [permutations(number, i) for i in range(1, len(number) + 1)]
    for i in range(1, len(number) + 1):
        num = ["".join(a) for a in permutations(number, i) if int("".join(a)) % 3 ==0 and int("".join(a)) != 0]
        output.append(num)
    output = [int(item) for sublist in output for item in sublist]
    output = sorted(list(set(output)))
#     print(output)
    return [len(output), max(output)]




def find_mult_3a(number):
    number = list(str(number))
    candidates = []
    for i in range(1,len(number) + 1):
        comb = [int("".join(list(a))) for a in combinations(number, i) if int("".join(list(a))) % 3 == 0]
        print(comb)


print(find_mult_3("345"))
print(find_mult_3(7766553322))


class Multiply:
    def __init__(self):
        self.operation = "Multiplication"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{}".format(self.operation,a,b))

class Add:
    def __init__(self):
        self.operation = "Sum"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{}".format(self.operation,a,b))

class Subtraction:
    def __init__(self):
        self.operation = "Subtraction"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{}".format(self.operation,a,b))

class Division:
    def __init__(self):
        self.operation = "Division"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{}".format(self.operation,a,b))

calculator={"1":Multiply(), "2":Add(), "3":Subtraction(), "4":Division()}
a = float(input("Number 1 >>"))
operation = input("Operation:\n \t[1] - Multiply\n\t[2] - Addition\n\t[3] - Subtraction\n\t[4] - Division")
b = float(input("Number 2 >>"))

calculator[operation].call(a,b)