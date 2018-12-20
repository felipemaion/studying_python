import itertools
length = input("[=] Please choose the length of the letters:\n>>>")
contains = input("[=] Please type in the choosen letters:\n>>>")
# generate = list(map("".join, itertools.product(contains,repeat=int(length))))
print(generate)
print(len(generate))
for i in range(int(length)+1):
    for group in itertools.combinations(contains, i):
        print(''.join(group))
#
# x = float(input("What is the cost of your meal? "))
#
# y = input("What is the sales tax in your area?  %\rWhat is the sales tax in your area?")
#
# y = float(y) / 100
# cost = (x + (x * y))
# print("The cost of your food is ", cost)