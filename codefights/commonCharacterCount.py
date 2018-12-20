#https://codefights.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
#  Given two strings, find the number of common characters between them.
#
# Example
#
# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.
#
# Strings have 3 common characters - 2 "a"s and 1 "c".

def commonCharacterCount(s1, s2):
    count = 0
    s1, s2 = list(s1), list(s2)
    for letter in s1:
        if letter in s2:
            s2.remove(letter)
            count += 1
    return count

s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1,s2))
