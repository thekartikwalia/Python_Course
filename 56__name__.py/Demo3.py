from Calc3 import add

def fun1():
    add()
    print("from fun1")

def fun2():
    print("from fun2")


# fun1()
# fun2()

# When you work on a project & if this is your stand alone application or stand alone code, this is the 
# only file you're going to write in your project, normally what we do is we define everything in a 
# function because statements should be a part of a function, so even fun1 & fun2 calling should be done
# inside a function. This is the standard procedure we all follow.
def main():
    fun1()
    fun2()
# main is a static point of execution, so generally we define the function name as main
# And ofcourse main will not be calling itself.
# So, if we run the above part we won't get any output as we need to call main as well

main() 

# So you're calling 1 function main() and it will take care how to execute all the statements and then
# you can call them right. This is how generally we make a software!
# So, we have a main function & from main function, you'll call all other functions


# Now, i want to use Calc3 in this & fun1() want to use add()
# So, i want to reuse add() in Demo3.py
# So, for this we need to import Calc
# ALL THIS IS DONE ABOVE AT INITIAL LINES OF CODE 


# When we run this code, then we're getting even "result 2 is" i.e. sub() is also running but we don't
# want that as we're not calling sub()

# This is bcoz the moment you import a library(or a module), it will execute all the statements & in 
# that you can see we've main, whcih is calling main & it calls all the functions, we don't want that

# So, we have to say hey, i want to call main only when i am executing this particular file (Calc3.py)
# as a standalone program, so i only want to call main() when i call Calc3.py as a standalone program
# We don't want to call main when we're running it from another file
# Why do we want to call a main() of Calc3 when i'm running Demo3 as my first code, i'm using Calc3 as
# a module 
# In that case, you'll call main() of Calc3 only when i'm running Calc3 as standalone code 


