# first program mith python
print("hello world ")

# python use indentation to indicate a block of code

if 5>2:
    print("five is greater than two")

# we use hashtag for comments
""" or this """

# variables in python
x=5
y=2
print(x,y)

# cating in python
x=str(3) # return '3'
y=float(3)
z=int(3)
print(x,y,z)

# get the type

print(type(x),type(y),type(z))

# this code with generate a error my-var = "John"

""" 
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)


"""

# Assign Multiple Values

x,y,z="Orange", "Banana", "Cherry"
print(x,y,z)

age_alex=age_jhon=age_marie=20
print(age_alex,age_jhon,age_marie)

# Unpack a Collection
fruits = ["apple1", "banana1", "cherry1"]

x,y,z=fruits

print(x,y,z)

#Output Variables
#The Python print() function is often used to output variables.

text="python is awesome"
print(text)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # the result is separated "Python is awesome"
print(x + y + z) # the reslut is "Pythonisawesome"

# Python - Global Variables
""" Variables that are created outside of a function
 (as in all of the examples above) 
 are known as global variables."""
""" Global variables can be used by everyone, both inside of functions and outside."""

# example
