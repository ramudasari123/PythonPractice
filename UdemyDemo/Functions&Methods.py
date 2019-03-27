class Cricle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.dimension=radius*radius*Cricle.pi
    def circumference(self):
        return self.radius*self.pi*self.dimension

circles=Cricle(20)
print('radius given is ',circles.radius)
circum=circles.circumference()
print("circum is ",circum)