class Animal():
    """docstring for Animal"""

    def __init__(self):
        print('Animal created')

    def bark(self):
        print('Animal Barking')

    def smell(self):
        print('Animal smelling')


class Dog(Animal):
    """docstring forDog."""

    def __init__(self, name='defaultDog'):
        self.name = name
        print("Dog is created")

    #Dog's own methods
    def eat(self):
        print("Dog is eating")

    def __str__(self):
        return "Dog value, {}".format(self.name)


myAnimal  = Dog()
myAnimal.bark()
myAnimal.smell()
#BELOW to SHOW DEFAULT STRING METHOD
print(myAnimal)
