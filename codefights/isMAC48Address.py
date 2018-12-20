# https://codefights.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm
# A media access control address (MAC address) is a unique identifier assigned to
# network interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is
# six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

# Example

# For inputString = "00-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = true;
# For inputString = "Z1-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = false;
# For inputString = "not a MAC-48 address", the output should be
# isMAC48Address(inputString) = false.
from string import hexdigits
def isMAC48Address(inputString):
    groups = inputString.split("-")
    if len(groups) != 6:
        return False
    else:
        for digits in groups:
            if len(digits) != 2:
                return False
            for digit in digits:
                if digit not in hexdigits:
                    return False
    return True

print(isMAC48Address("00-1B-63-84-45-E6"))
print(isMAC48Address("Z0-1B-63-84-45-E6"))
print(isMAC48Address("not a Z0-1B-63-84-45-E6"))


