# https://codefights.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL
# Call two arms equally strong if the heaviest weights they each are able to lift are equal.
#
# Call two people equally strong if their strongest arms are equally strong
# (the strongest arm can be both the right and the left), and so are their weakest arms.
#
# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
#
# Example
#
# For yourLeft = 10, yourRight = 15, friendsLeft = 15 and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 9, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    def strongestArm(left, right):
        return left if left > right else right

    def weakestArm(left, right):
        return left if left < right else right

    my_strongest_arm = strongestArm(yourLeft,yourRight)
    friends_strongest_arm = strongestArm(friendsLeft,friendsRight)
    my_weakest_arm = weakestArm(yourLeft,yourRight)
    friends_weakest_arm = weakestArm(friendsLeft,friendsRight)

    return True if my_strongest_arm == friends_strongest_arm and my_weakest_arm == friends_weakest_arm else False

yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10#, the output should be
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))# = true;

yourLeft = 15
yourRight = 10
friendsLeft = 15
friendsRight = 10#, the output should be
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))# = true;

yourLeft = 15
yourRight = 10
friendsLeft = 15
friendsRight = 9#, the output should be
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))# = false


