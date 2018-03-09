# https://codefights.com/arcade/intro/level-8/8N7p3MqzGQg5vFJfZ
# Given a string, find the number of different characters in it.
#
# Example
#
# For s = &quot;cabca&quot;, the output should be
# differentSymbolsNaive(s) = 3.
#
# There are 3 different characters a, b and c.
def differentSymbolsNaive(s):
    return len(set(list(s)))

print(differentSymbolsNaive("cabca"))