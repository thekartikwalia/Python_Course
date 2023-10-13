def person(name, *data):
    print(name)
    print(data) # Prints in a tuple format
person('navin',28,'Mumbai',9865432)

# But if i want to print data in a proper way like age, hoemtown, etc.
# But i don't know what exactly the suer is passing
# So, here comes the concept of Keyworded Variable Length Arguments
# The difference is here, you also need to pass Keywords
def person(name, **data): # * doesn't accepts Keyworded argument, so we write ** instead
    # ** means you're passing multiple arguments but with the help of keywords
    print(name)
    print(data)
person('navin',age=28,city='Mumbai',mob=9865432)


# If you want to pass multiple data taht too with help of keyword, then you've to use 
# Keyword Variable Length Argument

# We can also use for loop to print key & value in a pair
def person(name, **data):
    print(name)
    for i,j in data.items(): # items() is function to access data from tuple
        print(i,j)
person('navin',age=28,city='Mumbai',mob=9865432)