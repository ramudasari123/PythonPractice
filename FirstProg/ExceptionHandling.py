a = int(input("enter A"))
b = int(input("enter B"))

try:
    c=a/b
    print(c)
except:
    print("improper values given")
else:
    print("loop is done")


############Print formatting patterns###########
name=input("enter name")
age=input("enter age")
height=input("enter height")

print("name is %s, age is %s , height is %s"%(name,age,height))
print("name is {1} and age is {0}".format(name,age))
print("name is {1} and age is {0}".format(age,name))
print("{:1} {:2} {:3}".format(2,3,4))