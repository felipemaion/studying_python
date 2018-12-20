# https://codefights.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP
# Two arrays are called similar if one can be obtained from another by
# swapping at most one pair of elements in one of the arrays.
#
# Given two arrays a and b, check whether they are similar.
#
# Example
#
# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.
#
# The arrays are equal, no need to swap any elements.
#
# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.
#
# We can obtain b from a by swapping 2 and 1 in b.
#
# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.
#
# Any swap of any two elements either in a or in b won't make a and b equal.

def areSimilar(a, b):
    if a == b:
        return True
    different = [i for i, j in zip(a, b) if i != j]
    if len(different) > 2:
        return False
    indices_a = [index for index, x in enumerate(a) if x == different[0]]
    indices_a1 = [index for index, x in enumerate(a) if x == different[1]]
    for index in indices_a:
        if a[index] == b[index]:
            pass
        else:
            for index1 in indices_a1:
                if a[index1] == b[index1]:
                    pass
                else:
                    a[index],a[index1] = a[index1], a[index]
                    # print("\t", a,"\n\t", b)
                    if a == b:
                        return True
                    else:
                        return False


    ## ISSUE WITH TIME ELAPSED:
    # for i_a,element_a in enumerate(a):
    #     if a.count(element_a) != b.count(element_a):
    #         return False
    #     if element_a != b[i_a]:
    #         indices = [index for index, x in enumerate(b) if x == element_a]
    #         for i_b in indices:
    #             if a[i_b] == b[i_a]:
    #                 a[i_a], b[i_b] = b[i_a], a[i_b]
    #                 if a == b:
    #                     return True
    #                 else: # Only one change is allowed!
    #                     return False
    # return False

a = [1, 2, 3]
b = [2, 1, 3]
print(areSimilar(a,b)) # True

a = [1, 2, 1]
b = [2, 1, 2]
print(areSimilar(a,b)) # False

a = [4, 6, 3]
b = [3, 4, 6]
print(areSimilar(a,b)) # False

a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
print(areSimilar(a,b)) # False


