diction = {} 
# Creating a dictionary.
print("The empty dictionary: ",diction)
print()

diction = {'name': 'Anushka', 'age': 20, 'gender': 'Female', 'city': 'Visakhapatnam', 'course': 'B.Tech'} 
# A dictionary has key value pairs. It is usually enclosed in curly braces '{}', and the elements are sepersted by comma','. 
print("The dictionary is: ", diction)
print()

age = diction.get('age')
#  Getting the value of a key
print("The value of age is: ", age)
# Another way of getting the value of a key is
age = diction['age']
print("The value of age is: ", age)
print()

kv = diction.items()
# Getting key-value pairs
print("The key-value pairs are: ", kv)
print()

keys = diction.keys()
# Getting the all keys
print("The keys are: ", keys)
print()

values = diction.values()
# Getting the all values
print("The values are: ", values)
print()

# A dictionary is a mutable datatype. Hence, elements can be added, deleted or altered.
diction['branch'] = 'CSE'
# Adding a new key-value pair.
print("The updated dictionary after adding an element is:", diction)
print()

print("The dictionary before deleting an element is:", diction)
del diction['age']
# Removing a key-value pair.
print("The updated dictionary after deleting an element is:", diction)
# Other methods to remove an element:
diction['age'] = '20'
print("The dictionary before deleting an element is:", diction)
diction.pop('age')
print("The updated dictionary after deleting an element is:", diction)
diction['age'] = '20'
print("The dictionary before after deleting an element is:", diction)
diction.popitem() # Deletes the last element
print("The updated dictionary after deleting an element is:", diction)
print()

diction['city'] = 'Hyderabad'
# Changing the value of a key
print("The updated dictionary after updating an element is:", diction)
print()

#Ways to copy a dictionary:
dictc = diction.copy()
print("The copied dictionary is: ", dictc)
print()

diction.clear()
#Deletes all the elements
print("The updated dictionary after clearing is:", diction)