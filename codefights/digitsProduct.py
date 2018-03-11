# https://codefights.com/arcade/intro/level-12/NJJhENpgheFRQbPRA

# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

# Example

# For product = 12, the output should be
# digitsProduct(product) = 26;
# For product = 19, the output should be
# digitsProduct(product) = -1.

# MY SOLUTION DUE TO TIME ELAPSED:
def digitsProduct(product):
    for number in range(1, 9999):
        num = [int(x) for x in list(str(number))]
        mult = eval('*'.join(str(digit) for digit in num))
        if mult == product:
            return int("".join([str(x) for x in num]))
    return -1

#
# def digitsProduct(product):
#
#     if is_prime(product):
#         return -1
#     found = False
#     number = 1
#     while not found:
#         num = [int(x) for x in list(str(number))]
#         mult = eval('*'.join(str(digit) for digit in num))
#         if mult == product:
#             return int("".join([str(x) for x in num]))
#         number += 1
#
#
#
# def is_prime(a):
#     if a < 2:
#         return False
#     elif a!=2 and a % 2 == 0:
#         return False
#     else:
#         return all (a % i for i in range(3, int(a**0.5)+1) )

 # Input: 125, Output: 555, Input: 343, Output: 777
print(digitsProduct(12))
print(digitsProduct(125))
print(digitsProduct(343))
print(digitsProduct(9))
