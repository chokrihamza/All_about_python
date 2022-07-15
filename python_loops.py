"""
Python has two primitive loop commands:

while loops
for loops

"""
# while loop
# example
i=1
while i<6:
    print(i)
    if i==3:
        break # we break the loop if the condition is true
    i+=1

# break statment
# continue statment
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #we stop the current iteration
  print(i)


# else in the while loop

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# for loop in python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# loop through a string

for i in "banana":
    print(i)

# same thing you can use break and continue
# use the range() function

for i in range(6):
    print("i",i)
for x in range(2, 6):
  print(x)

# increment the sequence by steps
for x in range(2, 30, 3):
  print(x)

# else in the for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# the pass statement
for x in [0, 1, 2]:
  pass