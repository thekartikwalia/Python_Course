# 6 WAYS OF CREATING ARRAYS IN NUMPY:
# 1. array()
# 2. linspace()
    # Takes 3 parameters (start, stop, step)
    # Here stop in included unlike range()
    # Step means number of parts you want to go for, it will break range into these number of parts
    # If you don't specify step, by default it is taken to be 50
# 3. logspace()
    # Just like linespace(), in logspace() also you breakdown into number of parts
    # But in linspace() the gap between 2 elements is fixed, that's not the case with log space
    # In logspace(), spacing between 2 numbers will be dependent on the log of it 
    # All the values, the difference between different values is of log
    # Values are differentiated with the help of log value
# 4. arange()
    # Takes 3 parameters (first element, last element, steps)
    # Here step represents number of elements to skip
    # Like range() it excludes last element
# 5. zeroes()
    # To create an array of given size, in which all values should be 0 by default 
# 6. ones()
    # To create an array of given size, in which all values should be 1 by default 

from numpy import *


# 1. ARRAY()
arr = array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype) # dtype -> gives datatype of values entered in array (along with it's bits like int64)
arr = array([1, 2, 3, 4, 5.0]) # Now all values have been converted to float datatype
# Since, we're not doing conversion explicitly, so this is Implicit conversion that python itself does
print(arr)
print(arr.dtype)
arr = array([1, 2, 3, 4, 5], float) # This also converts all values to float datatypes
print(arr)


# 2. LINSPACE()
arr = linspace(0,15,16)
# Gives float because range is getting divided into parts which may result in float values
print(arr)
arr = linspace(0, 49) # By default step = 50
print(arr)


# 3. LOGSPACE()
arr = logspace(1, 40, 5)
# It will start from 10^1 to 10^40 & it will get divided into 5 parts 
print(arr) 
print('%.2f' %arr[4]) # After decimal we want to print only 2 digits (4->last part index)


# 4. ARANGE()
arr = arange(1, 15, 1)
print(arr)


# 5. ZEROES()
arr = zeros(5) # 5 represents size
print(arr) # By default, it gives output in float format


# 6. ONES()
arr = ones(5) # 5 represents size
print(arr) # By default, it gives output in float format
# For storing data in specific datatype, mention datatype
arr = ones(5, int)
print(arr)