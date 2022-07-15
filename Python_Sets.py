# a set in python
# A set is a collection which is
# unordered,
# unchangeable*,
# and unindexed.
myset = {"apple", "banana", "cherry"}
print(myset)

# Set items are unordered, unchangeable, and do not allow duplicate values
# Once a set is created,
# you cannot change its items,
# but you can remove items and add new items
# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset,len(thisset))

myset = {"apple", "banana", "cherry",1,2,3}
print(type(myset))

# u can just use the set constructor
thisset = set(("apple")) # note the double round-brackets
print(thisset)

# access data of a set
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# u can't change the value of a set one created but you can add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# add sets using update() method by any iterable
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") # remove() will raise an error if the element not exist

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")# discard() will NOT raise an error.

print(thisset)

# join two sets using union()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) # return in the same set

print(x)
# using itersection to return a new list
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.intersection(y)

print(z)

# symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)