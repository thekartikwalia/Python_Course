# We're gonna talk about 2 topics in this section:
# 1. Constructor in Inheritance 
# 2. Method Resolution Order (MRO)
    # So, what happens is whenever you've this Multiple Inheritance, it will always start from Left to Right,
    # which means Left will be given preference over right  



# Subclass can access all the features of superclass but superclass cannot access any features of Sub class 
class A: # A is superclass

    # Defining my own constructor
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("Feature 2 working!")


class B(A): # B inherits properties from A # B is subclass

    def __init__(self):
        super().__init__() # We're trying to call the init method of parent class A
        print("In B init")

    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("Feature 4 working!")


print("Creating object for class A")
a1 = A() # Definately calls the constructor of A

print("Creating object for class B")
b1 = B()
# Will it call the constructor of A or not (know that B is inherited from A) ?
# Yes, even if you've object of B it will still call the constructor of A

# What if you've your own constructor in B ?
# Since, we don't have __init__ inside B, that's why it's going to A
# But what if you've a __init__ with you?
# After adding __init__ in class B, the object creation of B doesn't goes up to call constructor of A, it 
# rather calls constructor of B instead

# That means if you create an object of B, first it will try to find the __init__ of B, if that is not found,
# then it will go for A

# If you create object of sub class it will first try to find init of sub class, if it is not found, then it 
# will call init of superclass

# But what if u want to call init of A as well, is it possible ?
# if i create a object of B, can i call the init of both the classes i emant A & B
# See by default it will call only B right, what if i want to class A as well ?
# That's where we've a very special keyword or a method you can say, that is 'super()'
# So, you'll say super(). 
# The moment you say super, you can access all the features of the parent class  
# So, by writing super().init() we're trying to call init method of class A (parent class)
# The moment you say super, you're representing the super class, which in this case is A 

# POINT TO REMEBER:
# When you create the object of B it will call the init of B first & from the init of B you're trying to call 
# the init of A, so it will jump up and it'll execute the init of A first which will print "In A init" & then,
# it will come back to print "In B init", that's what we got as the output

# When you create object of Sub class it will call init of Sub class first. If you've call super, then it will 
# first call init of Super class then call init of Sub class



# Let's take case of Multiple Inheritance 
# A1 & B1 are 2 different classes and C1 inherits from both of them 
class A1: 

    def __init__(self):
        print("In A1 init")

    def feature1(self):
        print("Feature 1-A working!")

    def feature2(self):
        print("Feature 2 working!")


class B1: 

    def __init__(self):
        print("In B1 init")

    def feature1(self):
        print("Feature 1-B working!")

    def feature4(self):
        print("Feature 4 working!")

class C1(A1,B1):
    def __init__(self):
        super().__init__()
        # But what if you want to call the init method of superclass
        # but there's a twist here, now C1 has 2 Super classes A1 & B1
        # The moment you say super().__init__, what do you think which init will it call, init of A1 or B1 ?
        # The moment you run this code, it says "In A1 init", that means we're unfair here
        # We're biased towards A, we are not taking B here, this is completely wrong

        # But the thing is we've a concept of Method Resolution Order(MRO)
        # So, the moment you say init, it will try to find the init of itself, so since we've init here, it'll 
        # execute the init of C, then the moment you say super().__init__(), now we've 2 classes A1 & B1, on 
        # the left hand side we've A and on the right hand side we've B, so it'll prefer left one first, so 
        # it goes from Left to Right & that's something you've to remember
        # That's why we got "In A init" on object creation of C

        # The same thing can be done for methods 
        # So,let's say we've 2 methods which are same 
        # Here we've feature1 in A as well as in B, both are the same methods with same name ofcourse!  
        # Now, if i try to call feature1(), will it call from A or B ? (continued after c.features1())
        print("In C1 init")

    def feat(self):
        # In this i'm trying to call the method of super class
        super().feature2()

print("Creating object for class C1")
c = C1() # when object is of C, then it'll call the init of C only

print("Calling feature1() method from object of C1")
c.feature1()
# Now, if i try to call feature1(), will it call from A or B ? (continued)
#  It'll always call from A because it goes from left to right & you can see the output


# So, in this section we've talked about 3 things:
# 1. How constructor behaves in Inheritance ?
# 2. How to use super() method in Inheritance ?
# 3. Method Resolution Order (MRO)


# So, now infact with the help of super() method can we call function, let's see that through method feat()
print("Running feat() method of class C1")
c.feat() # Seeing whether it's able to call feature 2
# On running code, you'll see it wqorks!
# So, you can use super() method to also call other methods as well, not just init 

# So, to represent this Super class, we use super method 