list1=['ram','john','saleem','raju','michel']
print(list1[1])
list2=['nadiya','kajal','sriya','rakul','asha',56,78]
print(list2[1:3])
list1.insert(2,"ravi")
print(list1)
list3=list1+list2
print(list3)
print(list3[-3])

for i in list3:
    print(i)
k=list3.reverse()
print("list reverse is ",k)
list3.append("hi")
list3[1]="anu"
print(list3)
print("list length is ",len(list3))
list4=list3.reverse()
print(list4)
