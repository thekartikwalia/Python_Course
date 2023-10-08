# COPYING IS OF 2 TYPES:
# 1. Aliasing -> arr1 = arr2
    # Means you still have one memory location, jsut 2 variables pointing at same location
# 2. Shallow Copy -> arr1 = arr2.view()
    # Means it will copy the elements but then, both the array are still dependent on each other
    # On changing value of one will automatically change value of other
# 3. Deep Copy -> arr1 = arr2.copy()
    # Means there are 2 different arrays and they're not linked with each other in any way


from numpy import *

arr1 = array([2, 6, 8, 1, 3])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
# Both arrays have the same id i.e. both variables (arr1 & arr2) are pointing to same array
# This is also called as "Aliasing" because you're creating new alias for the same array
# So, you can modify using arr1 or arr2 it's your choice


# IF YOU WANT TO CREATE 2 DIFFERENT ARRAYS (NOT THE SAME MEMORY LOCATION ONLY SAME DATA)
# view() is a function which will help you to create a new array at different memory location
arr3 = arr1.view()
arr1[1] = 7
print(arr1)
print(arr3)
print(id(arr3))
# view() function gives a shallow copy 



# FOR DEEP COPY, WE USE COPY() FUNCTION
arr3 = arr1.copy()
arr1[0] = 3
print(arr1)
print(arr3)
print(id(arr3))
