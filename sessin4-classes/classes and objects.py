# classes.py
# - classes and objects
class Employee:
   'Common base class for all employees'
   empCount = 0 # This is a class variable

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# Adding some members
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

# Check and display
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employees %d" % Employee.empCount

# Adding new attributes
emp1.location="California"
print emp1.location

class Manager(Employee): # Manager is an employee




