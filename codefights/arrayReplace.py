# https://codefights.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm
# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
#
# Example
#
# For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
# arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x == elemToReplace else x for x in inputArray]

inputArray = [1, 2, 1]
elemToReplace = 1
substitutionElem = 3
print(arrayReplace(inputArray,elemToReplace,substitutionElem))