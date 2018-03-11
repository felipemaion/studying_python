# https://codefights.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX
# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

# For n = 152, the output should be
# deleteDigit(n) = 52;
# For n = 1001, the output should be
# deleteDigit(n) = 101.

def deleteDigit(n):
    numbers = [str(x) for x in list(str(n))]
    max_sum = ['0']
    for i in range(len(numbers)):
        buf_number = numbers.pop(i)
        max_sum = numbers.copy() if int("".join(numbers)) > int("".join(max_sum)) else max_sum
        numbers.insert(i, buf_number)
    return int("".join(max_sum))


print(deleteDigit(152))
print(deleteDigit(1001))
