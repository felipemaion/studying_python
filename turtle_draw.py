from turtle import *
loop = [10,9,9,7,7,5,5,3,3,1]

hideturtle()
up()
for count in loop:
    for i in range(count):
        forward(10)
        write("*")
    right(90)
done()