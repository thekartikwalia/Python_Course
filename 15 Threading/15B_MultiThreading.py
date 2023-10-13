class Hello:
    def run(Self):
        for i in range(5):
            print("Hello")


class Hi:
    def run(Self):
        for i in range(5):
            print("Hi")


t1 = Hello()
t2 = Hi()

t1.run()
t2.run()
# Let's assume to print all "Hello" it takes 5 secs & to print all "Hi" it takes 5 secs, means in
# total it will take 10 secs & we know that it is using only 1 core, so even if this machine has 
# 10 core CPU it is still using 1 core.
# I want to execute the run of "Hello" and the run of "Hi" simultaneously, is it possible ?
# Can i execute 2 functions at the same time on different cores or maybe in the same core but
# simultaneously, is it possible ?
# By default every execution has 1 thread, so even if you're not creating a thread by urself, 
# you do have 1 thread & that thread is known as a "Main Thread"
# So this execution is done by a Main Thread 
# But i don't want to work with the Main thread, ofcourse we've that but i want to print "Hello"
# and "Hi" but then with help of 2 different threads.
# How will I create 2 different threads ?
# There's one way to have features is Hello has to be a subclass of thread, same goes with Hi
# Now they can run inidividually on 2 different cores 
# When you want to use Thread, you need to import a package called threading
print("After creating threads! (Not the right method)")
from threading import *

class Hello2(Thread):
    def run(Self):
        for i in range(5):
            print("Hello")


class Hi2(Thread):
    def run(Self):
        for i in range(5):
            print("Hi")


t3 = Hello2()
t4 = Hi2()

t3.run()
t4.run()
# EXPECTATION:
# So we've a main thread by default & main thread will execute all the statements 
# The moment you say run it should create 2 different threads which is let's say t3 & t4 and
# t3 will print "Hello" 5 times & t4 will print "Hi" 5 times. And it should be happening 
# simultaneously, so it should give output as Hello Hi, Hello Hi... (5 times)
# REALITY:
# But we're getting same output, they are not runnig in parallel. 
# See the moment you say you want to create 2 different threads, this is not happening here,
# even if you make your class as thread, we're not creating 2 different threads there!
# If you want to create 2 different threads, instead of calling a run method you need to call 
# a start method & that's weird right ?
# We are defining the method name as run & then we're calling start, so behind the scene what's
# happening is when you say t1.start() internally it will call run & the reason why we went for
# this method name as run is bcoz inside Thread class we do have a method called run and if you
# go for any other method it won't work 
# So, you've to make sure instead of run you have to say start, so that it execute 2 different 
# threads


print("After creating threads! (The right method)")
t3.start()
t4.start()
# We got random no of Hello before Hi,then again repeats randomly till 5 of each are printed
# So, something is happening in parallel but not exactly the way we wanted 
# We wanted to have a 1 Hi and then a 1 Hello alternate case 
# So, that means it is happening in parallel but your system is so fast that it is executing them
# at the same point, so there's a collision plus in your system we've a concept of schedulers
# which will give you a specific time to execute & we're expecting it'll print only 1 Hello in 
# that particular time but it so smart it is executing 10 times in that gap, so to increase the 
# gap since it is going very fast i'll make it sleep, i'll make it slow down, the way you do that 
# is by importing a package, so you'll use from time & you'll import special method that is sleep
print("\nAfter using sleep from time package!")
from time import sleep
# So, what i'll do is everytime it prints Hello i'll say Hey sleep for like 1 sec 
class Hello3(Thread):
    def run(Self):
        for i in range(5):
            print("Hello")
            sleep(1) # Sleep for 1 sec after printing "Hello" each time


class Hi3(Thread):
    def run(Self):
        for i in range(5):
            print("Hi")
            sleep(1) # Sleep for 1 sec after printing "Hi" each time


t5 = Hello3()
t6 = Hi3()

t5.run()
sleep(0.2)
t6.run()
# So now what happens is when "Hello" gets printed it'll wait for 1 sec and by the time you can 
# print "Hi" once, so it will go alternate now 
# Still it's not printing the "Hello" & "Hi" alternatively, so what's happening here?
# Now, this is called as Collision, maybe it's happening that 2 threads are coming at same time
# to the CPU, bcoz see we're assuming it will run in parallel but suddenly they're going to the
# CPU at same time after sleeping, so once they wake up they're going to the CPU at same time 

# What i'll do is when you say start, t1.start() & t2.start(), i want to have a gap between them 
# too, so i'll put a gap of like 0.2 secs so that they will not go into collision now
# This is how you can unsink them bcoz initially they were sink & thatswhy they were colliding 
# but now they will not 

# What's happening now is the moment you say t5 & t6 object you got 2 different threads but still 
# they're into main thread, they are not separating. The moment you say start it creates a new 
# thread, so in total we'll be getiing 3 threads (Main, t1 & t2)


t3.join() # At this point main is waiting for t3
t4.join() # Once t1 comes back, it is waiting for t4
# Once both come back it will print bye!


# now let's say i want to print Bye here
print("Bye!")
# Now what you think, where you'll print Bye!, after printing all Hi & Hello it'll print Bye ?
# What u think now will it print Bye at end of Hi Hello or somewhere in between ?
# Here, we see that we got Bye in between, that's wierd, before printing Hi & Hello how can you 
# print "Bye!". The problem is who is responsible to execute this "Bye!", is it t3 thread or t4
# thread ?
# Who is responsible here is the main thread, so after starting t3 and t4, t3 is printing Hello 
# & t4 is printing Hi, Main is doing nothing, thatswhy main says hey my job is done let me print
# Bye!, we don't want that!, we want to print Bye! at the end.
# So we've to ask main thread, Hey main thread wait for t3 & t4 to join, please continue only
# after there joining! So when u say t1.join() & t2.join() at this point you're asking you main 
# thread bcoz all the statements will be executed by the main thread, so at this point main
# thread will say okay you're asking me to wait for t3 i'll do that!