class CSStudent:
    stream ='cse'
    def __init__(self,roll):
        self.roll = roll

a = CSStudent(101)
b = CSStudent(102)
print(a.stream) 
print(b.stream)        
print(a.roll) 
print(CSStudent.stream) 

# o/p:
# cse
# cse
# 101
# cse
# PS F:\Coding Practise\GTT Python Training> 
