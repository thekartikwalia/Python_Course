# continue -> Print numbers from 1-20 but don't print numbers which are divisible by 3 or 5
for i in range(1,21):
    if(i % 3 == 0 or i % 5 == 0):
        continue # Skips remaining code inside loop for this iteration & moves onto next iteration
        # It will not jump out of the loop 
    print(i)


print("Bye!")