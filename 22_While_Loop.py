# SYNTAX OF WHILE LOOP :
# while ([condition]):
#     Suite of statements

i = 1 # Initialization
while(i<=5): # Condition
    print("Kartik", i)
    i=i+1 # Increment

# We can also use loop by Decrementing
i = 1
j = 1
while(i<=5):
    print("Kartik") # By default after print, cursor goes to next line
    while(j<=4): # while loop inside while loop can be present -> called "NESTED WHILE LOOP" 
        print("Rocks!")
        j=j+1
    i=i+1
# In case of nesting, firstly inner loop in completed, then control goes back again to outer loop


# Now we want to print Rocks on same line
i = 1
j = 1
while(i<=5):
    print("Kartik", end="") # end="" ensures that it shouldn't enter next line after print
    while(j<=4):
        print("Rocks!", end="")
        j=j+1
    i=i+1


# We don't want all Kartik on same line
i = 1
j = 1
while(i<=5):
    print("Kartik", end="") 
    while(j<=4):
        print("Rocks!", end="")
        j=j+1
    i=i+1
    print() # Enters new line each time outer loop is finished


# We want Rocks to appear 4 times with each Kartik
i = 1
while(i<=5):
    print("Kartik ", end="") 
    j=1 # initialize j as 1 each time inner loop starts
    while(j<=4):
        print("Rocks! ", end="")
        j=j+1
    i=i+1
    print()
