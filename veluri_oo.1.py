class Father:
    print("Father properties ;")
    def __init__(self, p, m):
        self._properties = p
        self._money = m
    
    def properties(self):
        print("father properties are: ", self._properties)
        return self._properties


    def money(self):
        print("father money are: ", self._money)
        return self._money

class Son(Father):
    print("Son properties ;")
    pass

f = Father("2Acres", "200000")
f.properties()

s = Son(4,800000)
s.properties()