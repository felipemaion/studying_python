# https://codefights.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb

# Given a position of a knight on the standard chessboard,
# find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically,
# or two squares vertically and one square horizontally away from it.
# The complete move therefore looks like the letter L.
# Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.
# http://www.chesscorner.com/tutorial/basic/knight/knight.htm
# Example

# For cell = "a1", the output should be
# chessKnight(cell) = 2.

# For cell = "c2", the output should be
# chessKnight(cell) = 6.

def chessKnight(cell):
    cell = cell.upper()
    return len(capture_zone_of(cell))




def capture_zone_of(knight_place):
    letters_cell = list("ABCDEFGH")
    numbers_cell = list(range(1, 9))
    knight_letter = letters_cell.index(knight_place[0])
    knight_number = numbers_cell.index(int(knight_place[1]))
    moves = []
    print("Place:{} Letter:{} Number:{}".format(knight_place,knight_letter, knight_number))
    # I BET I CAN REFACTOR THIS: DRY is NOT HERE!!
    # print("Moving Long UP and Short RIGHT")
    ## Cell E4 -> F6
    letter = letters_cell[knight_letter + 1] if knight_letter < 7 else ""
    number = numbers_cell[knight_number + 2] if knight_number < 6 else ""
    # print(letter,number)
    moves.append(str(letter)+str(number)) if letter and number else None
    #
    # print("Moving Short UP and Long RIGHT")
    ## Cell E4 -> G5
    letter = letters_cell[knight_letter + 2] if knight_letter < 6 else ""
    number = numbers_cell[knight_number + 1] if knight_number < 7 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    #
    # print("Moving Long UP and Short LEFT")
    ## Cell E4 -> D6
    letter = letters_cell[knight_letter - 1] if knight_letter > 0 else ""
    number = numbers_cell[knight_number + 2] if knight_number < 6 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    #
    # print("Moving Short UP and Long LEFT")
    ## Cell E4 -> C5
    letter = letters_cell[knight_letter - 2] if knight_letter > 1 else ""
    number = numbers_cell[knight_number + 1] if knight_number < 7 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    #
    #
    # print("Moving Long DOWN and Short RIGHT")
    ## Cell E4 -> F2
    letter = letters_cell[knight_letter + 1] if knight_letter < 7 else ""
    number = numbers_cell[knight_number - 2] if knight_number > 1 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    #
    # print("Moving Short DOWN and Long RIGHT")
    ## Cell E4 -> G3
    letter = letters_cell[knight_letter + 2] if knight_letter < 6 else ""
    number = numbers_cell[knight_number - 1] if knight_number > 0 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    #
    # print("Moving Long DOWN and Short LEFT")
    ## Cell E4 -> D2
    letter = letters_cell[knight_letter - 1] if knight_letter > 0 else ""
    number = numbers_cell[knight_number - 2] if knight_number > 1 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    #
    # print("Moving Short DOWN and Long LEFT")
    ## Cell E4 -> C3
    letter = letters_cell[knight_letter - 2] if knight_letter > 1 else ""
    number = numbers_cell[knight_number - 1] if knight_number > 0 else ""
    # print(letter,number)
    moves.append(str(letter) + str(number)) if letter and number else None
    # print(sorted(list(set(moves))))
    return sorted(list(set(moves)))

Cell = "E4"
print("D6; C5; C3; D2; F2; G3; G5; F6")
print(capture_zone_of("E4"))
print(capture_zone_of("H8"))
print(capture_zone_of("A8"))
print(capture_zone_of("A1"))
print(capture_zone_of("H1"))
print(capture_zone_of("G6"))