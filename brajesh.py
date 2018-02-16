class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list = []
        print("Hello {} your age is {}.".format(name, age))

    def marks(self, newmark=None):
        if newmark:
            self.list.append(newmark)
        return self.list
        # print self.list

    def avg(self):
        return sum(self.list) / len(self.list)

    def approved(self):
        average = self.avg()
        if average >= 20:
            return "Well done"
        else:
            return "Work harder"



s = student("Brajesh", 23)
s.marks(20)
s.marks(10)
s.marks(10)
print("{} got marks: {} which lead to average: {}".format(s.name, s.marks(), s.avg()))
print("{}, {}!!".format(s.name,s.approved()))