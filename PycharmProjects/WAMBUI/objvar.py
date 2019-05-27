"""Represents a robot, with a name"""
#A class vraiable, counting the number of the robots
population = 0

def __init__(self, name):
    """Initializes the data."""
    self.name = name
    print("(IInitializing {0})".format(self.name))

    #When this person is created, the robot
    #adds to the population
    Robot.population +=1

def die(self):
    """I am dying."""
    print("{0} is being destroyed!".format(self.name))

    Robot.population -=1

    if Robot.population ==0:
        print("Therevare still {0:d} robots working.".format(Robot.population))
def sayHi(self):
    """Greeting aby the robot.
    Yeah,they can do that."""
    print("Greetings,my masters call me {0}.".format(self.name))
@classmethod
def howMany(cls):
    """Prints the current population."""
    print("We have {0:d} robots.".format(cls.population))
droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howmany()

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")
droid1.die()
droid2.die()

Robot.howMany()
