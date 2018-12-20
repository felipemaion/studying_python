# https://codefights.com/arcade/intro/level-11/Zr2XXEpkBPtYWqPJu
# Determine if the given character is a digit or not.

# Example

# For symbol = '0', the output should be
# isDigit(symbol) = true;
# For symbol = '-', the output should be
# isDigit(symbol) = false.

from string import digits
def isDigit(symbol):
    return True if symbol in digits else False
