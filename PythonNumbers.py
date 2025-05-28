x = 1 # int
y = 2.8 # float
z = 1j # complex

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

# int is a whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# You cannot convert complex numbers into another number type.
# c = 1j
# print(int(c))  # This will raise a TypeError

# Random number
import random
print(random.randrange(1, 10))  # Returns a random integer between 1 and 10

# Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

