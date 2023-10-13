num = 7
for i in range(2,num):
    if(num % i == 0):
        print("Not Prime")
        break
else:
    print("Prime")


# More efficient way of doing this would be by checking divisibility only till half rather than till n-1
num = 11
for i in range(2, num//2):
    if (num % i == 0):
        print("Not Prime")
        break
else:
    print("Prime")
