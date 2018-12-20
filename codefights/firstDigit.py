# https://codefights.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov
# Find the leftmost digit that occurs in a given string.
#
# Example
#
# For inputString = "var_1__Int", the output should be
# firstDigit(inputString) = '1';
# For inputString = "q2q-q", the output should be
# firstDigit(inputString) = '2';
# For inputString = "0ss", the output should be
# firstDigit(inputString) = '0'.

def firstDigit(inputString):
    digits = list("0123456789")
    a = [x for x in inputString if x in digits]
    return a[0]


print(firstDigit("var_1__Int"))