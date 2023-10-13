# I want to add 2 numbers, so i've to create a method let's say sum which is gonna take 2 arguments  
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # OLD FUNCTION 
    # def sum(self,a,b):
    #     s = a+b 
    #     return s
    # MODIFIED FUNCTION 
    # def sum(self,a,b,c):
    #     s = a+b+c
    #     return s
    # HIGHLY MODIFIED FUNCTION 
    def sum(self,a=None,b=None,c=None):
        # Declare s outside, so you can use it anywhere, say s is by-default 0
        s = 0
        # Passing 3 arguments
        if(a!=None and b!=None and c!=None):
            s = a+b+c
        # Passing 2 arguments
        elif(a!=None and b!=None):
            s = a+b
        # Passing 1 argument
        else:
            s = a

        return s



s1 = Student(58, 69)

print(s1.sum(5,9)) # Old function case
# What if you want to pass 3 values but this isn't possible as you're passing 3 arguments & accepting only 2
# that means you need to create another method called as sum which will take 3 arguments, that's what we do in
# other languages 
# But here we won't do that, here what we can do is we will modify same function to take 3 arguments
print(s1.sum(5,9,6)) 
# So now we're passing 3 arguments & we're accepting 3 arguments it will work
# But what if i'm not passing 3rd argument, i'm passing only 2 arguments 
# Now, the problem starts because you're expected to pass the 3rd argument as well
# How do we solve this?
# To solve this thing we can use a concept where you'll say a=None 
# Other options is we can use the variable length arguments which we had done before
# But in the early option you can say all the values are by-default None which means even if we don't pass their
# value, these are default arguments, so even if you don't pass a value, their default value would be None
# So that means even if you don't pass any value, it will work & all the values will become None 
# None will be replaced by values 5,6,9
print(s1.sum(5))

# So, this is your "Method Overloading", so we're overloading methods but then we're not doing directly because
# it doesn't support in Python, so we're doing some trick!