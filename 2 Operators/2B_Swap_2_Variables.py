# CASE-1 -> SWAP 2 VARIABLES USING 3RD VARIABLE
a = 5
b = 6
print("Running Case-1")
print("Before swapping values of a & b are ",a,"and",b,"respectively")

temp  = a # takes exact 3 bits (needed to represent 5 & 6 in binary format)
a = b
b = temp

print("After swapping values of a & b are ",a,"and",b,"respectively")


# CASE-2 -> SWAP 2 VARIABLES WITHOUT USING 3RD VARIABLE
a = 5
b = 6
print("Running Case-2")
print("Before swapping values of a & b are ", a, "and", b, "respectively")

a = a + b # takes 4 bits, wastes 1 extra bit
b = a - b
a = a - b

print("After swapping values of a & b are ", a, "and", b, "respectively")


# CASE-3 -> SWAP 2 VARIABLES WITHOUT USING XOR
a = 5
b = 6
print("Running Case-3")
print("Before swapping values of a & b are ", a, "and", b, "respectively")

a = a ^ b  # doesn't wastes extra bits
b = a ^ b
a = a ^ b

print("After swapping values of a & b are ", a, "and", b, "respectively")


# CASE-4 -> ANOTHER WAY
a = 5
b = 6
print("Running Case-4")
print("Before swapping values of a & b are ", a, "and", b, "respectively")

a,b = b,a
# WORKING :
# Your right side is solved 1st, so system sends values of b and a to the stack & then it reverses by a 
# concept of ROT_TWO() which swaps the 2 topmost stack items
# a = b & b = a if written in 2 different lines won't work same as above

print("After swapping values of a & b are ", a, "and", b, "respectively")
