# convert the first letter to upper case
# the name of the function is capetalize()

print("hamza ".capitalize())

txt = "python is FUN!"

print(txt.capitalize()) #convert the first lette rto upper and all the other to lower case

txt = "36 is my age."

x = txt.capitalize()

print (x)

# the next function in casefold
# return a function where all characters are lower case
txt = "Hello, And Welcome To My World!"
print(txt.casefold())

# center return a center function
txt="hamza"
print(txt.center(20,"*"))

# count The count() method returns the number of times a specified value appears in the string.

txt = "I love apples, apple are my favorite fruit"

print(txt.count('apple'))
print(txt.count("apple",10,24))

# encode :method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors='replace'))
""" 
errors types:
'backslashreplace'
'ignore'
'namereplace'
'strict'
'replace'
'xmlcharrefreplace'
"""

# endswith The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "Hello, welcome to my world."
print(txt.endswith("my world."))
print(txt.endswith("my world.",5,11))


# expandtabs method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"

print(txt.expandtabs()) #Default tabsize is 8
print(txt.expandtabs(2))
print(txt.expandtabs(10))

#The find() method finds the *first* occurrence of the specified value.returns -1 if the value is not found.
# the find() method is almost the same as index() the only difference is that the index() method raises an exception if the value is not found
txt = "Hello, welcome to my world."

print(txt.find('e'))
print(txt.find('e',5,10))
print(txt.find('q'))

# format method formats the specified value(s) and insert them inside the string's placeholder.
txt="For only {price:.2f} dollars"
print(txt.format(price=49))
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt2,txt3)

#The index() method finds the first occurrence of the specified value.
txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)
print(txt.index("e", 5, 10))
#print(txt.index("q"))

# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"

print(txt.isalnum())
txt = "Company 12" # we add a space

print(txt.isalnum())

# The isalpha() method returns True if all the characters are alphabet letters (a-z).
txt="hellothere"
print(txt.isalpha())
txt="hello there"
print(txt.isalpha())
# he isdecimal() method returns True if all the characters are decimals (0-9).
txt="1234568558"
print(txt.isdecimal())
txt="1234568558f"
print(txt.isdecimal())

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

# The isdigit() method returns True if all the characters are digits, otherwise False.
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
""" 
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9),
 or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

"""
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print("identifier",a.isidentifier())
print("identifier",b.isidentifier())
print("identifier",c.isidentifier())
print("identifier",d.isidentifier())

# The islower() method returns True if all the characters are in lower case, otherwise False.
""" 
Numbers, symbols and spaces are not checked, only alphabet characters.
"""
txt = "hello world!"

x = txt.islower()

print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

"""
Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values,
because all the characters in the string must be numeric, and the - and the . are not.

"""
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print("numeric",a.isnumeric())
print("numeric",b.isnumeric())
print("numeric",c.isnumeric())
print("numeric",d.isnumeric())
print("numeric",e.isnumeric())

#The isprintable() method returns True if all the characters are printable, otherwise False.
#Example of none printable character can be carriage return and line feed.
txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
txt = "   s   "

x = txt.isspace()

print(x)

txt = "      "

x = txt.isspace()

print(x)

#The istitle() method returns True if all words in a text start with a upper case letter,
# AND the rest of the word are lower case letters, otherwise False.
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print("title",a.istitle())
print("title",b.istitle())
print("title",c.istitle())
print("title",d.istitle())

# The isupper() method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print("upper",a.isupper())
print("upper",b.isupper())
print("upper",c.isupper())

#The join() method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

print("*".join("hamza"))

# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
txt = "banana"

x = txt.ljust(20, "O")

print(x)
# The lower() method returns a string where all characters are lower case.
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#The lstrip() method removes any leading characters (space is the default leading character to remove)
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)

#The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(mytable)
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))

#The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)

#The replace() method replaces a specified phrase with another specified phrase.
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

# same we have
""" 
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string


"""

# the split() method splits a string into a list.
txt = "welcome to the jungle"

print(txt.split())

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)

# The splitlines() method splits a string into a list. The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)

#The startswith() method returns True if the string starts with the specified value, otherwise False.

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)

#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

#The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
txt = "Welcome to my world"

x = txt.title()

print(x)
txt = "Welcome to my 2nd world"

x = txt.title()

print(x)

#The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
txt = "50"

x = txt.zfill(10)

print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))