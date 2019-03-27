command='print only the words starts with s in sentence'
list1=command.split()
for val in list1:
    if val[0].lower()=='s':
        print(val)

list2=[x for x in range(1,51) if x%3==0]
print("list divide by 3 is ",list2)

for val in list1:
    if len(val)%2==0:
        print(" lettes {} is even".format(val))
list3=[]
for data in range(1,101,1):
    if data%3==0 and data%5==0:
        list3.append("FizzBuzz")
    elif data%3==0:
        list3.append("Fizz")
    elif data%5==0:
        list3.append("Buzz")
    else:
        list3.append(data)
print(list3)
len()