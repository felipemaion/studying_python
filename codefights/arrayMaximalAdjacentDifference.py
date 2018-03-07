# https://codefights.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
#
# Example
#
# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

def arrayMaximalAdjacentDifference(inputArray):
    dif_array = []
    for index in range(len(inputArray) - 1):
        dif_array.append(abs(inputArray[index] - inputArray[index + 1]))
    return max(dif_array)

ia = [2,4,1,0]
print(arrayMaximalAdjacentDifference(ia))
