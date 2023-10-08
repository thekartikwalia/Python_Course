# WE HAVE 2 METHODS FOR PASSING ARGUMENTS IN A FUNCTION CALL:
# 1. Pass by value
    # Whenever you're calling a function by passing a variable value, it'll pass as value not variable
    # Variable doesn't bother about changes in it coz we passed value not the variable 
# 2. Pass by reference
    # Whenever you're calling a function by passing address of a variable
    # Variable will get affected because we're making change directly at address of variable

# BUT IN PYTHON WE'VE NEITHER PASS BY VALUE NOR PASS BY REFERENCE


def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x",x)
a = 10
print(id(a))
update(a)
print("a",a)
# id of a & x before updating x is same, both a & x points to same object, so this isn't pass by value
# even on changing x, it doesn't effects value of a, so this isn't pass by reference also
# Hence, this is none of them neither pass by value nore pass by Reference
# The moment we update value of x, x will point to new address 



# When you change value of x, it'll create a new memory, it is bcoz int, str etc. they're immutable
# What if you use something which is mutable like list
def update(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print("lst",lst)
lst = [10, 20, 30]
print(id(lst))
update(lst)
print("lst",lst)
# It's also updating the original list bcoz the id is same 
# Since, we have the same id here, so it will not change, it is mutable