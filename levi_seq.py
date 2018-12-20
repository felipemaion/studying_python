import numpy
num_dim = int(input("Enter the inputs : ") or "9")
my_vector = numpy.zeros((num_dim, num_dim))
my_vector[:,0] = range(1,num_dim+1)


for x in range(1,num_dim):
    for y in range(1,x+1):
        my_vector[x,y] = (y+1)* my_vector[x][0]
# (x,y) = (y+1)*(x,0)

## DISPLAY AS REQUESTED:
for x in range(0,num_dim):
    for y in range(0,x+1):
        print(int(my_vector[x,y]), end =" ")
    print("")
# print("1  \t\n2  \t4  \t\n3  \t6  \t9  \t\n4  \t8  \t12  \t16  \t\n5  \t10  \t15  \t20  \t25  \t\n6  \t12  \t18  \t24  \t30  \t36  \t\n7  \t14  \t21  \t28  \t35  \t42  \t49  \t\n8  \t16  \t24  \t32  \t40  \t48  \t56  \t64  \t\n9  \t18  \t27  \t36  \t45  \t54  \t63  \t72  \t81")