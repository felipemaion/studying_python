# https://codefights.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
# Given a string, find out if its characters can be rearranged to form a palindrome.
#
# Example
#
# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.
#
# We can rearrange "aabb" to make "abba", which is a palindrome.
#

def palindromeRearranging(inputString):
    number_odds = 0
    tested = []
    for chr in inputString:
        # print(chr, inputString.count(chr))
        if chr not in tested:
            tested.append(chr)
            if inputString.count(chr) % 2 == 1:
                number_odds +=1
            if number_odds > 1:
                return False

    return True

s= "aabb"
print(palindromeRearranging(s))

s= "aaa"
print(palindromeRearranging(s))

