# TYPES OF VARIABLES:
# 1. Instance Variable
# 2. Class (Static) Variable 

class Car:
    wheels = 4 # class variable 
    def __init__(self):
        self.mil = 10
        self.com = "BMW"
        # These 2 variables (mil (mileage) & com(company)) are called as Instance Variables as Mileage & Company
        # are instances as when the object(car) changes, these values also changes

c1 = Car()
c2 = Car()

c1.mil = 8
# Since, it's changing now, so both the objects have different values 
# But what if i want to create a variable which is common for all the objects 
# Ofcourse these 2 are instance variables because they're different for different objects 
# If you change 1 object, it will not affect the other object 
# What if you want to have a variable which will change & it'll effect all the other objects 
# Eg: No. of wheels in a car is 4 right now, but what if in future we got a new concept & they're saying hey 
# now this time we will be having 5 wheels 
# In this case, what you'll do is, you'll define a variable outside __init__ because if you create or if you
# define the variable inside __init__, then it becomes a instance variable.
# If you define a variable outside __init__ & inside a class ofcourse, it becomes a class variable 

Car.wheels = 5
# The moment you change the value for wheels, it'll effect all the objects because they're shared
# So, this wheels variable is shared among all the objects

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

# If you want to access wheels (class variable), instead of using the object_name.(classvariable_name) we can
# also use class_name becuase if you talk about 'mil' & 'com' it is specific to the object, but that's not the 
# case with wheels, wheels is common to all the objects, so every object can share the same value of it.
# So, we can use object_name or we can use class_name, both works!


# In your memory you've different namespace
# namespace is an area where you create and store object/variable
# We've 2 types of namespace:
# 1. Class namespace - where you'll store all the class variables
#     Here, 'wheels' belong to class namespace
# 2. Instance (Object) namespace - where you'll create all the instance variables
#     Here, 'mil' & 'com' belong to instance namespace


# What if you wnat to change the value of wheels (class variable)
# Since, wheels belongs to class namespace, so if you want to modify it, you've to use a class_name