# print("Hello")
# print("Welcome user")
# ABOVE CODE WAS BEFORE DEFINING FUNCTION 


# I want to print this only when the demo2 is the first file


# DEFINING FUNCTION SO AS TO AVOID PRINTING BOTH STATEMENTS OF DEMO2 WHEN IMPORTED IN CALC2
def main():
    print("Hello")
    print("Welcome user")

# main()

# I want to call main only when demo2 is my first code 
if (__name__ == '__main__'):
    main()


# So, if you want to start a code & if this is the first thing you want to show to the user because this 
# is the start of the code & you want to call it, that's where you use this thing