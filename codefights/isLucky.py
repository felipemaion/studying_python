# # https://codefights.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half
# of the digits is equal to the sum of the second half.
#
# Given a ticket number n, determine if it's lucky or not.
#
# Example
#
# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

def isLucky(n):
    n = list(str(n))
    sum1,sum2 = 0,0
    for num in n[:int(len(n)/2)]:
        sum1 += int(num)
    for num in n[int(len(n)/2):]:
        sum2 += int(num)
    return True if sum1==sum2 else False

print(isLucky(1230))
print(isLucky(239017))


