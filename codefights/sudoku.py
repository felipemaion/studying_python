# # https://codefights.com/arcade/intro/level-12/tQgasP8b62JBeirMS
#     Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid
# with digits so that each column, each row, and each of the nine 3 × 3 sub-grids
# that compose the grid contains all of the digits from 1 to 9.

# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

# Example

# For the first example below, the output should be true. For the other grid,
#  the output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
import numpy as np
def sudoku(grid):
    matrix = np.matrix(grid)
    subgrid = []
    numbers = [1,2,3,4,5,6,7,8,9]
    print("Checking for Matrix: \n{}".format(matrix))

    # Check every small grid
    for i,j in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,6)]:
        smallgrid = matrix[i:i + 3, j:j + 3].reshape(1,9).tolist()
        subgrid.append(smallgrid)
        if sorted(list(set(smallgrid[0]))) != numbers:
            print("Grid: \n{} not correct, quiting.".format(np.matrix(smallgrid).reshape(3,3)))
            return False
    # Check each line:
    for row in matrix:
        row = row.tolist()
        if sorted(row[0]) != numbers:
            print("Line {} not correct".format(row))
            return False
    # Check each column:
    for column in range(len(matrix)):
        column = [x[0] for x in matrix[:,column:1+column].tolist()]
        if sorted(column) != numbers:
            print("Column {} not correct".format(column))
            return False
    return True



    # print(subgrid)
    # return True

grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
       [4, 6, 8, 5, 7, 9, 3, 2, 1],
       [7, 9, 2, 8, 1, 3, 6, 5, 4],
       [9, 2, 3, 1, 4, 5, 8, 7, 6],
       [3, 5, 7, 4, 6, 8, 2, 1, 9],
       [6, 8, 1, 7, 9, 2, 5, 4, 3],
       [5, 7, 6, 9, 8, 1, 4, 3, 2],
       [2, 4, 5, 6, 3, 7, 1, 9, 8],
       [8, 1, 9, 3, 2, 4, 7, 6, 5]]

print(sudoku(grid))


grid = [[1,3,2,5,4,6,9,8,7],
         [4,6,5,8,7,9,3,2,1],
         [7,9,8,2,1,3,6,5,4],
         [9,2,1,4,3,5,8,7,6],
         [3,5,4,7,6,8,2,1,9],
         [6,8,7,1,9,2,5,4,3],
         [5,7,6,9,8,1,4,3,2],
         [2,4,3,6,5,7,1,9,8],
         [8,1,9,3,2,4,7,6,5]]

print(sudoku(grid))