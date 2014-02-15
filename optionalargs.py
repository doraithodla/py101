# optionalorgs.py
# This program demonstrates the ability to use optional arguments
# in python

def emp(name,phone=None,email=None):
    print
    print "---", name
    if phone:
        print phone
    if email:
        print email

# only name given
emp('Dorai Thodla')

# name and phone
emp('RD Burman',phone='212-5555')

# all params
emp('Mr X',phone='212-5555',email='x@x.com')

# notice the different order or parameters
emp('Mr Y', email='y@y.com')