class Father:
    print("Father properties ;")
    def __init__(self, properties, money):
        self.properties = properties
        self.money = money
    
    @property
    def properties(self):
        print("father properties are: ", self._properties)
        return self._properties

    @properties.setter
    def properties(self, p):
        self._properties = p

    @property
    def money(self):
        print("father money are: ", self._money)
        return self._properties
    @money.setter
    def money(self,m):
        self._money = m

class Son(Father):
    print("Son properties ;")
    pass

f = Father("2Acres", "200000")
f.properties

s = Son(4,800000)
s.properties