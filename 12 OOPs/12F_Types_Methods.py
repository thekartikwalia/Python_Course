# TYPES OF METHODS:
# 1. Instance Method - which works with instance variables
    # In Instance itself we've 2 different types : 
    # a. Accessor Methods: Used when you just want to fetch the value of instance variables
    # b. Mutator Methods: Used when you want to modify the value of instance variables
# 2. Class Method - which works with class variables 
# 3. Static Method - which works with nothing (when you need to do something extra with your class)

# In variables, class & static variables are same, but that's not the case with methods
# So, in case of methods, class & static methods are different

# When working with Instance, we use a 'self' keyword in methods
# When working working with class, we use a 'cls' keyword in methods


# I want to know the average of marks
class Student:

    school = 'NKBPS' # Class(or Static) Variable 

    def __init__(self,m1,m2,m3): # m1, m2, m3 are Instance Varaibles 
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    # avg is a instance method. As we're passing self we know it means that it belongs to a particular object 

    def get_m1(self): # Instance (Accessor) Method
        return self.m1
    # Getters only fetch the value, thatswhy said Accessors
    
    def set_m1(self,value): # Instance (Mutator) Method
        self.m1 = value
    # Setters changes the value, thatswhy said Mutators


    @classmethod
    def getSchool(cls): # Class Method
        return cls.school


    @staticmethod
    def info(): # Static Method
        print("This is student class.. in abc module")
    # This method has nothing to do with the class variables & the instance variables 
    # Now, where it would be useful, so let's say if you want to peform any operation which has something to 
    # do with the other class objects, we can use static methods 
    # If you want to peform some operation like finding the factorial of a number because see factorial has 
    # nothing to do with the class variables or instance variables, maybe you're passing a value, you just 
    # want what's the factorial of the number, you can use static methods there





s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(s2.avg())

# Class methods should work with all the objects, so we can use class_name for it 
print(Student.getSchool())
# Above line of code give error -> Student.info() missing 1 required positional argument: 'cls'
# We don't want to pass 'cls', we aren't passing it for avg() also

# If you want to create a class method, we need to use a special symbol or special way of doing that & we can
# use something called 'Decorators'
# We've to mention '@classmethod' just above class method

# If you want a method which has nothing to do with instance variable & which has nothing to do with the class
# variable, we don't do something extra, so something which is not concerned with variable. 
# At that time, you'll we using a static method because we are not concerned about instance variable & we are 
# not concerned about class variable 
# Eg: Let's say i want to print info about this class, not about student but the class


# For static method as well we need to use a special decorator '@staticmethod'
# You've to use a class_name to call it
Student.info()
# It's static, so you don't need to pass anything not even a class, not even a object 
