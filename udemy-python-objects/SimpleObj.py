class myDog():

    def __init__(self,breed):
        self.breed = breed

mydog = myDog(breed = 'Als')
print(mydog.breed)


class Circle:

    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_radius):
        self.radius = new_radius

myCircle = Circle()
myCircle.set_radius(100)
print(myCircle.area())
