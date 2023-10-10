# We've this famous line which is "if there's a bird which looks like a duck, which is walking like a duck, 
# which is quacking like a duck and which is swimming like a duck, that bird  probably is a duck 
# It simply means it doesn't matter if it's duck or not, then what matters is the behaviour of the bird if it
# is matching with duck, then that's a duck

# In the same way, if there's an object IDE & it has a method execute(), that's it.
# We aren't concerned about which class object it is, what we're concerned about is that it should've that 
# method which is execute(). And that is called as "Duck Typing"



x = 5
# In Python, we've a concept of Dynamic Typing which simply means the type you can mention later
# Eg: when you say x=5, they type we're mentioning now is integer

# But what if you say x='Navin', are we changing the type of 'x' here ?
# See that's not the case
# What is happening here is, when you say 5, in you're memory you got a space which is of type integer, when 
# you say 'Navin' in your memory you got a space which is of type string, the 'x' is just a name to it.
# When you say x=5, there's a object of type integer, you're just naming it as 'x'.
# Later when you say you got 'Navin', you got some space in your memory & you're representing that with 'x'
# 'x' is just a name to it, so we don't have specific type to 'x'
# The moment you say type of 'x', you're actually getting the type of '5'
# When you say the type of 'x', you're getting the type of 'Navin'

# The moment you give a variable a name, that's just a name to a memory 
class PyCharm :
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")
        # This IDE does extra stuff 


class Laptop:

    def code(self,ide):
        # In this code, i want to execute my code. So, as a programmer we write code & we compile it , we run 
        # it & we get output at the end, to do that we also need an IDE (Integrated Development Environment)
        # In this case, if u want a code, you need to pass an IDE, so we're expecting in the arguments that 
        # someone will pass an IDE to us 
        ide.execute()
        # The question is IDE is of what type 
        # When you say execute that means there's something which is not there in existing class which you've,
        # that means the type of 'ide' is something very unique, is something which the user is defining
        # That means if you want to create this object 'ide', you need to create your own class 




print("Before changing the ide type")
ide = PyCharm()
# Now, we're gonna call code(), but there's problem, inside code() you need to pass an argument which is of IDE
lap1 = Laptop()
lap1.code(ide)
# To pass ide here, first you need to create an object of IDE 
# So the type of 'ide' here is PyCharm
# But is it fixed ? Can we change the type of IDE later ?
# Let's say we have one more ide, let's say in future i'm creatin my own editor 

# Is IDE type fixed to PyCharm ?
# Not exactly, because this is dynamic typing.
# So, you can replace this IDE type from PyCharm to Editor, provided you've that method which is 'execute'
# It doesn't matter which class object you're passing, what matters is that object should've the execute() 
# method because in ide we're saying execute()

# So now even if change from PyCharm to MyEditor, there's no problem
print("After changing the ide type")
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
