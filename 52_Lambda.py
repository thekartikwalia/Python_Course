# We define function by using def function_name()

# What if i don't mention the function name, it becomes anonymous
# Thatswhy we can create a function called as Anonymous functions (Functions without name) 
# Such functions are also called as "Lambda"

def square(a):
    return a*a 

result = square(5)
print(result)
# Now when we talk about functions we expect that it will have atleast 3-4 lines of code 
# But the above function has only 1 line of code
# We're wasting 2 lines with a "def" keyword & a "return" keyword & with name of function 

# What if you want to use a function only once & you don't want to define the name of the function & 
# you only have 1 expression
# When we talk about function, there's 1 thing about functions 
# We can pass functions to a function 
# The way you pass values & the way you pass objects, you can also pass functions
# because functions are objects in Python 

# Above code works perfectly but the only problem i have is i will not be using this square function 
# mutiple times, i will be using this square function only once & that too it has only 1 expression

# So, instead of defining function, we can define function where you want to use it directly 
# Syntax for doing so is by using keyword lambda
# lambda argument : operation on argument
# To use this lambda, as functions are objects, obviously you need to assign it to some variable
f = lambda a : a*a # f -> represents your function (You can use this function in other functions as well)
result = f(5)
print("Running Lambda function")
print(result)

# Lambda function which add 2 numbers
f = lambda a,b : a+b
result = f(5,6)
print("Running Lambda function")
print(result)

# POINT TO REMEMBER
# You can pass any number of arguments but it should be only of 1 expression