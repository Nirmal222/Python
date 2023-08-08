#this is a single line comment

"""
This helps us to write 
multiline comments
"""

# Variables
x = 5
y = "John"
# All the variable names are case sensitive 

# legal Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Cases
# Camel Case-> myVariableName = "John"
# Pascal Case-> MyVariableName = "John"
# Snake Case-> my_variable_name = "John"

# Many Values to multiple variables 
x, y, z = "Orange", "Banana", "Cherry"
# One Value to Multiple Variables
x = y = z = "orange"

# unpacking a collection 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

"""Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword."""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# type casting
x = str(3)
y = int("3")
z = float(3)

# To get the type we can use a method provided by python : type(x)
print(type(x))
print(type(y))