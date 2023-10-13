import math 
# # Import library to use math functions

print(math.sqrt(25))
print(math.floor(2.9)) # Floor of any number btw [2,3) is 2
print(math.ceil(2.1)) # Ceil of any number btw (2,3] is 3
print(math.pow(3,2)) # pow(x,y) = x ^ y = x ** y

# # Math Library also contains values of some constants 
print(math.pi)
print(math.e)

# # Each time writing fullname of library is difficult, so we use consept of allies
import math as m
print(m.sqrt(25))

# What if we don't want to import everything, we just want to import some of functions not all
from math import sqrt, pow 
# Now we don't even need to specify math because we're import function itself
print(sqrt(25))
print(pow(3,2))

# You can use help() to learn more about math library
help('math')