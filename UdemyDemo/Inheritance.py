'''
This below is Inheritance Examples******************overridingMethods
'''
class Animal():
    def __init__(self):
        print("HI, I am an Animal")
    def foodHabits(self):
        print("Hi, I eat food")
    def bark(self):
        print("I do barking")

class Dog(Animal):
    def __init__(self):
        print("I am dog")
    def foodHabits(self):
        print("I need chicken")


animals=Dog()
animals.foodHabits()
animals.bark()
'''
The below are polymorphism&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
'''

