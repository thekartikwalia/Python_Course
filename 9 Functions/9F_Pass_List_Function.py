# Create a function which takes list as input and returns number of even & odd numbers in list 

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if(i % 2 == 0):
            even+=1
        else:
            odd+=1
    return even, odd


lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]

even, odd = count(lst)
print("No. of even numbers",even)
print("No. of odd numbers",odd)

# We can print above in better format using format() function 
# format() -> replaces {} with values
print("Even : {} and Odd : {}".format(even,odd))