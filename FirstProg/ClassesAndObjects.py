class Student:
    def classPeople(self, name,age):
        print("names are {} and age is {}".format(name,age))
    def seniorsections(self,name,age):
        print("names are ",name,age)
    ##constructor method
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.cadre="human"
        print("person name is {} and age {}".format(name,age))
    def __str__(self):
        return ("Name is {} \nAge is {}".format(self.name,self.age))

s= Student("rams",17)
s.classPeople("Dasari",16)
print(s)
#s1=Student('names',26)