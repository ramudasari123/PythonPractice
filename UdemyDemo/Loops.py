from random import *

mylist1=[1,2,3,4,5,6,7,8,9,10]

mylist2=[(1,2),(3,4),(5,6)]
for i in mylist1:
    if(i%2==0):
        print(i," is a even num")
    else:
        print(i," is odd num")

print("list2 data is ",mylist2[2][0])
for data in mylist2:
    print("data is ",data)
    print("second element is ",data[1])
dict1={'name':'ram','age':12,'ph':985423456}
for key,value in dict1.items():
    print("key is ",key," value is ",value)

###################################################
print(" ########################While Loops##################")
x=1
while (x<=10):
    print(x)
    if(x>5):
        break
    x=x+1
####################################################################
indexpos=0
for value in 'auhdjkeyfceu':
    print("inex {} at letter {}".format(indexpos,value))
    indexpos+=1

###################ZIP###################################
list1=[1,2,3,5]
list2=['name','age','ph','nm']
for data in zip(list1,list2):
    print("combined zip list values are ",data)

list3=list(zip(list1,list2))
print(list3)
tup1=list3[0]
print("tup is ",tup1)
######################################shuffling##############
randlist=shuffle(list2)
print("random list ",randlist)
print("random value ",randint(0,3))
########## write string as list in single line ##########
mine='Ramihfdsuklb'
minelist=[letter for letter in mine]
print("string modified list is ",minelist)

minelist2=[num**2 for num in range(1,5)]
print("num square list is ",minelist2)

minelist3=[x if x%2==0 else 'Odd' for x in range(1,10)]
print(minelist3)

minelist4=[x*y for x in [1,2,3] for y in [10,20,30]]
print("multiplied list is ",minelist4)