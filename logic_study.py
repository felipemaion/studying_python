count = 0
for i in range(-1,2):
    for j in range(-1,2):
        if i != 0 or j != 0:
            print("i or j -> i:{}; j:{}".format(i,j))
            count += 1
    print(count)
print("\n")

count = 0
for i in range(-1,2):
    for j in range(-1,2):
        if i == 0 and j == 0:
            pass
        else:
             print("i | j -> i:{}; j:{}".format(i,j))
             count += 1
    print(count)
print("\n")

count = 0
for i in range(-1, 2):
    for j in range(-1, 2):
        if [i, j] != [0,0]:
            print("[i,j] -> i:{}; j:{}".format(i,j))
            count += 1
print(count)
print("\n")

count =0
for i in range(-1,2):
    for j in range(-1,2):
        if i != 0 and j != 0:
            print("i and j -> i:{}; j:{}".format(i,j))
            count += 1
print(count)