print('HiRam'[1])
x='hello world'
x=x.upper()
print(x)
x=x.lower()
print(x)
print(x.split())
print('hello {1} and {0} and {2}'.format('Ram','ASh','Anu'))
y=100/110
print('valu is {r:1.3f}'.format(r=y))
print(f"say {x}")
#######################Lists##########################################
list1=['hi','ram',56,567,7]
list2=list1[1:]
list3=list1+list2
print('list3 is ',list3)
print(list1+list2)
print('append list is',list1)
print(list1.index(56))
list1.append('ash')
list1.insert(2,'anu')
print(len(list1))
list1.remove('hi')
list1.pop(-1)
print(list1)
#############################Lists###########################################
list4=[1,5,2,97,4]
list4.sort()
print(list4)
list4.reverse()
print(list4)
list4.pop()
print('pop is',list4)
###########################Dictionaries##########################
dict1={'name':'ram','age':[1,4,'hi'],'may':{'nim':65}}
print('dict is ',dict1['age'])
print('dict2 is',dict1['may']['nim'])
list5=dict1['age']
num=list5[2]
num=num.upper()
print("value from dict to list to string is ",num)
print('items are ',dict1.items())
##############################################Tuples#########################
tup1=(1,4,'ram',45,9876)
print('tuple is ',tup1)
tup2=(1,2,[3,4])
print('tup2 data is',tup2)
####################################sets###########################
myset1=set()
myset1.add(12)
myset1.add('hi')
myset1.add(16)
myset1.add('his')
myset1.add('hi')
print("set is ",myset1)
myset2=set(list1)
print(myset2)
myset3=set(x.split())
print("splitted is ",myset3)