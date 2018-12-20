# https://codefights.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
# Given an array of equal-length strings, check if it is possible to rearrange the strings
# in such a way that after the rearrangement the strings at consecutive positions
# would differ by exactly one character.
#
# Example
#
# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false;
#
# All rearrangements don't satisfy the description condition.
#
# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.
#
# Strings can be rearranged in the following way: "aa", "ab", "bb".
from itertools import permutations
def stringsRearrangement(inputArray):
    # Create all possible arrangements:
    all_permutation = list(permutations(inputArray))
    # For each arrangement:
    for current_permutation in all_permutation:
        i = 0
        good = True
        # Check if sequence differs only by one character:
        while i < len(current_permutation) - 1:
            if not difference_is_one(current_permutation[i], current_permutation[i + 1]):
                good = False
                break
            i += 1
        if good:
            return True
    return False


def difference_is_one(a,b):
    words = zip(a, b)
    return True if len([letter_a for letter_a, letter_b in words if letter_a != letter_b]) == 1 else False


inputArray =  ["abc", "abx", "axx", "abx", "abc"]

print(stringsRearrangement(inputArray))