# I want to have 2 variables 
# 1 which defines type of CPU i'm working with & the other which defines the amount of RAM i have
class Computer:

    def __init__(self,cpu,ram): # Normally we use __init__ to initialize variables
    # __init__ is like constructor in C++ it will get called automatically at time of object creation
        print("init")
        # The thing is every object needs to have a value 
        # cpu & ram are just an argument 
        # If you want it to be a part of your object, you need to assign this value to a object
        # And we know object here is self, so we need to say 
        self.cpu = cpu
        self.ram = ram
        # Again, there's no compulsion that you should be having same name, you can have different name

    def config(self):  
        # print("Config is ",cpu,ram)
        # Above line of code gives error, CPU isn't a local variable, CPU belongs to an object
        # So, we need to use self to refer to object 
        print("Config is ",self.cpu,self.ram)
        # That's the idea behind passing self, we're passing it so that you can use it to fetch values


# Object Creation
com1 = Computer('i5',16) # Behind the scene 3 arguments(object, value, ram) are passed
# Whatever value we're passing here which is 'i5' goes to the CPU as a argument it will be assigned to
# the object which is self
com2 = Computer('Ryzen 3',8) # Behind the scene, com2 also gets passed
# Here, "init" is printed 2 times (1 time for each object)

com1.config() 
com2.config()


# You can imagine your methods & your data works together & we've name for this concept (discuss later)
# But we're binding data with every method, so 1 object will have it's own Method & it's own variable
# They're working together