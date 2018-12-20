# https://codefights.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx
# Given a string, find the shortest possible string which can be achieved
# by adding characters to the end of initial string to make it a palindrome.

# Example

# For st = "abcdc", the output should be
# buildPalindrome(st) = "abcdcba".
def buildPalindrome(st):
    if is_palindrome(st):
        return True
    size = len(st)
    for i in range(size):
        sub_string = st[i:size]
        print(sub_string)
        if is_palindrome(sub_string):
            return st + st[0:i][::-1]


def is_palindrome(st):
    return True if st[::-1] == st else False

print(buildPalindrome(st = "abcdc"))
print(buildPalindrome("abba"))