# https://codefights.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ
# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the
# distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).
#
# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
#
# Example
#
# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.
#
# https://codefightsuserpics.s3.amazonaws.com/tasks/circleOfNumbers/img/example.png?_tm=1490625697098
#

def circleOfNumbers(n, firstNumber):
    space = 360 / n
    opposite = 180 / space
    return int((firstNumber + opposite) % n)

print(circleOfNumbers(10,2))
print(circleOfNumbers(10,9))
print(circleOfNumbers(10,0))
print(circleOfNumbers(10,8))