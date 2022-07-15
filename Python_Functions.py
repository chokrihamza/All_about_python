# create a function in python

"""
def my_function():
    print("Hello from a function")
    my_function()
"""


# calling the function


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# arbitrary arguments *args
""" 
If you do not know how many arguments that will be passed into your function,
 add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments,
 and can access the items accordingly:

"""
def garden(*kids):
    # the function will receive a tuple of the arguments
    print(kids)

garden("alex","stive","jhon")  # Arbitrary Arguments are often shortened to *args in Python documentations
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.
def my_function1(child3, child2, child1):
  print("The youngest child is " + child3)

my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function2(**kwargs):
  print(kwargs) # the arguments are passend in a dictionary

my_function2(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#You can send any data types of argument to a function
# (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function
def my_function4(food):
   food.append("kiwi")


fruits = ["apple", "banana", "cherry"]

my_function4(fruits) # reference passage
print(fruits)

# use the return value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# u can use pass inside a function to never get errors
# now let's get an idea about recursion
# vary useful
#a function that call is self

# use recursion to reverse a string
# str="hamza" -> how can i reverse it
# first thing first i have to find the base condition
# when the string is empty "" return ""
# ""+str[1]
# in the parameter we have an index for the postion
def reverse(str):
    # base condition
    if len(str)==1:
        return str
    return reverse(str[1:])+str[0]

print(reverse("hamza"))
print(reverse("123456789"))

# this is the recursion to inverse a string