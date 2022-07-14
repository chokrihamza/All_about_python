"""
There are three numeric types in Python:

1-int
2-float
3-complex

"""

x=1
y=2.8
z=3j
print(type(x),type(y),type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# python random number
""" 
Python does not have a random() function to make a random number,
 but Python has a built-in module called random that can be used to make random numbers:
"""
import random

print(random.randrange(1,11)) # random variable between 1 and 10

# Python Casting

#using python constructors
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x=int()
print(x,y,z)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x,y,z,w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)