class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.list=[]
        print("Hello {} your age is {}.".format(name,age))
        
    def marks(self,newmark):
        self.list.append(newmark)
        #print self.list
        
    def avg(self):
       print (sum(self.list) / len(self.list))
       if sum(self.list) / len(self.list) >= 20:
            print ("Well done")
       else:
            print ("Work hard")
            
s=student("Brajesh", 23)
s.marks(20)
s.marks(10)
s.marks(40)
s.avg()
