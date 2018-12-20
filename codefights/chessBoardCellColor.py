# https://codefights.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
# Given two cells on the standard chess board, determine whether they have the same color or not.
#
# Example
#
# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.
#
#
#
# For cell1 = "A1" and cell2 = "H3", the output should be
# chessBoardCellColor(cell1, cell2) = false.
#

def chessBoardCellColor(cell1, cell2):
    letter_cell = list("ABCDEFGH")
    number_cell = list(range(1,9))
    board = {}
    color = 0
    # Create Board
    for letter in letter_cell:
        for number in number_cell:
            board[str(letter) + str(number)] = color
            # Change color of next Square:
            color = 1 - color
        # Change color when change the row.
        color = 1 - color
    return  True if board[cell1] == board[cell2] else False


print(chessBoardCellColor("A1","H3"))