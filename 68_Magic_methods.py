# a = 5
# b = 'World'
# print(a+b)
# The moment you try to run above code, it gives an error saying unsupported operands types
# We can't use 'int' & 'str' for '+', so all this things are pre-defined
# All these things are called as Synthetic Sugar, which simply means it's trying to simplify the code for user
# Behing the scenes, things are abit different
# Imagine if a=5 & b=6, then what happens in behind the scene?
a = 5
b = 6
print(a+b)
# trust me whatever happens in Python happens with help of object & here as well, when you talk about a & b,
# the type of it is 'int', so 'int' is a class here.
# What's happening here is when you say a+b, which is of type integer, it is calling something
# So, behind the scene it is calling int.__add__()
# The moment you say int.__add__(), this is taking 2 parameters
# So, whatever we're doing in print(a+b) can same be done as here below
print(int.__add__(a, b))
# In programming, whatever you want to do, you will be doing that with the help of methods & __add__ is a
# method which belongs to the 'int' class

# So, even if u say print(a+b), behind the scene int.__add__(a,b) is getting called!

# If now both a & b become strings, then even the str.__add__() method is getting called behind the scene
a = '5'
b = '6'
print(a+b)
print(str.__add__(a, b))

# Now, you knwo that
# The moment you put +, it calls the __add__() method
# The moment you put -, it calls the __sub__() method
# The moment you put *, it calls the __mul__() method
# So, we've different methods for different operators!
# Normally, those things are called as "Magic Methods"
# So all these operators, behind the scene works as Methods
