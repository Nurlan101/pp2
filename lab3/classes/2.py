class Shape:
    def __init__(self):
        pass           #the area of Shape is 0 by default
    
    def area(self):
        print("Area of the shape is 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(f"Area of the square is: {self.length * self.length}")    #calculate the area of the square and print it

length = float(input())
square = Square(length) 
square.area()
