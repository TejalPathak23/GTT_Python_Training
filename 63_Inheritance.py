# class childClassName (ParentClassName):
#     'Optional class Documentation String'
#     class Suite

class Person:
    def __init__ (self,name):
        self.name = name

    def getName (self):
        return self.name


    def isEmployee (self):
        return False        

class Employee(Person):
    def isEmployee (self):
        return True

emp = Person('Sejal') # An Objject of Person
print(emp.getName(), emp.isEmployee())        

emp1 = Employee('Tejal') # An Objject of Employee
print(emp1.getName(), emp1.isEmployee())

# o/p:
# Sejal False
# Tejal True 
# PS F:\Coding Practise\GTT Python Training> 