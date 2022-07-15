# create tuples in python
mytuple=("cherry","banana","apple")

print(mytuple)

# tuples are ordered ,unchangeable and it allow duplications
mytuple=("apple","banana","cherry","apple")

print(mytuple,len(mytuple))

# tuple with one item
thistuple = ("apple") #this is like <class 'str">
print(type(thistuple))
thistuple = ("apple",) #this is now <class 'tuple"> when you add that comma,
print(type(thistuple))

#in tuple we can contain any type of data
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1,tuple2,tuple3)

# tuples can contain different type of data and this never create a problem
mytuple=("hamza",True,1,2,3,4)
print(mytuple,type(mytuple))
# we can create a tuple using our construor tuple
thistuple=tuple("hamza") # put inside any iterable you want
print(thistuple)
thistuple=tuple({"name":"hamza","lastname":"chokri"})
print(thistuple)

#how to access tuples
thistuple=("hamza","alex","jeanique","stive","maria","vangheluwe")
print(thistuple[1],thistuple[-1])

# same you can use a range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# negative ranges
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
# you can use if  condition to check if an elemnt is in the tuple
#Update Tuples
# Change Tuple Values , as said that tuples unchangeable or immutable
# frankly you can do this only in you convert it to a list and than reconvert it to a tuple one more time
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add items using append() same when just you convert it to a list

x = ("apple", "banana", "cherry")
x=list(x)
x.append('kiwi')
x=tuple(x)
print(x)

# you are allowed to concatenate tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# remove item only and only if you convert it to a list

# u can delete a tuple
thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple)

# unpack a tuple
# in list we just do :

(a,*b)=["cherry","banana","kiwi"]

print("values",a,b)
# in tuples
(a,b,c)=("cherry","banana","kiwi")
print(a,b,c)

# u can use asterisk * to pack all in list
(*a,b)=("cherry","banana","kiwi")

print(a,b)

# we loop through the data by using for or while loop
# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# u can manipluate lists as you wish

print([1,2,3,4]*5)  # retrun [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# using tuples
print((1,2,3,4)*2)

# retun the index of a tuple

tuple1 = ("a", "b" , "c")

print(tuple1.index("b"))
