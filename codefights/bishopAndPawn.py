# https://codefights.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo
#
# Given the positions of a white bishop and a black pawn on the standard chess board,
# determine whether the bishop can capture the pawn in one move.
#
# The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
# Check out the example below to see how it can move:
#https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/bishop.jpg?_tm=1493360096740
#
# Example
#
# For bishop = "a1" and pawn = "c3", the output should be
# bishopAndPawn(bishop, pawn) = true.
#https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/ex1.jpg?_tm=1493360096945
#
# For bishop = "h1" and pawn = "h3", the output should be
# bishopAndPawn(bishop, pawn) = false.
#https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/ex2.jpg?_tm=1493360097459

def bishopAndPawn(bishop, pawn):
    bishop, pawn = bishop.upper(), pawn.upper()
    # board = create_board()
    # if board[bishop] != board[pawn]:
    #     return False
    # else:
    return True if pawn in capture_zone_of(bishop) else False

def capture_zone_of(bishop_place):
    letters_cell = list("ABCDEFGH")
    numbers_cell = list(range(1, 9))
    bishop_letter = letters_cell.index(bishop_place[0])
    bishop_number = numbers_cell.index(int(bishop_place[1]))
    moves = []
    # print("Moving UP and RIGHT")
    number = bishop_number + 1
    for letter in letters_cell[bishop_letter:9]:
        moves.append(str(letter) + str(number)) if number < 9 else None
        number += 1
    # print("Moving UP and LEFT")
    for i,number in enumerate(numbers_cell[bishop_number:9]):
        letter = letters_cell[bishop_letter - i]
        moves.append(str(letter) + str(number)) if bishop_letter - i >= 0 else None
    # print("Moving DOWN and RIGHT")
    number = bishop_number + 1
    for letter in letters_cell[bishop_letter:9]:
        moves.append(str(letter) + str(number)) if number > 0 else None
        number -= 1
    # print("Moving DOWN and LEFT")
    for i,number in enumerate(reversed(numbers_cell[0:bishop_number+1])):
        letter = letters_cell[bishop_letter - i]
        moves.append(str(letter) + str(number)) if bishop_letter - i >= 0 else None
    # print(sorted(list(set(moves))))
    return sorted(list(set(moves)))

#
# def create_board():
#     letters_cell = list("ABCDEFGH")
#     numbers_cell = list(range(1,9))
#     board = {}
#     color = 0
#     # Create Board
#     for letter in letters_cell:
#         for number in numbers_cell:
#             board[str(letter) + str(number)] = color
#             # Change color of next Square:
#             color = 1 - color
#         # Change color when change the row.
#         color = 1 - color
#     return board

# print(bishopAndPawn(bishop = "h1", pawn = "h3"))
# print("D4:")
# print(bishop_moves("D4")) # A1, A7,B2,B6,C3,C5,D4,E3,E5,F2,F6,G1,G7,H8
# print("A1, A7,B2,B6,C3,C5,D4,E3,E5,F2,F6,G1,G7,H8")
# print("E7:")
# print(bishop_moves("E7"))

bishop = "a1"
pawn = "c3"#, the output should be
print(bishopAndPawn(bishop, pawn)) # = true.
#https://codefightsuserpics.s3.amazonaws.com/tasks/bishopAndPawn/img/ex1.jpg?_tm=1493360096945
#
# For bishop = "h1" and pawn = "h3", the output should be
# bishopAndPawn(bishop, pawn) = false.