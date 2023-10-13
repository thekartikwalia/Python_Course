# FOR LOOP WITH LIST
x = ['navin', 62, 2.5]
for i in x:
    print(i)
# Above code can also be written as 
for i in ['navin', 62, 2.5]:
    print(i)


# FOR LOOP WITH STRING
x = 'NAVIN'
for i in x:
    print(i)


# FOR LOOP TO PRINT FIRST 10 WHOLE NUMBERS
for i in range(10):
    print(i)


# FOR LOOP TO PRINT NUMBERS FROM 11-20
for i in range(11,21,1): # 21 gets excluded
    print(i)


# FOR LOOP TO PRINT NUMBERS FROM 20-11
# for i in range(20, 10): # Gives nothing bcoz it always goes in ascending order
for i in range(20, 10, -1): # 10 gets excluded, we've to mention to go in reverse order by writing -1
    print(i)


# FOR LOOP TO PRINT NUMBERS FROM 1-20 excluding numbers divisible by 5
for i in range(1, 21, 1): 
    if(i % 5 != 0): # We can use if statements inside for loop
        print(i)
