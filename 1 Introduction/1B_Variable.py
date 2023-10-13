# _ represents the output of the previous operation
# >>> x + 10
# 19
# >>> _ + 10
# 29

# INDEXING
name = 'youtube'
# left to right -> 0 to 6
# right to left -> -1 to -7
name[0:2]   # -> 'yo'   # 0 means indexing & 2 means position of character
name[1:4]   # -> 'out'
name[1:]    # -> 'outube'
name[:4]    # -> 'yout'
name[3:10]  # -> 'tube'
name[0:3] = 'my'    #  -> throws error because string doesn't support item assignment
len(name)   # -> prints 7


# STRING IN PYTHON IS IMMUTABLE 
