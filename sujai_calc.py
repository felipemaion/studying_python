class Multiply:
    def __init__(self):
        self.operation = "Multiplication"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{} -> Result:{}".format(self.operation,a,b, a*b))

class Add:
    def __init__(self):
        self.operation = "Sum"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{} -> Result:{}".format(self.operation,a,b, a+b))

class Subtraction:
    def __init__(self):
        self.operation = "Subtraction"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{} -> Result:{}".format(self.operation,a,b, a-b))

class Division:
    def __init__(self):
        self.operation = "Division"
    def call(self, a, b):
        print("Performing the operation:{} in a:{} and b:{} -> Result:{}".format(self.operation,a,b, a/b))

calculator={"1":Multiply(), "2":Add(), "3":Subtraction(), "4":Division()}
a = float(input("Number 1 >>"))
operation = input("Operation:\n \t[1] - Multiply\n\t[2] - Addition\n\t[3] - Subtraction\n\t[4] - Division\n >>")
b = float(input("Number 2 >>"))

calculator[operation].call(a,b)