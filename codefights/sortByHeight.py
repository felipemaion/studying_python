# # https://codefights.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
# Some people are standing in a row in a park. There are trees between them which cannot be moved.
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
#
# Example
#
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]

def sortByHeight(a):
    people = a.copy()
    people = [person for person in people if person > 0]
    new_row = []
    for spot in a:
        if spot == -1:
            new_row.append(spot)
        else:
            person = min(people)
            people.remove(person)
            new_row.append(person)
    return new_row


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))