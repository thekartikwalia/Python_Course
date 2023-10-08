nums = [12, 16, 18, 21, 26]

# Check if list has number divisible by 5, if u found such a number, then print it
for num in nums:
    if(num % 5 == 0):
        print(num)


# We only want to print only 1st number which is divisible by 5
for num in nums:
    if (num % 5 == 0):
        print(num)
        break
    else : # This 'else' is for the 'if', thatswhy it prints "Not found!" 5 times
        print("Not found!")


for num in nums:
    if (num % 5 == 0):
        print(num)
        break # break is compulsary here
else : # This 'else' is for the 'for', thatswhy it prints "Not found!" 1 time -> for else
    # for else used in cases where loop is never breaked
    print("Not found!")


nums = [10, 16, 18, 21, 26]
for num in nums:
    if (num % 5 == 0):
        print(num)
        # break # On removing break, it will print not found even after finding a number
else : # This 'else' is for the 'for', thatswhy it prints "Not found!" 1 time
    print("Not found!")