'''
Created on 27-Jun-2018

@author: ramu.dasari
'''
heros = ['prabha','pawan','ntr','mahesh']
print(heros)

heroines = ['kajal','anushka shetty','samantha','sreya']
print(heroines)

print(heros[0:2])
print(heroines[1][1])
heros.append('nani')
print(heros)
heros.insert(1, 'vijay')
print(heros)
print("sorted list is ",heros.remove("nani"))
print("lenght is ",len(heros))
print("max is ",max(heros))
print("min is ",min(heros))

actors = (1,2,3,4,5)
newactor = list(actors)
print(newactor)
print(newactor.__sizeof__())