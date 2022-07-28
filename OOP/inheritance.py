# parent class
class Bird:
    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# Child class

class Penguin(Bird):
    def __init__(self):
        # call the super() function
        super().__init__()
        print("Penguin is ready too")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()