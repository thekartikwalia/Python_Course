from array import *
# Declaring empty array 
arr = array('i',[])
n = int(input("Enter length of array:"))
for i in range(n):
    x = int(input("Enter the next value:"))
    arr.append(x)

print(arr)


# PRINT THE INDEX OF THE SEARCHED ELEMENT
val = int(input("Enter the value for search: "))
k = 0 # For indexing
for e in arr:
    if( e == val):
        print(k)  # If element is found, that's the end
    k+=1


# ABOVE CAN ALSO BE DONE USING FUNCTION 
val = int(input("Enter the value for search: "))
print(arr.index(val))  # index() gives index of value entered
