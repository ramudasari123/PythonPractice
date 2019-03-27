class parent:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        print("parent name is {} , age is {} , phone is {}".format(self.name,self.age,self.phone))
    def __str__(self):
        return ("parent name is {} , age is {} , phone is {}".format(self.name,self.age,self.phone))
class staff(parent):
    def __init__(self,name,age,phone,prof):
        parent.__init__(self,name,age,phone)
        self.prof= prof
        print("profession is ",prof)
    def __str__(self):
        return ("business is {}".format(self.prof))

st = staff("RD",22,9876543210,"business")
print(st)