def add():
    print("result 1 is ",__name__)
    # On running Cal3, its prints result 1 is __main__, that means this is your standalone code
    # The moment you use Calc as a module in some other code, then it prints resul 1 is Calc3
    # It's because the __name__ now is printing the (module_name)
    # That's the importance of this __name__

def sub():
    print("result 2 is ")

def main():
    print("In Calc3 main")
    add()
    sub()

# main()


# HOW DO YOU KNOW THAT THIS IS TEH CODE I'M RUNNING 
# Whenever you run a code & whenever you execute a code, there's a variable called as __name__, which 
# will hold the name 
# So, if this is the code which i'm running at start, the __name__ variable will have __main__ as value

# If this is the file which i'm running, the __name__ variable will have __main__ as a value
# Otherwise, the __name__ variable will have the module name 

if(__name__ == "__main__"):
    main()
# Now, you're saying if the __name__ is __main__, then only call main(), otherwise other codes will
# use this as a module