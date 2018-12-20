# https://codefights.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
# You are given an array of integers. On each move you are allowed to
# increase exactly one of its element by one. Find the minimal number of moves
# required to obtain a strictly increasing sequence from the input.
#
# Example
#
# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.
#
from timeMeasure import *

@speed_test
def arrayChange(inputArray):
    def get_not_increasing(sequence, current_index=0):
        for index in range(len(sequence) - 1):
            if sequence[index] >= sequence[index + 1]:
                return index + current_index
        return -1

    count = 0
    not_inc = 0
    while True:
        not_inc = get_not_increasing(inputArray[not_inc:], not_inc)
        if not_inc == -1:
            break
        dif = (1 + inputArray[not_inc]) - inputArray[not_inc + 1]
        inputArray[not_inc + 1] = inputArray[not_inc] + 1
        count += dif

    return count

@speed_test
def arrayChange1(inputArray):
    def get_not_increasing(sequence):
        for index in range(len(sequence) - 1):
            if sequence[index] >= sequence[index + 1]:
                return index
        return -1

    count = 0
    while True:
        not_inc = get_not_increasing(inputArray)
        if not_inc == -1:
            break
        dif = (1 + inputArray[not_inc]) - inputArray[not_inc + 1]
        inputArray[not_inc + 1] = inputArray[not_inc] + 1
        count += dif

    return count

@speed_test
#### FINAL SOLUTION!!!!
def arrayChange2(sequence):
    count = 0
    # print(sequence)
    for index in range(len(sequence) - 1):
        # print(sequence[index], sequence[index+1])
        if sequence[index] >= sequence[index + 1]:
            dif = (1 + sequence[index]) - sequence[index + 1]
            count += dif
            sequence[index +1] = sequence[index] + 1
    return count


iArr = [1,1,1]
arrayChange(iArr) # 3
arrayChange1(iArr) # 3
arrayChange2(iArr)
print(" ")

iArr = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
arrayChange(iArr) # 13
arrayChange1(iArr) # 13
arrayChange2(iArr)
print(" ")


iArr =  [-1000,0,-2,0]
arrayChange(iArr)
arrayChange1(iArr)
arrayChange2(iArr)
print(" ")

# Comparing longer lists
import random
iArr = random.sample(range(100000), 10000)
arrayChange(iArr)
arrayChange1(iArr)
arrayChange2(iArr)
print(" ")

