# TYEPS OF ARGUMENTS:
# 1. Formal Arguments : At time of defining function
# 2. Actual Arguments : At time of calling function

# TYPES OF ACTUAL ARGUMENTS:
# 1. Position : We use position order to pass data
# 2. Keyword : We use keywords in function call to pass data (bcoz we don't remember exact sequence)
# 3. Default : When some argument is not passed, so function itself takes default value of it
# 4. Variable Length : You can define a function where no. of arguments isn't fixed

# 1-POSITION
print("Running Case-1")
def person(name,age): # name & age are formal arguments
    print(name)
    print(age)

person('navin',28) # 'navin' & 28 are actual arguments # Here we're using position order


# 2-KEYWORD
print("Running Case-2")
# If we don't have access to person() function, so we don't know whether 1st position is age or name
# In that case, we can call function as follows
person(age=28,name='navin') # Here we're using keywords


# 3-DEFAULT
print("Running Case-3")
def person(name,age=18): # name & age are formal arguments
    print(name)
    print(age)
person('navin') # If we're not passing age value, it will take default as age=18
person('navin',28) # If we're passing age value, it will over write default 


# 4-VARIABLE LENGTH
print("Running Case-4")
def sum(a,b):
    c = a+b
    print(c)
sum(5,6)
# What if we need to add 5, 10 or more numbers
# If u want to add 2 numbers we would be atleast having 2 arguments 
# So, the first one is confirmed & the length of second one isn't confirmed
# So, in b we're gonna accept 1 value or multiple values
def sum(a, *b): # *b mans b can have multiple values
    # c = a+b # But we cannot directly add 'int' & 'tuple', thatshwy this will throw as error!
    c = a
    for i in b:
        c += i
    print(c)
sum(5,6,34,78) # 5 will be assigned to a & 6,34,78 will be assigned to b in a tuple
# Above code can also be re-written as
def sum(*b):
    c = 0
    for i in b:
        c += i
    print(c)
sum(5,6,34,78)

