class Shape:
    def __init__(self):
        pass                  #the area of Shape is 0 by default
    
    def area(self):
        print("Area of the shape is 0")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):        #calculate the area of the rectangle
        print(f"Area of the rectangle is: {self.length * self.width}")

length = float(input("Lenth:"))
width = float(input("Width:"))
rectangle = Rectangle(length, width)
rectangle.area()
