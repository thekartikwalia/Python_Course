def div(a,b):
    print(a/b)

div(2,4)

# I want irrespective of sequence in which i pass value, numberator should be bigger than denominator
def div(a,b):
    if(a<b):
        a,b = b,a
    print(a/b)

div(2,4)
 
# Imagine [if(a<b): a,b = b,a] this code is not with you, this is in some other file and you're 
# importing it. Maybe you don't have access to this function & maybe you don't want to change the code 
# of the existing function
# So, i want you to swap those 2 values without touching the div() function 
# Thatswhere decorators comes into picture 
# Using Decorators you can add extra features in the existing functions

# Creating a function which would be a decorator for div() function 
# This decortaor will accept a function 
print("Running decorator")
def smart_div(func): # Creating a new function which takes function as a parameter
    # Then we can define a function inside a function which is actually replacing the code of div 
    def inner(a,b):
        if(a<b):
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)
# You don't have to go for a new name, you can replace it with original itself
div = smart_div(div) # Making a new div function from the old div function
div(2,4)
# Basically we're changing the way div works 

# The amazing part about decorators is you can change the behaviour of the existing function at the
# compile time itself