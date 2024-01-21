x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Name
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)

#Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Variable Exercises 
#Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"
#Ex.2
x = 50
#Ex.3
x=5
y=5
print(x + y)
#Ex.4
x=5
y=5
z=x+y
print(z)
#Ex.5
x, y, z = "Orange", "Banana", "Cherry"
#Ex.6
x = y = z = "Orange"
#Ex.7
def myfunc():
    global x
    x = "fantastic"
