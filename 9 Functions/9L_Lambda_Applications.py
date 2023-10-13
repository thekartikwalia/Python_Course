# We're gonna use 3 functions: filter(), map() & reduce()



# FILTER() -> In-built function
# We want to fetch all the even numbers from a list 
def is_even(n):
    if(n % 2 == 0):
        return True
    else: 
        return False 


# Above function can be re-written as 
def is_even(n):
    return (n % 2 == 0)
nums = [3, 2, 6, 8, 4, 6, 2, 9]
# filter() function takes list from you & will filter it to give you values
# filter() will take a sequence & will give a sequence, but we want list, so we'll use list() function
# Syntax of filter() -> filter(function,iterable), here iterable means sequence
evens = list(filter(is_even, nums))
print(evens)


# Writing above code using Lambda function 
nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(lambda n : (n % 2 == 0), nums))
print(evens)


# MAP() -> In-built function
# Now, we want to double all the even numbers present in a list
# When you want to change any value, we can use very simple concept as map()
# map() will take a sequence & will give a sequence, but we want list, so we'll use list() function
# Syntax of map() -> map(function,iterable), here iterable means sequence
def update(n):
    return n* 2
doubles = list(map(update, evens))
print(doubles)

# Writing above code using Lambda function
doubles = list(map(lambda n : n*2, evens))
print(doubles)



# REDUCE() -> belongs to module functools
# We need to import it from module first
from functools import reduce
# We want to reduce the values, so instead of having multiple values, i want only one value
# I want to add all this values 
# We keep on adding 2 values at a time to get sum of all values (At 1 point we add 2 values)
# Since, we're not expecting multiple values, so we aren't gonna use list 
# We're gonna use reduce() function for this
# Syntax for reduce() -> reduce(function,sequence)
def add_all(a,b):
    return a+b
sum = reduce(add_all,doubles)
print(sum)

# Writing above code using Lambda function
sum = reduce(lambda a,b : a+b, doubles)
print(sum)
