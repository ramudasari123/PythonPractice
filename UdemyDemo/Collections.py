from collections import *

word="how many times each word is repeated for word times"
words=word.split()
print(Counter(words))
###################Default dictionaries   ##################
dect=defaultdict(lambda: 0)
dect['one']
dect['two']=2
print(dect)

###############   Ordered Dictionaries ###################

dect1={}
dect1['a']=1
dect1['b']=2
dect1['c']=3
dect1['d']=4
dect1['e']=5

print("dictinary is",dect1)

dect1=OrderedDict()

for k,v in dect1.items():
    print(k,v)
############################## Equal verify tuples  ##########
dec1=OrderedDict()
dec2=OrderedDict()

dec1['a']=1
dec1['b']=2

dec2['b']=2
dec2['a']=1

print(dec1==dec2)

#############################  Named tuples ######
details=namedtuple('dog','age breed height')
qs=details(age=2,breed='german',height=2)
print(qs.age)
