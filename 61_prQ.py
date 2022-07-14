# Write a Python class which has two methords 'get_String' and 'print_String'.

# get_String : accept string from the user 
# print_String : print string from the user

class InOpString():
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input()

    def print_String(self):
        print(self.string.upper())

str1 = InOpString()
str1.get_String()
str1.print_String()

# o/p:
# India
# INDIA
# PS F:\Coding Practise\GTT Python Training> 