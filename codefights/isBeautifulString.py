# https://codefights.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE
# A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

# Given a string, check whether it is beautiful.

# Example

# For inputString = "bbbaacdafe", the output should be
# isBeautifulString(inputString) = true;
# For inputString = "aabbb", the output should be
# isBeautifulString(inputString) = false;
# For inputString = "bbc", the output should be
# isBeautifulString(inputString) = false.

import string
def isBeautifulString(inputString):
    current_count = inputString.count("a")
    for char in string.ascii_lowercase:
        local_count = inputString.count(char)
        if local_count > current_count:
            return False
        else:
            current_count = local_count
    return True

print(isBeautifulString("bbbaacdafe")) # True
print(isBeautifulString("aabbb")) # False
print(isBeautifulString("zaa")) # False

