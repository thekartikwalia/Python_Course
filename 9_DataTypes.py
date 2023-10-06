# DATATYPES :
# 1. None :
#     When you've a variable and that variable is not assigned with any value
# 2. Numeric : int, float, complex, bool
#     In Python, we use a+bj to represent complex (j instead of i)
# 3. List
# 4. Tuple 
# 5. Set 
# 6. String 
# 7. Range 
# 8. Dictionary

# Everyhting from List to Range comes under Sequence

a = 5.6
b = int(a) # Put int value of a in b 
print("b is",b,"and has type",type(b))
k = float(b) # Put float value of b in k
print("k is",k)
c = complex(b,k) # Put b & k in complex form inside c
print("c is",c)

# int(True) = 1
# int(False) = 0

# In python we have String (str), not char as datatype
print("Range is :",range(0,10))
print("List of range (0,10) is :",list(range(0,10)))
print(list(range(2,10,2))) # start:2, end:10, difference:2
# range function generates numbers up to, but not including, the stop value. Thatswhy 10 isn't printed


d = {'navin':'samsung', 'rahul':'Iphone','kiran':'Oneplus'}
print("Keys of Dictionary d are:",d.keys()) # Prints keys of dictionary
print("Values of Dictionary d are:",d.values()) # Prints values of dictionary