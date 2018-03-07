# https://codefights.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
# In the popular Minesweeper game you have a board with some mines and those cells
# that don't contain a mine have a number in it that indicates the total number of mines
# in the neighboring cells.
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.
#
# Example
#
# For
#
# matrix = [[True, False, False],
#           [False, True, False],
#           [False, False, False]]
# print(*minesweeper(matrix), sep="\n")
# the output should be
#
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]
# Check out the image below for better understanding:
#https://codefightsuserpics.s3.amazonaws.com/tasks/minesweeper/img/example.png?_tm=1490636350838

def minesweeper(matrix):
    # Define dimensions:
    rows, columms = len(matrix), len(matrix[0])
    # Create a board the same size of the given matrix:
    board = [[0 for x in range(columms)] for y in range(rows)]
    # Sweep the matrix for bombs:
    for i in range(rows):
        for j in range(columms):
            if matrix[i][j]:
                # If we found a bomb mark the surroundings:
                for sweep_i in range(-1,2):
                    for sweep_j in range(-1,2):
                        # Check if this place is inside of the Board:
                        if (i+sweep_i >= 0) and (i+sweep_i < rows) \
                                and (j+sweep_j >=0) and (j+sweep_j < columms):
                            if [sweep_i, sweep_j] != [0,0]: # Don't count myself (bomb's talk)
                                # Increase the count of this place
                                board[i+sweep_i][j+sweep_j] += 1
    return board



matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
print(*minesweeper(matrix), sep="\n")
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]

print("\n")
matrix =  [[True,False,False,True], 
            [False,False,True,False], 
            [True,True,False,True]]

# Expected Output:
# [[0,2,2,1],
#  [3,4,3,3],
#  [1,2,3,1]]
print(*minesweeper(matrix), sep="\n")
