import math

n = float(input("Input number of sides: "))
l = float(input("Input the length of side: "))

print("The area of the polygon is:", ((n * l ** 2) / (4 * math.tan(math.pi / n)))) 