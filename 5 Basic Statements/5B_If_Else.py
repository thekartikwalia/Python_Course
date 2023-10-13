# if is a suite (or block) where you can write multiple statements
# All statements with indentation belong to that suite


# SYTAX FOR IF STATEMENT
# if True:    # Execute below block of code
#     print("I'm right")
# if False:    # Don't execute below block of code
#     print("I'm right")

x = 8
r = x % 2
if(r==0):
    print("Even")
if(r==1):
    print("Odd")

# BETTER REPLACEMENT OF ABOVE CODE 
x = 8
r = x % 2
if (r == 0):
    print("Even")
    if(x > 5):  # if inside if can be present -> called "NESTED IF"
        print("Greater than 5")
    else:
        print("Lesser than 5")
else: # There's no need of checking r==1 bcoz by default if it's not 0, it wou,d be 1
    print("Odd")

