'''
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import ipywidgets as widgets
'''
#import Decorators
tup1=(1,2,3,2,4,3,5)
list1=[1,2,4,57,2,6,6,6,7,8,8]
print(tup1.count(2))
print(tup1)
print(list1.count(6)," ",list1.pop(2))
#list1.append(99)
list1.insert(2,99)
list2=list1.sort()
print("sort is ",list2)

case=lambda num: num**2
print(case(3))

##################################

a_b_c=1_2000_20
a,b,c=2,4,5
print(a)