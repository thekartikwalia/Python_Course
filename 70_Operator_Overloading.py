
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        # This is how you add values 
        # m1 will have addition of self m1 & other m1 
        # m2 will have addition of self m2 & other m2 
        # Once you got this 2 values, you'll be creating a new student object by passing these 2 values
        s3 = Student(m1,m2)
        # Once you got the student, you'll return s3 here
        return s3
        # Now, the moment you say s1+s2, it will return the value, return a new object of student & will 
        # assign that to s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if (r1>r2):
            return True
        else:
            return False
        
    def __str__(self):
        # return self.m1, self.m2
        # now if i run this code, it will return a Tuple ofcourse 
        # So, now if you want to print the object, it will not print the address, it will print the values
        # because we're overriding the __str__
        # print(s1) will still give an error of __str__ returned non-string(type tuple)
        
        # When you directly call print(s1), Python attempts to print result of the __str__ method of s1 object.
        # In your original code, the __str__ method returns a tuple ((self.m1, self.m2)), which is not a valid 
        # string representation, hence the error.
        # In contrast, when you explicitly call print(s1.__str__()), you are explicitly calling the __str__ 
        # method on the s1 object, and then you print the result. Since you're directly invoking __str__, 
        # Python doesn't complain about the return type, and it prints the result without an error.

        # To clarify:
        # print(s1) tries to print the result of s1.__str__(), which is why it attempts to use __str__ method.
        # print(s1.__str__()) explicitly calls the __str__ method on s1 and prints the result, bypassing the 
        # implicit call that print(s1) would make.

        # To make print(s1) work, you should return a formatted string to display the values of m1 and m2. 
        # For example, you can modify it like below:
        return '{} {}'.format(self.m1,self.m2) # You're returning a string now




s1 = Student(58,69)
s2 = Student(69,65)

# Now, i want to apply the operator here, which is '+' operator, i want to add these 2 students 
# The moment i say s1+s2, i want a different student object 
s3 = s1 + s2
# Now, we know that '+' operator means it will add 2 values, but it is possible with the help of integer, it 
# is possible with the help of string.
# Is it possible to use the '+' operator with Student class ?

# As you run above code it will give you an error saying that we cannot use '+' between 'Student' & 'Student'
# because we have not defined it 
# If you remember behind the scene even if you use '+' with an integer it'll be calling a __add__() method
# But if you see our class, we don't have that add method 
# Because if you say s1 + s2, how your compiler, how your python will know what to do 
# That's where you need to define it, that's where you've to say Hey, the moment anyone says '+' of a student
# you need to call this method, called as add
# So you can overload the operator & you can change the defination for it, you can define anything you want 
# It takes 2 parameters self & other, so behind the scene 
# s3=s1+s2 this code is getting converted into -> Student.__add__(s1,s2) which takes 2 parameters s1 & s2 
# 1st parameter is Self & s2 is the other parameter 

print(s3.m1) 
# So, if you want to add 2 students, you need to overload the operator of '+' because the integer knows what is 
# '+', string knows what is '+', but your Student class don't know what does that '+' means
# So '+' means call the __add__() method, but we don't have __add__() method here, so we've to define our own 
# method 
# the same things can be doen with substraction, multiplication

# Now, i want to compare if 2 objects are greater than or equal to 
if (s1>s2):
    print("s1 wins!")
else:
    print("s2 wins!")
# So what we're trying to do here is whoever has maximum marks they'll win 
# but when you say maximum marks, how will you check it because we aren't defining it ?
# Maybe i want to check only 1st marks which is m1 or maybe i want to check m2 or maybe variation of both
# For it you need to define method which is __gt__ which means greater than (__ge__ is greater than equal to)
# Because behing the scene that's what's happening, it is saying Student.__gt__(s1,s2) & it is passing 2 
# variables s1 & s2, so s1 goes to self & s2 goes to other 


# So if you want to peform any operation on objects which are user-defined, you've to define all this methods

a = 9 
print(a) # It prints value of a 
print(a.__str__())
print(s1) 
print(s2)
# The moment you try to print s1, it will not print the values of s1, it'll try to print the address of s1
# Here, we don't want address, we want values, then why's this happening ?
# Whenever you try to print the object, doesn't matter is it integer or your class, behind the scene it is 
# calling a method called as __str__(). Even if you don't call it, it is happening behind the scene!
# The moment you say print(a) it will try to call a.__str__() & thatswhy you're getting their output
# You're getting 9 because it is calling __str__() 

# In the same way, the moment you say s1, even this is calling __str__, and now if you run following command,
# you'll see it's giving the same output, that means it is calling the __str__()
print(s1.__str__())
# When you clcik on __str__() you'll se it's in builtin, so even if you don't define __str__ method in your
# own class, it is getting defined somewhere & taht defination is printing the module_name, it is printing 
# the name of the cladd & it is printing the object_address
# We don't want that, we want values right 
# That means we need to override this method to return values of m1 & m2


# POINT TO REMEMBER:
# Whenever you peform any operator like addition, substraction, division etc. 
# Behind the scene, we're calling methods 