# A village has a tradition of war game every year.
# They place one archer on each hill and make them shoot each other.
#  Each hill has different altitude.
# Altitude of the hill is depicted by a number from 1 to 9.
# An archer on a hill can shoot other archers if an altitude of a hill
# on which he is located is greater or equal to the altitude of a hill the other archer is located

# But this time due to the heavy south-east wind,
# archers are only able to shoot in south and east direction.
# Find the sum of total hits of all archers can make.

# Archers position and height of the hill is represented by a matrix A.
#
# 4 1 2
# 3 8 8
# 7 6 5


# Archer (1, 1) can hit (1, 2), (1, 3) and (2, 1). Hit count = 3.
# Archer (1, 2), (1,3), (2, 1), (3, 3) can't hit anyone on the east side
# or south direction because he is standing on a hill which has the smallest height among all.
# Their total Hit count = 0.
# Archer (2, 2) can hit (2, 3) and (3, 2). Hit count = 2.
# Archer (2, 3) can hit (3, 3) only. Hit count = 1.
# Archer (3, 1) can hit (3, 2) and (3, 3). Hit count = 2
# Archer (3, 2) can hit (3, 3). Hit count = 1
#
#
# Hence, sum of total hits of all archers = 3 + 0 + 2 + 1 + 2 + 1 = 9
import numpy as np

def solution(matrix,m,n):
    matrix = np.matrix(matrix)
    it = np.nditer(matrix, flags=['multi_index'])
    count = 0
    while not it.finished:
        print ("%d %s:" % (it[0], it.multi_index))
        row, columm = it.multi_index
        for enemy_c in range(columm,n):
            if it[0] >= matrix[row, enemy_c]: #enemy_r != row and enemy_c != columm:
                if enemy_c != columm:
                    print("\tHit {} ({},{})".format(matrix[row, enemy_c],row+1,enemy_c+1))
                    count += 1
        for enemy_r in range(row,m):
            if it[0] >= matrix[enemy_r, columm]: #enemy_r != row and enemy_c != columm:
                if enemy_r != row:
                    print("\tHit {} ({},{})".format(matrix[enemy_r, columm],enemy_r+1,columm+1))
                    count +=1
        it.iternext()
    print("Total hits:",count)
    return count



solution([[4,1,2],[3,8,8],[7,6,5]],3,3)