# PATTERN - 1 : # # # #
                # # # #
                # # # #
                # # # #
print("Running Pattern-1")
for i in range(4): # i -> rows
    for j in range(4): # j -> columns
        print("# ", end="")
    print()


# PATTERN - 2 : # 
                # #
                # # #
                # # # #
print("Running Pattern-2")
for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()


# PATTERN - 3 : # # # #
                # # #
                # # 
                # 
print("Running Pattern-3")
for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()