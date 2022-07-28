class Parrot:
    # class attribute
    species="bird"
    # instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # instance methods
    def sing(self,song):
        return "{} sings {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing ".format(self.name)

# create an object from the Parrot class

parrot1=Parrot("Blu",10)
parrot2=Parrot("Woo",20)

# access the class attributes

#print("Blu is a {} ".format(parrot1.__class__.species))
#print("Woo is a {} ".format(parrot2.__class__.species))

# access the instance attributes
#print("{} is {} years old".format( parrot1.name, parrot1.age))
#print("{} is {} years old".format( parrot2.name, parrot2.age))

# call our methods
#print(parrot1.sing("Happy"))
#print(parrot1.dance())

# inheritance in python

