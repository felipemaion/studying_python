# # https://codefights.com/arcade/intro/level-12/uRWu6K8E7uLi3Qtvx
# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

# Example

# For n = 3, the output should be

# spiralNumbers(n) = [[1, 2, 3],
#                     [8, 9, 4],
#                     [7, 6, 5]]
import numpy as np
def spiralNumbers(n):
    matrix = np.arange(1,n**2+1).reshape(n, n)
    i=1
    j=0
    while i+n < n**2:
        last_row = 0
        for row in range(1+j,n-j):
            matrix[row, n-1-j]=n + i
            i+=1
            last_row = row
        last_column = 0
        # print("1) i:{} j:{} \n {}".format(i,j, matrix))
        # input()
        for column in reversed(range(0+j,n-1-j)):
            matrix[last_row, column] = n + i
            i+=1
            last_column = column
        # print("2", matrix)
        # input()
        for row in reversed(range(1+j,n-1-j)):
            matrix[row, last_column] = n + i
            i+= 1
            last_row = row
        # print("3", matrix)
        # input()
        for column in range(1+j,n-1-j):
            matrix[last_row, column] = n + i
            i +=1
        j +=1
        # print("4", matrix)
        # input()
    return matrix




print(spiralNumbers(9))