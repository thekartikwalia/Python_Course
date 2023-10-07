# pass -> Print all numbers 1-20 but don't print those values which are odd numbers
# Imagine a scenario where you're checking for odd value
# You cannot check for even value, in that case we wanna print i in else part
# But u can't put an impty if block
# So, in that case you say hey i don't have any code here (This is done by PASS)
for i in range(1, 21):
    if(i % 2 != 0):
        pass # pass simply means there's no code, so ignore it 
    else:
        print(i)


print("Bye!")
