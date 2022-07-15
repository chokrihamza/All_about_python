"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

"""

mylist=["banana","cherry","lemon"]
print(mylist)

""" 
Lists are :
 * ordered 
 * changeable 
 * allow deplicated value 
 

"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist,len(thislist))

# lists in python allow any data types and also mixed value
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"] # mixed list
print(list1,list2,list3,list4,type(list1))

#It is also possible to use the list() constructor when creating a new list.

mynewlist=list("hamza")# inside it any type of iterrable like string ,hashtable list tuple ...

print(mynewlist)

# access list items

print(list1[0],list1[-1])
print(list((list1[0],list1[-1])))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# check if the element exists in the list
if "apple" in thislist:
    print("yess apple is in the list of fruits  ")

#change elments in a list:
thislist = ["apple", "banana", "cherry"]
# change one item
thislist[0]="orange"
print(thislist)
# change a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3]=["watermelon","pear"]
print(thislist)

# we can change one element by a bunch of elements
thislist = ["apple", "banana", "cherry"]
thislist[1:2]=["blackcurrant","watermelon","orange"]
print(thislist)
# chnage two value by a simple value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# using the insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon")
print(thislist)
# add list item
#by using insert or append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.insert(1, "kiwi")
print(thislist)
# extend list
# append another list to the first list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#extend use any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = "kiwi,ananas"

thislist.extend(thistuple.split(","))

print(thislist)
# remove list items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
#print(thislist)

del thislist
#print(thislist)

# the clear() method : list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# loop through lists
thislist = ["apple", "banana", "cherry"]
for item in thislist:
    print(item)

# loop using index

for i in range(len(thislist)):
    print(thislist[i])

# using the while loop

i=0
while i<len(thislist):
    print("while loop " ,thislist[i])
    i+=1

# loop through the using of list comprehension
thislist = ["apple", "banana", "cherry"]
[print("list  comprehension",x) for x in thislist ]

# list comprehension python

#without using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for item in fruits:
    if "a" in item:
        newlist.append(item)



print(newlist)

# with the list comprhension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1=[x for x in fruits if 'a' in x]
print("newlist1",newlist1)

# [expression for item in iterable if condition == True]

print([x for x in range(11) if x%2==0])

print([x for x in range(10) if x <= 5])

names=["alex","jhon","keen","jeanique"]

print([x if x!="jhon" else "stive" for x in names])

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort descending
thislist.sort(reverse=True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#we can even sort by customize functions
#this by using key=function
def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key=myfunc)

print(thislist)

# the sort is case insensitive in python
# so u can use key=str.lower
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# make a copy of a list using copy() or list() methods
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

print(mylist)

# using the join method in lists
# first : using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)

# you can use append ,extend or just a loop for of while or whatever other technic
# using the count() function in python
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

print(points.count(9))
print(points.count(1))