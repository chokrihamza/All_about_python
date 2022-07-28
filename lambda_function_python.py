# Python Lambda
#A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# syntax lambda arguments : expression

# example
x=lambda a:a+10

print(x(5))

# multiply two functions
x = lambda a, b : a * b
print(x(5, 6))

# the power of lambda function
""" 
The power of lambda is better shown when you use them as
 an anonymous function inside another function.

Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:
"""

def my_function(n):
    return lambda a:a*n

mydoubler2=my_function(2)

print(mydoubler2(2))
mydoubler3=my_function(3)
print(mydoubler3(2))