# Object takes Heap Memory 
class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 28
        # Now, both the objects will have the same values 

    def update(self):
        self.age = 30

    def compare(self,other):
        if (self.age == other.age):
            return True 
        else:
            return False

c1 = Computer()
c2 = Computer()


print("Before modifying the age of object c1")
if c1.compare(c2):  # c1 becomes self (bcoz c1 is calling it) & c2 becomes other
    print("They're same!")
else:
    print("They are different!")

print(id(c1))
print(id(c2))
# Since, both id's are different 
# So, Every time you create an object it is allocated to a new space 

# SIZE OF OBJECT 
# - Depends upon number of variables & size of each variable 

# WHO ALLOCATES SIZE TO OBJECT 
# - Constructor 
    # Here, Compute() is your Constructor
    # So, whenever you'll write a constructor, it will call the __init__ method for you
    # Obviously you don't have to call it explicitly, it'll be called internally

# If i want to change the value of 1 object, the way you can do that is 
# If you want to assign your own values, you've 2 choice here:
# 1. Before printing change the value of c1 
c1.name = 'Rashi'
c1.age = 12

c1.update()
# We can change the value of one object from different objects as ofcourse they've 2 different entities
# So, remember this that we got 2 different objects & both the objects will have different variables 
# You can assign the values there, you can change it, you wish!

print(c1.name)
print(c2.name)


# IMPORTANCE OF SELF
# You've 2 different objects but there is program execution
# So, the moment you say c1.update(), your pointer which is your focus will move towards this update 
# method, so it's executing it. update() will say okay i'm getting called, i belong to a class Computer.
# My job is to change the value of age, but hold on we got 2 objects whose value you want to change.
# Because we're calling update() and we aren't mentioning which object i'm talking about because when 
# you call this update, we've not mentioned whether it is c1 or c2, we've mentioned it by calling it, so 
# we're saying c1.update() but we aren't passing anything in bracket, so when you're calling update(), 
# how your pointer will know which object i'm talking about, is it the c1 age or the c2 age and that's 
# where you need to use self.
# So, this self is a pointer or you can say self is directing to c1 or c2. So we've 2 objects the self 
# will direct either on c1 or c2 based on what you're calling. So, if you're saying c1.update(), then 
# in the bracket it is passing c1, so self will be assigned to c1. 
# So, that's the importance of self, it's very important because it's refering to the object 
# If you've 10 objects, you want to refer to one object, you can use self 
# So self is the current instance you say, at a time you're working with one object


# What if i want to compare 2 objects 
# I want to compare 2 people based on their age
# So, i want to check if both the objects are same, then i'll print same
# But then i don't want to compare the object address, i want to compare their values, i want to compare
# their age, name doesn't matter even if it's different 
# In this case, we can't directly say c1 == c2 because your python don't know how to compare
# So, in this case what you'll do is, you'll use a separate function to do that

print("After modifying the age of object c1")
if c1.compare(c2): # c1 becomes self (bcoz c1 is calling it) & c2 becomes other
    print("They're same!")
else: 
    print("They are different!")

# So, we can compare 2 objects by defining oiur own method which is compare() in this case 
# But remember that compare() method takes 2 parameters 
# compare(who is calling, whom to compare)