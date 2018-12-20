# https://codefights.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq
# Given a sorted array of integers a, find an integer x from a such that the value of
#
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
# is the smallest possible (here abs denotes the absolute value).
# If there are several possible answers, output the smallest one.
#
# Example
#
# For a = [2, 4, 7], the output should be
# absoluteValuesSumMinimization(a) = 4.

# (4-2) + (4-4) + (7-4) = 5

# Not working since it does not say about POSITIVE x.
# def absoluteValuesSumMinimization(a, x = 0, min_sum = []):
#     min_sum.append(0)
#     for term in a:
#         min_sum[x] += abs(term - x)
#     x += 1
#     min2 = min_sum[x-1]
#     if min2 > min(min_sum):
#         return min_sum.index(min(min_sum))
#     else:
#         return absoluteValuesSumMinimization(a,x,min_sum)
#
#
def absoluteValuesSumMinimization(a):
    def get_sum(a, x):
        my_sum = 0
        for term in a:
            my_sum += abs(term-x)
        return my_sum

    all_sum = []
    for i,x in enumerate(a):
        all_sum.append(get_sum(a,x))
        if i > 1:
            if all_sum[i] > all_sum[i-1]:
                return a[all_sum.index(min(all_sum))]
    return a[all_sum.index(min(all_sum))]




print(absoluteValuesSumMinimization([2, 4, 7]))

