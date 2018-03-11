# https://codefights.com/arcade/intro/level-11/o2uq6eTuvk7atGadR
# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of
#  disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a
# concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.
# Example

# For s = "aabbbc", the output should be
# lineEncoding(s) = "2a3bc".

import re
def lineEncoding(s):
    matcher = re.compile(r'(.)\1*')
    groups = [match.group() for match in matcher.finditer(s)]
    new_encoding = ""
    for group in groups:
        size = len(group) if len(group) > 1 else ""
        new_encoding += str(size)+ group[0]
    return new_encoding


print(lineEncoding("aaabbc"))
