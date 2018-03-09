# https://codefights.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo

# Let's define digit degree of some positive integer as the number
# of times we need to replace this number with the sum of its digits
# until we get to a one digit number.

# Given an integer, find its digit degree.

# Example

# For n = 5, the output should be
# digitDegree(n) = 0;
# For n = 100, the output should be
# digitDegree(n) = 1.
# 1 + 0 + 0 = 1.
# For n = 91, the output should be
# digitDegree(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.
def sum_digits(n):
    numbers = [int(x) for x in list(str(n))]
    return sum(numbers)

def digitDegree(n, degree = 0):
    print("n:{} len(n):{} degree:{}".format(n, len(str(n)), degree))
    if len(str(n)) > 1:
        n = sum_digits(n)
        degree += 1
        return digitDegree(n, degree)
    return degree


print(digitDegree(3))
print(" agora 91")
print(digitDegree(91))

