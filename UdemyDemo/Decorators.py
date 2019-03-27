def Master(name="ram"):
    def child1(name):
        print("I am child1 {}".format(name))
    def child2(name):
        print(f"I am child2 {name}")
    if(name.upper()=="RAM"):
        return child1
    else:
        return child2

calling=Master("nadi")
calling("nadi")


###Passing one method/function as arguments to another function##############

def sayhello():
    print('Hi Ram')

def callerfunc(somefunc):
    print("I am calling some function")
    print(somefunc())

callme=callerfunc(sayhello)
#callme()
####################Decators#########################
def maindec(somefunc):
    def func1():
        print('code before modification')
        somefunc()
        print("code after modification")
    return func1()

@maindec
def somedefunc():
    print("decorator main func called")

#calldec=maindec(somedefunc)
#calldec()