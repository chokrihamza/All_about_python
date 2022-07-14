print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

# loop through a string

for i in "banana":
    print(i)
# string length

print(len("hamza"))

# check string

print("hamza" in "hello hamza how are you")
# use it inside an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)
# Use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# slicing string

text="hello there how are you"
print(text[0:5])
print(text[:5])
print(text[5:])
print(text[-3:])

# modify strings
a = "Hello, World!   "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("Hello","bye"))
# Split String

print(a.split(" "))

# String concatenation
a = "Hello "
b = "World"
c = a + b
print(c)

# Python - Format - Strings
"""
age = 25
txt = "My name is John, I am " + age
print(txt)
-------------------------------------------------------------
this code will generate a error 
cause we trying to concatenate string with number
instead we do
"""
age = 25
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Python - Escape Characters
"""
txt = "We are the so-called "Vikings" from the north."
this code will generate a error 
"""
# to fix it we use  backslash
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

name="hamza\b"
print(name)