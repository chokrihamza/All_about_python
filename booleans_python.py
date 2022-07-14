print(10 > 9)
print(10 == 9)
print(10 < 9)

#the following booleans are true

print(bool("abc"),bool(123),bool(["apple", "cherry", "banana"]))
# the follwing booleans are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# if you have a function

"""
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

"""


  # test if an object is an instance of a class
x = 200
print("instance ",isinstance(x, int))

  # if you have a class with __len__ return false
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))