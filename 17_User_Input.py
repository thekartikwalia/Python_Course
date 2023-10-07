x = input("Enter 1st number ")
y = input("Enter 2nd number ")
# By default input() takes value in str format, so if x=1 n y=2, it will give 12
z = x + y
print("Sum is",z)

# CORRECTED CODE
x = input("Enter 1st number ")
a = int(x)
y = input("Enter 2nd number ")
b = int(y)
z = a + b
print("Sum is",z)

# BETTER APPROACH FOR CORRECTED CODE 
x = int(input("Enter 1st number "))
y = int(input("Enter 2nd number "))
z = a + b
print("Sum is",z)

# TAKING INPUT IN CHARACTER FORMAT (EVEN THOUGH CHAR ISN'T PRESENT IN PYTHON) 
ch = input("Enter a char ")
print(ch) # If entered pqr, it will print it as it is
# We can use indexing to convert str into char
print(ch[0]) # If entered pqr, it will print p 
# (But it saved ptr as a whole to ch)
ch2 = input("Enter a char ")[0]
print(ch2) # If entered pqr, it will print p 
# (But it didn't saved ptr as a whole, rather it assigned 0th index of input to ch2)

# We can't directly pass expression like 2+4-6 as input to int it will assign it 1st number i.e. 2
# So, eval() is used to take expression as an input from user
result = eval(input("Enter an expression: "))
print(result)
 
# argv is a special keyword for Argument Values
# It helps us to take input from command line on basis of indexing
# argv belong to module sys, so need to import that also
import sys
# python [file_name].py 6 2
# Here [file_name] represents index 2, 6 represents index 1 & 2 represents index 2
# So in this case, we should take input as 
x = int(sys.argv[1]) # Not 0 bcoz it was for [file_name]
y = int(sys.argv[2]) 
z = x + y
print(z)