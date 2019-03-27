list1=['how','are',2,4,5,'you']
list2=['what','are',6,8,'you',9,'doing']
tuple1=('hi',3,'rowdi')
tuple2=(12,'run',56)
dict1={'name':'ram','age':18,'phone':98765325,'marital':'unmarried'}
dict2={'name':'DSA','age':17,'phone':95268974,'marital':'unmarried'}

print("combined list is ",list1.append(list2))
print("dict value is ",dict1['phone'])

Name='Ramu is bad'
print("value is string is :",Name[3])
print("changed string can be ",Name[:4],"are")

def Demo(age=12,name='RD'):
    age=age-2
    print("user age is ",age,"name is ",name)
    Name = 'SA'
    print("name is ",Name)
    list3=list2
    del list3[2]
    print("list 3 values are ",list3)
    return list3

def practice():
    a=20
    print("a value is ",a)
    return

a=practice()
print("a is ",a)
lists= Demo(name='hi',age=19)
print("final list value is ",lists)