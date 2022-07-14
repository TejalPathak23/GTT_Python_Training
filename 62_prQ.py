# Write a python class named Rectangle constructed by a length and  a width and a method which will compute the area of the rectangle.

class Rectangle():
    def __init__(self, len, wid):
        self.length = len
        self.width = wid
    def rectangle_area(self):
        return self.length * self.width


newRectangle = Rectangle(11, 5)
print(newRectangle.rectangle_area())

# o/p:
# 55
# PS F:\Coding Practise\GTT Python Training> 
