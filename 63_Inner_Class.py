class Student: # Outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() # Creating an instance of Laptop class
        # If you want to create object of laptop, we should be creating it inside the outer class
        # So, you can see that in constructor itself we can define a variable  
        # So, int he outer class we defined a variable lap & you can define the object 
        # So, whenever you want to use a laptop, you've to say student_object.lap

    def show(self):
        print(self.name,self.rollno)
        # We also want to print Laptop details as well along with student details
        self.lap.show()

    class Laptop: # Inner class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self): # This show() is different from the show() of class Student
            print(self.brand,self.cpu,self.ram)
            
    


# 1 way of saving laptop specs in class is like uh increase the nmber of arguments of class 
# s1 = Student('Kartik',2,'hp','i5',8)
s1 = Student('Kartik',2)
s2 = Student('Kanika',3)
# Other way is to create a laptop class inside the Student class

print(s1.name, s1.rollno)
# But this doesn't look good, better approach would be as below
print("Running show of class Student")
s1.show()

print("Brand: ",s1.lap.brand)
# You can't simply say lap.brand() because the lap is inside a Student class 
# What if you want to create another object of it, so you can simply say
# For every object yoy're gonna get different laptops 
lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))
# Since id's are different, we got 2 different objects here 

# Here, we've Laptop as inner class of class Student 
# You could've used 2 different classes as well
# But when you know this class Laptop wll be used only for Student, nothing else, then you don't have to create 
# a separate file for that, you can do it in student class itself

# Can we create object of Laptop outside the Student class directly 
# You can't directly acces Laptop because Laptop class belongs toa student class 
lap3 = Student.Laptop()

# POINTS TO REMEMBER:
# You can create object of inner class inside the outer class 
# OR
# You can create object of inner class outside the outer class, provided you use outer class name to call it


