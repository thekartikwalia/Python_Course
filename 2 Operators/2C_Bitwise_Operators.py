# BITWISE OPERATORS :
# 1. Compliment (~) :
#     Also called 'Tilde operator'
#     Gives compliment of binary format of number
# 2. And (&) :
#     Both T, then T
# 3. Or (|) :
#     Both F, then F
# 4. XOR (^)
#     Both different, then T
# 5. Left Shift (<<)
#     Left shift binary format by adding zeroes at right end
# 6. Right Shift (>>)
#     Right shift binary format by adding zeroes at left end

print("~12 =",~12)
# Gives 13 as 12 = 00001100
# ~ 12 = 11110011
# To represent negative number in binary format, we use 2's compliment
# 2's compliment = 1's compliment + 1
# 13 = 00001101
# 1's compliment of 13 = 11110010 
# 2's compliment of 13 = 1 + 11110010 = 11110011 
# so, - 13 = 11110011
# Thatswhy ~12 = 13

print("12 & 13 =",12 & 13)
# Gives 12 
# 12 = 00001100
# 13 = 00001101
# &  = 00001100 = 12
print("12 | 13 =",12 | 13)
# Gives 13 
# 12 = 00001100
# 13 = 00001101
# |  = 00001101 = 13

print("12 ^ 1 =",12 ^ 1)
# Gives 13
# 12 = 00001100
# 1  = 00000001
# ^  = 00001101 = 13

print("10 << 2 =",10 << 2)
# Gives 40
# 10 = 00001010
# << = 00101000 = 40

print("10 >> 2 =",10 >> 2)
# Gives 2
# 10 = 00001010
# >> = 00000010 = 2