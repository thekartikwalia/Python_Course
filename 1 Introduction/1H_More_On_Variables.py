a = 10
b = a 
# id() gives address of variable 
print(id(a))
print(id(b))
# In python, when you create multiple variables & they have same data, both will point to the same 
# blocks & won't be creating mutiple boxes for each variable. Thatswhy Python is more memory efficient
print(id(10))
# Address is not based on the 'variable name', it's based on the block itself
# Thatswhy id of a, b & 10 is same 


# Whenever you've a data in your memory which is not being used or which is not ttagged by any variable,
# it will be garbage collected later


# When you talk about variable it means you can change the Value
# But when you say about Constants, it means you can't change the value (soemthing like immutable)

# type() tells us Type of variable 
pi = 3.14
print(type(pi))