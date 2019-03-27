s='HelLo worlD yes'

print(s.upper())
print(s.lower())
print(s.count('L'))
print(s.index('w'))

print(s.center(25,'D'))
print(s.islower())
p='hidhihihihihi'
s1=p.split('i')
print(s1)
s2=p.partition('d')
print(s2)
################################ Sets #########################
s1={1,2,2,3,3,4,5}
s2=s1.copy()
s1.remove(4)
s1.remove(2)
print("s1 is ",s1)
print("s2 is ",s2)
print("s1 difference is ",s1.difference(s2))
print("s1 intersection is ",s1.intersection(s2))
print("s1 intersect update is ",s1.intersection_update(s2))
print("s1 is subset of s2 or not", s1.issubset(s2))
print("s1 is subset of s2 or not", s1.issuperset(s2))
print("symmetric diff",s1.symmetric_difference(s2))
print("union data",s1.union(s2))
print("update set",s1.update(s2))
print("s1 is ",s1)

############### Dictionaries ##############
#d1={'k1':1,'k2':2}
#d2={k:v**2 for k,v in zip(['a','b']),range(2)}
#print("dict2 is ",d2)

#d={k:v**2 for k,v in range(5)}
#print('dictionary is ',d)

#####################Advanced Lists #############
l1=[1,4,3]
print('gives count of number',l1.count(4))
l2=[2,5]
l1.append(l2)
print('appended list is ',l1)
l1.extend(l2)
print('extended list is ',l1)
l1.insert(2,'Ram')
print('inserted list is ',l1)
l3=l1.pop()
print('pop list is ',l3)
l1.remove('Ram')
print('removed list is',l1)
l1.sort()
print('sorted lsit si ',l1)
#################################
n=453.54
print(hex(n))
print(round(n))