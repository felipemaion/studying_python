# https://codefights.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
# After they became famous, the CodeBots all decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.
#
# Help the bots calculate the total price of all the rooms that are suitable for them.
#
# Example
#
# For
# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]
# the output should be
# matrixElementsSum(matrix) = 9


def where_are(this, at_matrix):
    zeros = []
    for i, rows in enumerate(at_matrix):
        # Get all indices in each row with value 0:
        indices = [index for index, x in enumerate(rows) if x == this]
        zeros.append((i, indices))
    return zeros

def fill_below(pos_zeros, matrix):
    for row,columm in pos_zeros:
        for r in range(row,len(matrix)):
            for col in columm:
                matrix[r][col] = 0
    return matrix

def matrix_sum(matrix):
    mat_sum = 0
    for vector in matrix:
        mat_sum += sum(vector)
    return mat_sum

def matrixElementsSum(matrix):
    pos_zeros = where_are(0, matrix)
    new_matrix = fill_below(pos_zeros,matrix)
    return matrix_sum(new_matrix)


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

zeros = matrixElementsSum(matrix)
print(zeros)