# person.py
# - classes and objects
class Person:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email  = email
        self.phone  = phone

# test
if __name__ == '__main__':  # When run for testing only
     # self-test code
    dorai = Person('Dori Thodla')
    sue = Person('Sue Jones', email='sue@imorph.com')
    print(dorai.name, dorai.email)
    print(sue.name, sue.email)
