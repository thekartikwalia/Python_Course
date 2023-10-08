# Factorial of n = n! = 1x2x3x4 ...(till n)

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
        i+=1
    return f


x = 4
result = fact(x)
print(result)
