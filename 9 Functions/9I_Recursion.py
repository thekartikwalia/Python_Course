# Recurrsion means you're calling a function from itself
import sys

sys.setrecursionlimit(2000) # setrecursionlimit(n) -> sets recursion limit to n

print(sys.getrecursionlimit()) # getrecursionlimit() -> gives limit of recursion

i = 0
def greet():
    global i # So, that we can use global variable 'i' inside function
    i+=1
    print("Hello ",i)
    greet()

greet()