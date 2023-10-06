# SYNTAX FOR DECLARING LIST 
nums = [25, 12, 36, 95, 14]
# nums[0] -> 25
# nums[2:] -> 36, 95, 14
# nums[-1] -> 14
# nums[-5] -> 25
names = ['rohan', 'kartik', 'saksham']

# LIST CAN CONTAIN ELEMENTS OF DIFFERENT DATATYPES
values = [9.5, 'navin', 25]

# NESTED LISTS CAN EXIST
mil = [nums, names]
print(mil)

# LISTS ARE MUTABLE
nums.append(45) # Add data 45 at end
print("After appending: ",nums)
nums.insert(2,77) # Insert at 2nd index (3rd position) data 77
print("After inserting: ",nums)
nums.remove(14) # removes 14 
print("After removing: ",nums)
nums.pop(1) # pop(i) removes element at ith index & returns its value
print("After removing 1st indexed element: ",nums)
print(nums.pop()) # pop() removes last element & returns its value
print("After removing last element: ",nums)
del nums[2:] # removes all values from index 2 (including 2)
print("After removing all elements from index 2: ",nums)
nums.extend([29, 12, 14, 36]) # Add all these elements at end of nums
print("After adding all elements: ",nums)
print("Min value in nums: ",min(nums)) # prints minimum value
print("Max value in nums: ",max(nums)) # prints maximum value
print("Sum value in nums: ",sum(nums)) # prints sum of all elements
nums.sort() # sort nums in accending order
print("After sorting: ",nums)