# Syntax for defining a class:
# class class_name:
# Stuffs you can put in a class -> Attributes(Variables) & Behaviour(Methods(or Functions))
# Syntax for defining a object of a class:
# object_name = class_name()
# Syntax for calling Method of a class:
# 1. class_name.method_name(obj_name)
# 2. obj_name.method_name()
# Normally, we prefer using the (2) syntax for calling methods of a class 

class Computer:
    # Defining some Methods
    def config(self): # self is the object which you're passing
        print("i5, 16gb, 1TB")

a ='8'
print(type(a)) # 'str' is in-built class ('a' is a object of string)

# Creating objects of class Computer
com1 = Computer()
com2 = Computer()

print(type(com1)) # 'Computer' is our class

# Computer.config()
# Above line of code gives an error because a class has mutiple objects. 
# In this case, we're using only 1 object which is com1
# The thing is this config() method will change it's behaviour based on the object because different 
# object have different behaviour because dependent on what they know they've different behaviour
# In this case, config() is not depending on any data, but may be there's a chance that this config()
# will depend on some data & every object will have it's own data
# So, we need to call config() by telling for which object i'm calling it
Computer.config(com1) # Hey, i want to call config() for com1
Computer.config(com2) # Hey, i want to call config() for com2
# We're same data because at this point we're not changing data for different objects (can do later)

# Another way for calling config:
com1.config() # In this case, you're using object itself to call the function
com2.config()
# Behind the scene, config() will take that com1 as a argument & it'll pass that in self