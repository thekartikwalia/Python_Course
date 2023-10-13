# Iterators is used for iterations 
nums = [7, 8, 9, 5]

print(nums[0])
for i in nums:
    print(i)
    # Behind the scene of for loop, what works is Iterator 

it = iter(nums) # iter() function converts list to iterator
# Iterator will not give you all the values, it will give you 1 value at a time 
print(it) 
# It's printing the object of iterator, we don't want it, we want values right
# If you want values, you need to use __next__() in-built method, it will give you 1st value
print("Running __next__() method")
print(it.__next__()) # when you say next for 1st time, it gives 7
print(it.__next__()) # when you say next again it'll give you 8
# Behing the scene, when you say iterator, iterator have multiple values, so you'll say hey 
# iterator i'm calling your method which is __next__(), in this next it'll pick up 1 value maybe
# tehre's a loop there which will give you 1st value which is 7 in this case. Again when you call
# next it knows last value of i, which means it'll preserve the state of the last value, so it'll 
# give you the next value & that's the beauty of our iterator 
# When you call the functions again, it will preserve the old value 


# We've 1 more way of fetching the next value 
# We can use next() function in which you pass the iterator
print("Running next() function")
print(next(it))
# So, after printing this, again you can use a loop here 
print("Running loop")
for i in nums:
    print(i)


# What if you want to create your own objects because the objects which are there here are 
# in-built objects (list is in-built) ?
# What if you want to create your own iterator ?
# Because if you say integers it is having in-built function __next__(), what if you want to 
# create your own ?





# CREATING MY OWN CLASS 
# The moment you say you need your own object, you need your own class 
# What i want here is i want to print the top 10 values, not all, one by one 
print("Creating my own class")
class TopTen:
    def __init__(self):
        self.num = 1 # I want to start my counter variable from 1

    # Now when you say ypou want to create your own iterator, you need 2 important methods 
    # One is iter() method, it will give the object of iterator & the next method is next()
    # which will give you the next value or next object 
    def __iter__(self):
        return self
    
    # BEFORE TELLING TO STOP AT 10
    # def __next__(self): # it will give you teh next value
    #     # I want the next value of num 
    #     val = self.num
    #     self.num += 1 # incrementing the iterator
    #     return val # Not num bcoz it is incremented


    # TELLING TO STOP AT 10
    # def __next__(self):
    #     if(self.num <= 10):
    #         val = self.num
    #         self.num += 1
    #         return val
        
    # RAISING AN EXCEPTION
    def __next__(self):
        if(self.num <= 10):
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

# So, now this TopTen is your iterator 

values = TopTen()
# for i in values:
#     print(i) 
# Above loop when runned with before telling to stop at 10 gives infinite values instead of 10
# When runned with telling 10 gives infinite values as 'None' (we're getting top 10 values but
# after that the loop is still running, we don't want that we want to stop the loop), so to
# stop a loop we're gonna write a else condition in which you'll simply raise an exception bcoz
# only way to stop for loop is to raise the exception, there's no other way & it handles that 
# exception internally, so for loop has that power
# Now, when runned with loop after raising exception, it prints all top 10 values 

# print(values.__next__())
# print(values.__next__())
# __next__() method is working but then what's wrong with loop, the problem is loop will go from
# start to end & we're assuming the end to be 10 but no where we've mentioned that we need to 
# stop at 10, we need to do that!



# So, this is our own iterator & the only way to get iterator is using those 2 beautiful functions
# next and iter 

# for i in values:
#     print(i)
# print(next(values)) 
# It won't print this now as 10 values are reached, so it stops the iteration



print(next(values)) 
for i in values:
    print(i)
# This prints 10 values exact, '1' is printed a single time 
# That's the power of iterator, so once you got the value of that 'i'  here in next(values), 
# it will not repeat here in for loop 