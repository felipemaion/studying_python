# https://codefights.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.
# # TIME ELAPSED ISSUED:
# def arrayMaxConsecutiveSum(inputArray, k):
#     max_sum = 0
#     for index in range(len(inputArray) - k + 1):
#         local_sum = sum(inputArray[index:index + k])
#         max_sum = local_sum if local_sum > max_sum or index == 0 else max_sum
#     return max_sum
# #
#
# def arrayMaxConsecutiveSum(inputArray, k):
#     group_sum = []
#     for index in range(len(inputArray) - k + 1):
#         group_sum.append(inputArray[index:index + k])
#     return sum(max(group_sum,key=lambda x: sum(x)))
def arrayMaxConsecutiveSum(inputArray, k):
    # print(inputArray, k)
    local_sum = 0
    max_sum = 0
    for index in range(len(inputArray) - k + 1):
        if index == 0:
            local_sum = sum(inputArray[index:index + k])
            # print(local_sum)
        else:
            local_sum += inputArray[index + k -1]
            # print("+", inputArray[index])
            for i in range(index - 1, index):
                # print("-", inputArray[i])
                local_sum -= inputArray[i]
        max_sum = local_sum if local_sum > max_sum or index == 0 else max_sum
    return max_sum


print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6],2)) #8
print(arrayMaxConsecutiveSum([1, 3, 2, 4],3)) #9
print(arrayMaxConsecutiveSum([2, 4, 10, 1],2)) #14
import random
iArr = random.sample(range(100000), 10000)
print(arrayMaxConsecutiveSum(iArr,1000))

