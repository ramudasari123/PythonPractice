def sayhello(name):
    '''
    this is demo program
    '''
    print("say hi to "+name)

sayhello('Ram')

def summation(*args):
    return sum(args)*0.5

value= summation(2,5,6)
print(value)

def mulargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("fruit is {}".format(kwargs['fruit']))
    else:
        print('sorry no fruit')

mulargs(fruit='banana',vegitable='kakara')

def kwarsAndargs(*args,**kwargs):
    print(args,kwargs)
    for n in args:
        print('list is ',n)
    for key1,val1 in kwargs.items():
        print("key is {} and values is {}".format(key1,val1))

kwarsAndargs(1,3,5,6,name='rd',size='good',case='bus',ph='9653356')

def myfunc(*nums):
    list1=[]
    for n in nums:
        if n%2==0:
            list1.append(n)
    return list1
lists=myfunc(1,4,3,5,6,9,8)
print(lists)

def casees(val):
    listd=[]
    for n in val:
        if val.index(n)%2==0:
            n.upper()
            listd.append(n)
        else:
            n.lower()
            listd.append(n)
    total=''.join(listd)
    print(total)

casees("sdfghgkjfdh")

def worddiv(text):
    listword=text.upper().split()
    print(listword)
    print("0 0 is ",listword[0][0])
    print("1 0 is ", listword[1][0])
    return listword[0][0]== listword[1][0]

res = worddiv('grand mother')
print("startus is ",res)