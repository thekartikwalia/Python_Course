# Function is a suite(or block) which performs one specific task

# It's good practice to have separate function for separate tasks, so that you can call them again
# It also has advantage : in future if you feel that your want to modify something, you'll be changing
# only one function, it won't effect other functions. You can test a particular function individually

# STEP-1 : Defining a function 
    # Syntax 
    # def function_name():
# STEP-2 : Calling a function 
    # Syntax
    # function_name()

# You can create multiple functions & can call them multiple times
# Function can be of 2 types, either it peforms task or it returns something

def greet():
    print("Hello")
    print("Good Morning")
greet()

def add(x, y): # Function takes arguments
    c = x+y
    print(c)
add(5,4)

# Your function can return a value as well (when you want to store output in a variable)
def substract(x, y):
    c = x - y
    return c
z = substract(8,4)
print(z)

# FUNCTION CAN ALSO RETURN 2 VALUES
def add_sub(x,y):
    c = x+y
    d = x-y
    return c, d  
result1, result2 = add_sub(5,4) # Since, we're returning 2 values, we need to accept 2 values as well
print(result1, result2) 