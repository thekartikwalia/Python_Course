class A:
    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("Feature 2 working!")


# What if you wnat to get features of class A as well in class B
# That's where Inheritance comes into picture 
# So, we can say hey!, this B is a child(or sub) class of A
# The moment you say child class, it will import all the features
# Syntax to say so is:
# class subclass_name(parentclass_name):
class B(A): # class B is inheriting all features from class A
    # So now, from the object of B you can also access features 1 & 2 of class A 
    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("Feature 4 working!")


class C(B):
    def feature5(self):
        print("Feature 5 working!")
        # So now, C is inheriting features of both parent class B & grand parent class A 
        # This is known as "Multi Level Inheritance" 



a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

# Inheritance simply means if you only have a class which provides some features And in future if u want to 
# create new classes in which you want to use those features, you just need to inherit them
# We can use some terminologies here like: super class & sub class OR parent class & child class 


# class B inherits from class A -> This is known as "Single Level Inheritance"

# We also have "Multi Level Inheritance" in which there comes grandparent class also along with parent & child 
# So, a child can access features from parent as well as grandparent 


# We also have "Multiple Inheritance" 
# When a single class inherits properties from 2 different parent classes 
# Consider a case when class B doesn't inherits properties from class A, and then if class c inherits properties
# from both the classes A & B, then such a case is known as "Multiple Inheritance"
# Syntax of doing so is :
# class subclass_name(parentclass1_name, parentclass2_name):
# class C(A,B)
# In above case, class C will inherits features from both class A & class B
# But class B doesn't inherit even a single features from class A


# We're done with following inheritances:
# 1. Single Level Inheritance
# 2. Multi Level Inheritance
# 3. Multiple Inheritance