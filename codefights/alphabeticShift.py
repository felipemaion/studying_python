# https://codefights.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui
# Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).
#
# Example
#
# For inputString = &quot;crazy&quot;, the output should be
# alphabeticShift(inputString) = &quot;dsbaz&quot;./
import string
def alphabeticShift(inputString):
    alphabet = string.ascii_lowercase
    betabet = string.ascii_lowercase[1:] + "a"
    key_change = dict(zip(alphabet,betabet))
    new_string = ""
    for chr in inputString:
        new_string += key_change[chr]
    return new_string

print(alphabeticShift("crazy"))