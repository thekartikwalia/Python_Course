# Creating a analogy to candy vending machine

# break -> If user wants more candies than we've, then we give avaailabel candies & then, print we're 
# out of stock
av = 10 # av stands for available candies
x = int(input("How many candies you want?"))
i=1
while(i<=x):
    if(i>10):
        print("Out of stock!")
        break # Takes us out of while loop (Allows us to jump out of the block)
    print("Candy")
    i+=1

print("Bye!")