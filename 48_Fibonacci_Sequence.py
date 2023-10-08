# Fibonacci Sequence : Sequence whose next term equals sum of previous 2 terms
# 0 1 1 2 3 5 8 13 21 ...

def fib(n):
    a = 0
    b = 1
    if(n<=0):
        print("Invalid Input!")
    else:
        if(n==1):
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
                c = a+b
                print(c)
                a = b 
                b = c
fib(1)

# We want take if user enters a number say 100, then it should print last fibonacci term less than 100
def fib_lastterm(n):
    a = 0 
    b = 1
    while (True):
        c = a+b
        a = b 
        b = c
        if(c > n ):
            print("Last term less than or equal to {} is {}".format(n,a)) 
            break

fib_lastterm(100)