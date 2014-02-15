# employee.py
# - a class that inherits from person

class Person:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email  = email
        self.phone  = phone

class Employee(Person):
    def __init__(self,name, email, phone, title):
        Person.__init__(self,name,email,phone)
        self.title=title
    def __str__(self):
        return '[Person: %s, %s, %s, %s]' % (self.name, self.phone, self.email, self.title)


dorai=Employee('Dorai Thodla','dorait@imorph.com','555-1212','CTO')
#print dorai.name, dorai.email, dorai.phone, dorai.title
print dorai