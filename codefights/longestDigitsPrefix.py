# https://codefights.com/arcade/intro/level-9/AACpNbZANCkhHWNs3
# Given a string, output its longest prefix which contains only digits.

# Example

# For inputString="123aa1", the output should be
# longestDigitsPrefix(inputString) = "123".

def longestDigitsPrefix(inputString):
    digits = list("0123456789")
    if " " in inputString:
        return ""
    prefix = ""
    for i, char in enumerate(inputString):
        if inputString[0] in digits:
            if inputString[i] in digits:
                prefix += inputString[i]
            else:
                break
        else:
            return ""
    return prefix

print(longestDigitsPrefix("123aa1"))
print(longestDigitsPrefix("123456755243"))


