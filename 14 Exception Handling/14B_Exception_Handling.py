# Statements if of 2 types 
# 1. Normal 
# 2. Critical : will not give any error 

a = 5
b = 0

try :
    print(a/b) # This line would give me the error
except Exception as e: # This is where you'll handle it
    print("Hey, you cannot divide a number by Zero",e)
    # This message is better than showing error!
    # Infact you can not just print a message, you can do whatever things you need eg: you can
    # peform some operations 



print("Bye")
# On making b=0, it gives eroor & it's not printing 'bye' as well, that means your execution is 
# getting stopped in between
# You don't want that 
# So if you want to solve this problem we've to use a special block, see at this line of code we
# are getting exception, we're getting error 
# Whatever block you've you just need to put that in a try block or in a try statement 
# We've a special thing called as try, so what we're saying is that hey this line of code is a 
# critical statement, i'm not sure if this would work or not, so try to execute that, so 
# python will say ok since you're writing this a try block, i'll try to execute, in case of error
# i'll except the error & the way you do that is by writing exception 



# The moment you don't have any Error, it'll not execute the except block bcoz except block will 
# be executed only when you have an Error

# But what if you want to print the message error as well (what is the error ?)
# So, you can use 'e' as a representation or object of Exception 


# It's always a good practice that whenever you open a resource (like file), always close it!
# Let's say if i open a resource inside try block (if i'm opening a file here, or i am opening a
# database connection here), then where should we close it ?
# Should i close it inside try block like below :
print("CASE-1 : Closing in try block")
try:
    print("Resource Open")
    print(a/b)
    print("Resource Closed")
except Exception as e:
    print(e)
# This gives output as Resource Open then prints error 
# It is so bcoz the moment you get the exception at line print(a/b), it's jumping outside the 
# statement in the except block, so it means instead of closing in try block we should close it 
# in except block like below :
print("CASE-2 : Closing in except block")
b = 2
try: 
    print("Resource Open")
    print(a/b)
except Exception as e:
    print(e)
    print("Resource Closed")
# But now what if i change value of b to be non-zero, you will see that it won't be saying 
# Resource Closed bcoz you won't be executing the except block if you don't have an Error!
# So should i put resource closed in both the blocks (try & except) ?
# No, we don't have to because Python provides you 1 more feature which is called finally, it
# says it doesn't matter if you're getting the exception or not, i'll execute
# Finally block will be executed if we get error as well as if we don't get error 
print("CASE-3 : Closing in finally block")
try: 
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)
except Exception as e:
    print("You cannot divide a number by zero!",e)
finally:
    print("Resource Closed")
# If i enter 'p' it even then says "You cannot divide a number by zero! invalid literal for int() 
# with base 10: 'p'"
# Let's try it outside the try block
print("For Different Types of Errors, we've different names as well & general one is exception")
# So, exception will be on top.
# So, even if u say Zerodivisionerror, it's a part of exception
# What you can say is hey i want to say "You cannot divide number by zero" only when there's a
# ZeroDivisionError

try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)
except ZeroDivisionError as e: # Trying to handle ZeroDivisionError
    print("You cannot divide a number by zero!", e)
except ValueError as e: # Trying to handle ValueError
    print("Invalid Input!",e)
    # What if you get a error which you don't know about, in that case, at the end to be on safe 
    # side you'll say Exception, it'll try to handle all the other errors which are not ZeroDivision 
    # & ValueError
except Exception:
    print("Something went wrong!")
finally:
    print("Resource Closed")

