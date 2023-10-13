# CREATING GENERATOR 
# Here, let me define a function 
# That's right we've to define a function, not the class this time 
# So, we're gonna define a fucntion & it'll return the top 10 values 
def topten():
    # Topten is function which will give you iterator 
    # But hold on a fucntion cannot give you a iterator! 
    # A function has to be something special 
    # So we've to convert this function into a generator 
    # The way you do that is 
    # normally in fucntion we write return, so if u say return 5, so this values will be having 5
    # but if you instead of saying return 5, if you say yield 5, you job is done because yield is
    # special keyword which will make your function as a generator.
    yield 1
    # But now you'll think what's the difference return will give you the value, even yield will 
    # give you the value ?

    yield 2
    yield 3
    yield 4


print("Running topten")
values = topten()

print(values)
# Instead of getting a value 5 we got a obejct of generator & that's the thing you know bcoz
# generator gives you iteraor, so this function is not a normal function, this is a generator 
# bcoz we're using yield 
# if you said return instead of yield, you can expect it to behave normally, it'll return 5
# But yield will be different, yield will also return the value but it'll return in the format
# of a iterator 
# And everyone knows if u want to fetch something for iterator we've to use the next function 

print(values.__next__()) # Run this code and you can see we got 5

# Now you'll think that's fine even return gives the same output, but no there's a difference
# in yield, since it's a generator which will give you iterator, you can write multiple yield
# statements

# Now you can see we go 4 yields which is 1, 2, 3, 4. If you run this code, you'll only get the 
# 1st value bcoz you're saying next only once. So this is same as iterator where you're getting
# multiple values 
# So, you got your own iterator without using next & iter function 
print(values.__next__())
# You can also use loop 
for i in values: # It'll print all the remaining values for you which is 3 & 4
    print(i)

# This is how you can create a generator just by using that 1 keyword which is 'yield' 


# Now, i wanna print top 10 perfect squares 
def toptensquare():
    n = 1
    # Since, we want to print all the perfect squares i've to use a loop 
    # I'll not be using for loop here because indirectly for uses an iterator, let's use while
    while n<=10 : # Bcoz we want to fetch top 10
        # Everytime you find a new value you just have to say yield 
        sq = n*n
        yield sq
        # We're sending the value, so it's almost same as return but then return will terminate 
        # the function and this will not, that's something you need to remember!
        # Now once you say sq you've to say 'n', bcoz you've to also iterate 'n'
        n += 1

print("Running toptensquare")
values2 = toptensquare()
for i in values2:
    print(i)
# yield will give next next value each time 




# This is how we can use generator with the help of yield keyword 