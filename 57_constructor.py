class Student:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    def displayStudent(self):
        print('Roll No :',self.rollno ,'| Name :',self.name)    

emp1 = Student(121,'Ajeet')
emp2 = Student(122, 'Sonoo')
emp1.displayStudent()
emp2.displayStudent()        

# o/p:
# Roll No : 121 | Name : Ajeet
# Roll No : 122 | Name : Sonoo
# PS F:\Coding Practise\GTT Python Training>
