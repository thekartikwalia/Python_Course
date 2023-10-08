from numpy import *

arr1 = array([[1, 2, 3, 6],[4, 5, 6, 7]])
print(arr1)

# To actually work with matrix, we've to convert 2D-array into matrix format
# We can do this by using matrix() function
m = matrix(arr1)
print(m) # Output loooks same but with this 'm' we can peform more operations which we do in matrices

# If you don't have 2D-array, you've string with you, in that case also you can create matrix
m = matrix('1 2 3 6; 4 5 6 7') # ; -> used to differentiate between 2 rows
print(m)
# We don't need a separate array to save the value

# If you want to create multiple rows, i mean, 4 rows & 2 columns
# You can give semicolon after every 2 values 
m = matrix('1 2; 3 6; 4 5; 6 7')
print(m)

# I will make it now as 3 rows & 3 columns
m = matrix('1 2 3; 6 4 5; 1 6 7')
print(m)


# We want to print all diagonal elements only
print("Diagonal Elements",diagonal(m)) # diagonal() -> prints diagonal elments of a matrix

# We can also print minimum & maximum elements of matrix
print("Minimum",m.min())
print("Maximum",m.max())