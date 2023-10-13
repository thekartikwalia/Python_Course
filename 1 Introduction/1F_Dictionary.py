# Dictionary is used to create value with a key
# Key should be unique & immutable type

# SYNTAX FOR DECLARING DICTIONARY
data = { 1:'Navin', 2:'Kiran', 4:'Harsh'}
print(data)
print(data[4])
# data[3] -> give error bcoz no key with 3 exist 
data.get(4)
data.get(3) # -> gives no error 
print(data.get(3)) # -> prints none
print(data.get(1, "not found")) # If value of 1 exists, print 1
print(data.get(3, "not found")) # If value of 3 does not exists, print 'not found'

# CREATING DICITONARY WITH HELP OF LISTS
keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
data = dict(zip(keys, values)) # zip -> zips keys & values & dict -> converts zip to dictionary
print(data)
data['Monika']= 'CS' # Appends the key & value at end of list data
print(data)
del data['Harsh'] # Deletes the data with key: Harsh
print(data)


# DICTIONARY INSIDE DICTIONARY & LIST INSIDE DICTONARY
prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}
print(prog['Python'])
print(prog['Python'][1]) # Python: has value as list, so indexing can be done
print(prog['Java'])
print(prog['Java']['JEE']) # Java: has value as dictionary, so value can be accessed through keys