# Python by default don't support abstract classes, you'll not see Python supporting it directly 
# But we've a module which is ABC module which we can use here to achieve abstract classes
# ABC stands for Abstract Base Classes
# We can use that to create our own abstract classes 
# What is Abstract Class & why do we need it ?

from abc import ABC, abstractmethod


# class Computer:
class Computer(ABC): # Making Computer class -> Abstract
    def process_early(Self):
        print("Running")
    # Whenever your method has a body, it's a Normal method

    # But what if i don't want to mention anything inside this method, i want it to be blank
    # I just want to declare this method. When you say declare it simply means it doesn't have a body
    # The way you can declare a method is by saying 'pass'

    @abstractmethod # Tells that process is an Abstract method
    def process(Self):
        pass
    # This methods which only have declaration but not a defination, we call them as Abstract Methods
    # A class which have abstract Methods, is called "Abstract class"
    # This type of concept is there in ohter languages well like Java, C# but in pythons it's abit different
    # Becuase Python by default does not support Abstract classes 
    # Now, if you want to make it Abstract class, you need to do something
    # There's 1 more thing about abstract class, that you cannot create an object of it 



# com = Computer()
# com.process()
# Above line of code doesn't give error! That means we're able to create ans object of it because it's not a
# Abstract class yet

# How do you make a abstrcat class ?
# For that you've to import a module abc & in it, you've to import only 2 things ABC & asbtract method 
# Then make class Computer a subclass of ABC, so that this also becomes an abstract class 
# Now, above abstract method, you need to tell this method is abstract by using decorator @abstractmethod

# Now, com = Computer() gives error -> Can't instantiate abstract class Computer with abstract method process
# If you make a class Abstract, you can't create an object of it, bcoz we've a method which isn't defined 

# BEFORE DEFINING FUNCTION INSIDE LAPTOP 
# class Laptop(Computer):
#     pass
# com1 = Laptop() 
# Gives same error : Can't instantiate abstract class Laptop with abstract method process
# That's the thing Laptop is inheriting Computer in which you've abstract method, so it is compulsion for 
# you to define that method, otherwise even this class Laptop would be Abstract class 


# DEFINING FUNCTION INSIDE LAPTOP 
class Laptop(Computer):
    def process(self):
        print("It's running!")

com2 = Laptop()
com2.process()
# Now, this is working 



# You can see we can create a class & that class will implement all the methods 
# And if you fail to implement all the methods, all the abstract methods you'll get an Error!
# Now this is what Abstract Class is, Abstract class will've atleast 1 abstract method 

# What's the use of this concept of Abstract Classes ?
# If you look at statements, we're calling a process() & this rpocess is geeting called from Laptop, so what's 
# important here is a Laptop class, what do you think is the use of Computer class anyway.any
# So even if i remove that it'll not make any difference 
# I can remove this class Computer as extense & it'll surely works!
# See this thing makes sense only when your class Computer has some extra methods which Laptop needs 
# Then it makes sense to use a Computer 
# but what if your class only has Abstract Methods, does it make any sense ?
# Yes, it makes sense only when you're designing an application in a OOPs way 
# So basically when you follow the concept of Object-Oriented Programming, you've to follow some patterns
# And 1 of the pattern is, let's say if you've alot of classes 
# eg: let's say you talk about a programmer
class Programmer:
    def work(Self,com): # Passing Computer type for now 
        # com can be anything, it can be a Laptop or a Desktop or a mobile phone or white board 
        # Will white board work ? 
        # Can i pass an object of white board here ?
        print("Solving Bugs!")
        com.process()

class Whiteboard:
    def write(self):
        print("It's writing!")


prog1 = Programmer()
# Now, what's important is as a programmer you need a machine to work with 
# Ofcourse you can't work on paper. Programmers writes code on Laptop or mobile phone or on Desktop
# So ofcourse you need a Computer here, now what you think what type of object should i pass to work ?
# Will it be a type of Laptop or a type of Computer ?

# If i pass the object of Laptop, there's no problem 
print("Passing Laptop object")
prog1.work(com2) 
# It prints 'solving bugs' bcoz we're work(), it prints 'running' bcoz from this method we're calling process 
# Because as a programmer we write a code & we've to say process 

# But what if i create an object of Whiteboard & if i pass an object of Whiteboard you can see there's no compile
# time issue
print("Passing Whiteboard object")
com3 = Whiteboard()
# prog1.work(com3)
# This gives an error: 'Whiteboard' object has no attribute 'process', bcoz Whiteboard don't have method which 
# is process(). Now why it doesn't have a process method ? Becuase there's no compulsion for a Whiteboard to 
# implement or to have that method whichis process()

# And if you say hey, whiteboard is a computer, in this case it becomes compulsion for this whiteboard to have 
# this method which is process()
# that's the design aspect, it is not that you can't write a code without abstract classes but then sometimes 
# it also  depends upon the desgin, the way you design your application, the way you design your classes
# So this is the one way of defining a class, you can create a Abstract class so taht the other classes will be
# having some signature or some restriction to which method to define 
# Eg: When you define APIs, so you can create a API. If someone wants to use your API, they've define all the 
# methods.
# So that's how we use Abstract classes & Abstract Methods 
# And it's not that you can have only 1 abstract method, you can have multiple Abstract methods & you can also
# have normal methods there 

# QUICK RECAP:
# Abstract class has atleast 1 abstract method in a class 
# Abstract methods are methods which doesn't have a definition, they only has a declaration 
# And if you want to use them in Python
# Since python by default does not support it, then you need to import a module which is ABC which stands for 
# Abstract Base Classes 