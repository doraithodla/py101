class Animal:
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place

    def speak(self,):
        print("%s just did a %s" % (self.name, self.sound))



# This class inherits kind and place arguments from Animal class (which can work for any animal)
# Initiates a Dog object with name, gender and breed parameters.

class Dog(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.sound = "woof"
        Animal.__init__(self, 'Dog', 'Ground')


# Cat class inherits the paramets of use for a Cat (similar things)
# like name, gender and breed, which they both share, also the getallinfo method and initiate them.
class Cat(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.sound = "meow"
        Animal.__init__(self, 'Cat', 'Ground')


# Here I create 3 objects, 2 dogs and 1 cat with selected arguments.
# And check for some methods on the objects.
Mickey = Dog('Mickey', 'Male', 'Bulldog')
Flora = Dog('Flora', 'Female', 'Pug')
Tina = Cat('Tina', 'Female', 'Persian')
Tina.speak()
Mickey.speak()
