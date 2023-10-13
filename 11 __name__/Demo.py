# print(__name__)

# main is a static point of execution

# The moment you run this code, if this is your first code because in your project you might have 
# multiple modules, but there will be some module which you'll run first, so this example demo.py is
# my first module
# First module name is always main
# But that is the point of execution, that is the point from where code starts 
# So, the value of name here is main


# What if i go back to Calc 

import Calc
# Now what will happen is, everything which is there in Calc will come to this demo file including the 
# print statement 
print("Demo says: " + __name__)
# Ofcourse demo will print main
# Now, Calc will print the name of the module i.e. Calc 