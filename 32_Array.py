# In an array, we do have all the values of the same type
# Arrays are similar to list, but only difference is that you need to have all elements of same type 
# Arrays in python don't have specific size which means you can expand/shrink it
# So, arrays are quiet flexible to work with

# We need to import module array to use array() function
from array import * # * means you want to import all the functions
# SYNTAX FOR ARRAY DECLARATION
# array('TypeCode',[values])
vals = array('i',[5, 9, -8, 4, 2])
print(vals)
# buffer_info() gives tuple of (Address, Size) of array
print(vals.buffer_info())
# typecode prints type of code you're working with'
print(vals.typecode)
# reverse() it reverses the array
vals.reverse()
print(vals)

# INDEXING CAN BE USED TO PRINT VALUES ONE-BY-ONE RATHER THAN PRINTING ALL AT SAME TIME
print(vals[0])
for i in range(5):
    print(vals[i])


# MORE DYNAMIC FORM OF ABOVE CODE
# using len() whih gives length 
for i in range(len(vals)):
    print(vals[i])

# ABOVE CODE CAN ALSO BE WRITTEN AS
for i in vals:
    print(i)

# WE CAN ALSO WORK WITH CHARACTERS
vals = array('u',['a','e','i'])
for i in vals:
    print(i)

# CREATING A NEW ARRAY WITH THE SAME VALUES
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode,(a for a in vals))
# vals.typecode -> take typecode from another array 'vals'
# a for a in vals -> copy each element from another array 'vals'
for i in newArr:
    print(i)

# INSTEAD OF ASSIGNING SAME VALUE WHAT IF WE WANT TO ASSIGN SQUARE OF IT IN NEW ARRAY
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode,(a*a for a in vals))
for i in newArr:
    print(i)

# WE CAN USE WHILE LOOP ALSO TO PRINT VALUES
i = 0
while(i < len(newArr)):
    print(newArr[i])
    i+=1

    