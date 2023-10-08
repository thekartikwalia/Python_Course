# We can create variable inside a function & even outside the function as well
# that's where a concept comes into picture called 'Scope'

# A program can have 2 variables with same name if they've different scope
a = 10 # GLOBAL Variable -> declared outside the function (It's scope is everywhere)
def something():
    a = 15 # LOCAL Variable -> declared within the function (It's scope is inside function)
    print("In function",a)
something()
print("Outside",a)

# Inside the function, preference would always be given to the local variable


# What if i don't have a variable inside function
a = 10 
def something():
    print("In function",a)
something()
print("Outside",a)
# We can access a global variable inside the function as well


# By default, inside function local variable is given preference 
# But what if we want to change value of global variable inside a function
# To use a global variable inside function, we need to use keyword global 
a = 10 
def something():
    global a # Now, preference is given to global vairbale 'a'
    a = 15 # We don't have a local variable here, this is a global variable bcoz of above statement
    print("In function",a)
something()
print("Outside",a)

# We cannot have global & local variable in same function
# Bcoz once we mention global a inside the function
# Then, it treats every a to be global


# We want a local vairable a, but we also want to change the global variable a 
# For this, we can use function globals() 
# Using globals(), we can access the global variable address
a = 10
print(id(a))
def something():
    a = 9
    # globals() function will give you all the global variables (not just 1)
    x = globals()['a'] # So, we need to specify which global variable we need to access
    print(id(x))
    # To change value of global variable don't change value of x coz it will just create new memory for it
    # Rather change the value of global a using function globals()
    globals()['a'] = 15
    print("In function",a)
something()
print("Outside",a)
# Since, id's of both a & x are same, so it means that both of them refer to same object

# So, if u want to change global variable a without affecting the local, then we use globals()['a']