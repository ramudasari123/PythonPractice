def check(n):
    result=[]
    for val in range(n):
        result.append(val**2)
    return result

res=check(8)
print(res)
########################################  YIELD ######################
def verifyyield(n):
    for num in range(n):
        yield num*2
for x in verifyyield(8):
    print(x)

g= verifyyield(2)
print('next value is',next(g))
print('next value is',next(g))

list1=list(verifyyield(10))
print('final list is ',list1)
######################################String iterator################3
def siter():
    s='Hello'
    for m in s:
        yield m
sis=siter()
print(next(sis))
print(next(sis))