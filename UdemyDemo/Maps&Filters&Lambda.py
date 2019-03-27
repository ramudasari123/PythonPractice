names=['ram','sru','dd']
def filters(num):
    for val in num:
        if len(val)%2==0:
            return 'Even'
        else:
            return num[0]
name=list(map(filters,names))
print(name)

def evenver(nums):
    return nums%2==0

numb=[1,2,3,4,5]
lists=list(filter(evenver,numb))
print(lists)

list1=list(map(lambda num: num**2, numb))
print("list1 lambda exp is ",list1)

lists=list(filter(lambda num: num%2==0,numb))
print("lists lambda exp is ",lists)