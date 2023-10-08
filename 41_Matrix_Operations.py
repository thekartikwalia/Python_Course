from numpy import *

m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')

m3 = m1 + m2
print("Addition\n",m3)
m3 = m1 * m2
print("Multiplication\n",m3)


# MANUAL MATRIX MULTIPLICATION 
# Get the dimensions of the matrices
r_m1, c_m1 = m1.shape
r_m2, c_m2 = m2.shape
# Check if the matrices can be multiplied
if(c_m1 != r_m2):
    print("Matrix multiplication isn't possible!")
else:
    # Initialize a result matrix with zeros
    result = zeros((r_m1, c_m2), int)
    # Perform Multiplication
    for i in range(r_m1):
        for j in range(c_m2):
            # Initialize the result element at position (i, j) to zero
            result[i, j] = 0 
            for k in range(c_m1): 
                # Multiply corresponding elements of both, & add to result
                result[i, j] += m1[i, k] * m2[k, j]
    # Print the result matrix
    print("Result matrix:")
    print(result)
