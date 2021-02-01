class Animal:
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place


# This class inherits kind and place arguments from Animal class (which can work for any animal)
# Initiates a Dog object with name, gender and breed parameters.

class Dog(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        Animal.__init__(self, 'Dog', 'park')


Mickey = Dog('Mickey', 'Male', 'Bulldog')
print(Mickey)
print(Mickey.breed)
print(Mickey.kind)
