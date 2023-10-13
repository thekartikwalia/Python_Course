from numpy import *


# 2-DIMENSIONAL ARRAYS 
arr1 = array([[1, 2, 3, 6, 2, 9],[4, 5, 6, 7, 5, 3]])
print(arr1)
print(arr1.ndim) # ndim -> gives us dimension of array
print(arr1.shape) # shape -> gives tuple (r, c), where r->rows & c->columns 
print(arr1.size) # size -> gives us total number of elements

# CONVERT 2D-ARRAY INTO 1D-ARRAY
arr2 = arr1.flatten() # flatten() -> flattens the 2D-array into 1D-array
print(arr2)


# CONVERT INTO MULTI-DIMESNIONAL ARRAY (1D to 2D)
arr3 = arr2.reshape(3, 4) # (rows, columns)
print("2D-Array\n",arr3)
# 1D to 3D
arr3 = arr2.reshape(2, 2, 3) # Create 3D-array (Number of 2D-arrays, rows, columns)
# 3D-array will have 2 2D-array, each 2D-array will have 2 1D-array, each 1D-array will have 3 values
print("3D-Array\n",arr3)