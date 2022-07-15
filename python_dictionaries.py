# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable* and do not allow duplicates*.
# this is a hash table in python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,# this value will be overwrited
  "year":2020
}

print(thisdict)
print(thisdict["brand"])

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# u can put any type you want
print(thisdict,len(thisdict),type(thisdict))

# acces items by key to get the -> value
# u can use key or just u can use the get() method

print(thisdict.get("year"))
print(thisdict.keys(),thisdict.values(),type(thisdict.keys()))
print(thisdict.items())

# change items directly or by using update() method

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict.update({'brand':'BMW'})
print(thisdict)

# add items directly or by update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
thisdict['color']='red'
print(thisdict)

thisdict.update({'shape':'round'})
print(thisdict)
# remove by pop() or popitem()
for x in thisdict:
  print(x)   # this gonna print all the keys

for x in thisdict:
  print(thisdict[x])

for x,y in thisdict.items():
  print(x,y)


# copy dictionaries using the method copy() or using the dict constructor
# we can create nested dictionaries # like the JSON files
# Create a dictionary with 3 keys, all with the value 0: using fromkeys() method
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)