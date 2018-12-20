import numpy as np
import sys

# print(len(sys.argv))
if len(sys.argv) == 5:
    random_matrix1 = np.random.randint(1, 10, (int(sys.argv[1]), int(sys.argv[2])))
    random_matrix2 = np.random.randint(1, 10, (int(sys.argv[3]), int(sys.argv[4])))
    print("Matrix 1:")
    print(random_matrix1)
    print("Matrix 2:")
    print(random_matrix2)
    print("Multiplication")
    # Only for Numpy > 1.10 (Python 3?), but better method!!
    # m2 = np.matmul(random_matrix1,random_matrix2)
    m = np.dot(random_matrix1,random_matrix2)
    print(m)
    # print(m2)
else:
        print("Usage: {} row1 column1 row2 column2".format(sys.argv[0]))
        sys.exit()