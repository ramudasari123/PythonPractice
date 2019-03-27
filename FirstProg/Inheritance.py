class school:
    def __init__(self,name,age):
        self.Tname=name
        self.Tage=age
        print("teacher name given is {} and age is {}".format(self.Tname,self.Tage))
class student(school):
    def parent(self,name,age):
        school.__init__()
        print("teacher name is {}".format(name))

p=student("anu",26)