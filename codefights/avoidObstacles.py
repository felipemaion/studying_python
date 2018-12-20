# https://codefights.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
# You are given an array of integers representing coordinates of obstacles situated on a straight line.
#
# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
#
# Example
#
# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.
#
# Check out the image below for better understanding:
#     # https://codefightsuserpics.s3.amazonaws.com/tasks/avoidObstacles/img/example.png?_tm=1490625560816


def avoidObstacles(inputArray):
    array = sorted(inputArray)
    chuncks = get_chuncks(array)
    max_chunck = biggest_chunck(chuncks)
    min_step = len(max_chunck) + 1
    ruler = fill_ruler(array)
    # print(ruler)
    pos = 0
    max_pos = len(ruler)
    inside_ruler = True
    while inside_ruler:
        pos += min_step
        # print(pos)
        if pos >= max_pos:
            break
        if ruler[pos] == []:
            pass
        else:
            min_step += 1
            pos = 0
    return min_step


def fill_ruler(array):
    ruler = []
    for i in range(max(array) + 1):
        ruler.append([])
        if i in array:
            ruler[i].append(i)
    return ruler


def get_chuncks(array):
    chunckSize = 0
    chuncks = []
    chunckCount = -1
    inside_chunck = False
    for index in range(len(array) - 1):
        if array[index] == array[index + 1] - 1:
            if not inside_chunck:
                chunckCount += 1
                chuncks.append([])
                inside_chunck = True
            chuncks[chunckCount].append(array[index]) if array[index] not in chuncks[chunckCount] else None
            chuncks[chunckCount].append(array[index + 1])
        else:
            inside_chunck = False
    return chuncks


def biggest_chunck(chuncks):
    try:
        return max(chuncks, key=lambda x: len(x))
    except:
        return [0]


# >> myArr = sorted([5, 3, 6, 7, 9,2,15,16,20,27,28,29,30])
# >> print("myArr:", myArr)
# myArr: [2, 3, 5, 6, 7, 9, 15, 16, 20, 27, 28, 29, 30]

# >> chuncks = get_chuncks(myArr)
# >> print("get_cruncks(myArr):", chuncks)
# get_cruncks(myArr): [[2, 3], [5, 6, 7], [15, 16], [27, 28, 29, 30]]

# >> maior = biggest_chunck(chuncks)
# >> print("Biggest chunck:", maior)
# Biggest chunck: [27, 28, 29, 30]

# >>print("Size of biggest chunk:", len(maior))
# Size of biggest chunk: 4

# >>print("Ruler filled with elements:", fill_ruler(myArr))
# Ruler filled with elements: [[], [], [2], [3], [], [5], [6], [7], [], [9], [], [], [], [], [], [15], [16], [], [], [], [20], [], [], [], [], [], [], [27], [28], [29], [30]]

# >>print("Min step to avoid obstacles:", avoidObstacles(myArr))
# Min step to avoid obstacles: 11
#
#
#
# For sure I could solve it mathematically, but I wanted to solve it "visually"
#
# def avoidObstacles2(inputArray):
#     for i in range(1, max(inputArray)):
#         divs = any([x for x in inputArray if not x % i])
#         if not divs:
#             return i

#     return max(inputArray) + 1


myArr = sorted([1,2,3,4,5,6,7])
print("myArr:", myArr)
chuncks = get_chuncks(myArr)
print("get_cruncks(myArr):", chuncks)
maior = biggest_chunck(chuncks)
print("Biggest chunck:", maior)
print("Size of biggest chunk:", len(maior))
print("Ruler filled with elements:", fill_ruler(myArr))
print("Min step to avoid obstacles:", avoidObstacles(myArr))


import random
iArr = random.sample(range(40), 40)
print(iArr)
print(avoidObstacles(iArr))


ia =  [19, 32, 11, 23]
print(avoidObstacles(ia))