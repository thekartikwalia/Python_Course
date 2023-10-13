from numpy import *


# ADD VALUE TO EACH ELEMENT OF ARRAY WITHOUT USING LOOP 
arr = array([1, 2, 3, 4, 5])
arr = arr + 5
print(arr)


# ADD 2 DIFFERENT ARRAYS -> Also called as "VECTORIZED OPERATION"
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])
arr3 = arr1 + arr2 # add 2 arrays byadding correspodning elements of both arrays
print(arr3)


# YOU CAN FIND SINE, LOGARITHM, SQUARE ROOT, SUM, MINIMUM, MAXIMUM OF EACH ELEMENT OF ARRAY
print(sin(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
# Even you can find the unique element, sort the array
 

# YOU CAN EVEN CONCATENATE 2 ARRAYS 
print(concatenate([arr1,arr2]))