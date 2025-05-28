x = 5
y = "John"

# Change type after being assigned
x = "Sarah"

# Casting type
x = str(3)  # Convert x to string
y = int(3)
z = float(3)  # Convert y to integer

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

name = "John"
# is the same as
name = 'John'

# Case sensitivity
a = 4
A = "Sally"
# a and A are different variables, A will not overwrite a

# Variable names
# 1. Start with a letter or underscore
# 2. Can contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 3. Cannot start with a number
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. A variable name cannot be any of the Python keywords.

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Use these to make variables more readable
# Camel Case: myVariableName
myVariableName = "John"
# Pascal Case: MyVariableName
MyVariableName = "John"
# Snake Case: my_variable_name
my_variable_name = "John"

# Many value to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to Multiple Variables
x = y = z = "Turquoise"
print(x + " " + y + " " + z)

# Unpack a collection
color = ["Red", "Green", "Blue"]
x, y, z = color
print(x)
print(y)
print(z)

# Output variable using print()
# x = "Python is awesome"
# print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z) #Result: Pythonisawesome (not have space)

x = 5
y = "John"
#print(x + y)  # This will raise an error because you cannot concatenate a string and an integer
# Using comma to separate variables in print
print(x, y)  # This will print: 5 John

# Global Variables
# This will print: Now the value of x is awesome
# Global variables can be changed inside a function
# Local variables can be created inside a function
x = "awesome"
def myfunc():
   x = "fantastic"  # This is a local variable
   print("Now the value of x is " + x)

myfunc()
print("But the value of x is " + x)  # This will print: But the value of x is awesome

# Global keyword
def myfunc2():
   global y
   y = "dazzling"  # This will change the global variable y


myfunc2()
print("Python is " + y)  # This will print: Python is dazzling