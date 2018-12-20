# https://codefights.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
#
# Example
#
# For
#
# picture = ["abc",
#            "ded"]
# the output should be
#
# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
    border_width = len(picture[0]) + 2
    new_picture = []
    new_picture.append(border_width*"*")
    for line in picture:
        new_picture.append("*" + line + "*")
    new_picture.append(border_width*"*")
    return new_picture

picture = ["abc",
           "ded"]
print(addBorder(picture))
