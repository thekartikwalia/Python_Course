
class A:

    def show(self):
        print("In A show!")

# What if you create another class B ?
# Now imagine this class A is a parent & class B is a child 
class B(A): # B inherits A
    # pass
    # The moment you run this code after uncommenting "pass" it'll first search for the method show() inside B
    # Now, since we don't have that it will go to A to search it 
    # That's how it works!
    def show(self):
        print("In B show!") 
    # The moment you create a show() method inside class B, it overrides the show() method of class A
    # When we weren't having show() inside class B, it was going to class A 
    # Now since we've show() method inside class B, it'll print the show() of class B

a1 = A()
a1.show()

b1 = B()
b1.show()

# POINT TO REMEMBER :
# Whenever you call show() it will call the show() method of the Sub class, if you've it!