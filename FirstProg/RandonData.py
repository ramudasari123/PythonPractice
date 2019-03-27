import random
import string

list1=[1,4,6,7,'ram',4,9,2,8]
print(random.randint(1,100))
print(random.random())
print(random.randrange(10,100))
print(random.choice(list1))
random.shuffle(list1)
print(list1)
###############################String generator#############

data=string.ascii_letters
name= ''.join(random.sample(data,5))
print(name)

choice='asdfghjxcvbnm'

for i in range(8):
    name=''.join(random.choice(choice))

print(name)

name=''.join((random.choice(choice)) for i in range(10))
print(name)