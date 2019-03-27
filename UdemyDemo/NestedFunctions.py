from string import ascii_lowercase as asc_lower

name='Ram Dasari'
x=10
def syahello():
    print("saying hello")
    name='SRU'
    def greet():
        print("Hello",name)
    greet()
syahello()


def globalVar1(x):
    print(f'value of {x} globally')
    x='RamSr'
    print('valu of {}'.format(x))
globalVar1(x)


def globalVar():
    global x
    print(f'second type value of {x} globally')
    x='RamSr'
    print('reassigned value of {}'.format(x))

globalVar()
print(x)

def VerifyPalindrome(name):
    rev=[]
    strev=name[::-1]
    if(strev.upper()==name.upper()):
        print("ur string is palindrome")
    else:
        print('ur string is not palindrome, sorry dude')
VerifyPalindrome('MaDaM')

def verifyRange(n1,n2,n3):
    if(n1<n3<n2):
        print("yes its in range")
    else:
        print("its not range")
verifyRange(1,99,56)

def pangrameVer(data):
    words=data.split()
    for all in words:
        for num in range(0,len(words)-1):
            if all[num].lower() not in asc_lower:
                print('this is not in english: ',all[num].lower())
            else:
                print('this is in english: ',all[num].lower())

pangrameVer('He is a very bad boy')