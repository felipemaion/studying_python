# https://codefights.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv
# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# Example

# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
# the output should be
# differentSquares(matrix) = 6.

# Here are all 6 different 2 × 2 squares:

# 1 2
# 2 2

# 2 1
# 2 2

# 2 2
# 2 2

# 2 2
# 1 2

# 2 2
# 2 3

# 2 3
# 2 1
import numpy as np
def differentSquares(matrix):
    matrix = np.matrix(matrix)
    m,n = matrix.shape
    squares = []
    for i in range(m - 1):
        for j in range(n-1):
            submatrix = matrix[i:i+2,j:j+2].tolist()
            squares.append(submatrix) if submatrix not in squares else None
    return len(squares)

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

print(differentSquares(matrix))