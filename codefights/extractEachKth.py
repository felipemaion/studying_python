# https://codefights.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
# Given array of integers, remove each kth element from it.
#
# Example
#
# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
# extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
def extractEachKth(inputArray, k):
    for i in reversed(range(len(inputArray))):
        i+=1
        if i % k == 0:
            inputArray.pop(i-1)
    return inputArray


print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))
print(extractEachKth([1, 2, 1, 2, 1, 2, 1, 2],2))