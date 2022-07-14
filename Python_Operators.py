"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

# start with the modules
x = 5
y = 2

print(x % y) # print 1

x = 5

x &= 3

print(x)

# the or condition
x = 5

x |= 3

print(x)

# test equility between  lists
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # true

# returns True because z is the same object as x

print(x is y) # false

# returns False because x is not the same object as y, even if they have the same content

print(x == y) # true

print(x is not z)
print(x is not y)
print(x!=y)

x = ["apple", "banana"]

print("banana" not  in x)
print("kiwi" not in x)