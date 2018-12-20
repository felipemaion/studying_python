import numpy as np
import sys

def create_matrix(m = 3, n = None):
    n = m if n == None else n
    string_matrix = ""
    for i in range(m):
        valid = False
        # To avoid problems with wrong number of items:
        while not valid:
            row = raw_input(" Row {} >>".format(i+1))
            # check if # of items are ok.
            data = row.split(" ")
            # remove extra blank spaces:
            data = [x for x in data if x]
            # If items are not the same size of the matrix, try again.
            if len(data) != n:
                valid = False
                formating = ['1'] * n
                print("Please Enter the row in the format:{}".format(" ".join(formating)))
            else:
                # If ok, store then in the string.
                valid = True
                string_matrix += row
                # Add a line breaker ; at the end of each row except the last one.
                string_matrix += ";" if i != m-1 else ""

    # Make it a Matrix in Numpy
    return np.matrix(string_matrix)


if len(sys.argv) > 0 and len(sys.argv) <= 3:
    if len(sys.argv) == 2:
        try:
            m = int(sys.argv[1])
            n = m
        except:
            print("Usage: {} row [=columm]".format(sys.argv[0]))
            sys.exit()
    if len(sys.argv) == 1:
        m, n = 3, 3
    if len(sys.argv) == 3:
        m,n = int(sys.argv[1]), int(sys.argv[2])
else:
        print("Usage: {} row [=columm]".format(sys.argv[0]))
        sys.exit()
print("{} rows by {} columns:".format(m,n))
matrix = create_matrix(m, n)
rank = np.linalg.matrix_rank(matrix)
shape = matrix.shape
print("Matrix: \n{}\nRank: {}\nShape:{}".format(matrix,rank,shape))
