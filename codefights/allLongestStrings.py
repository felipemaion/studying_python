# https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
# Given an array of strings, return another array containing all of its longest strings.
#
# Example
#
# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inputArray):
    biggest = max(inputArray, key=lambda x: len(x))
    allLongest = []
    for word in inputArray:
        allLongest.append(word) if len(word) == len(biggest) else None
    return allLongest
