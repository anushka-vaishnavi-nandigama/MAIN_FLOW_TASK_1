lst = []
# Creating a list
print("This empty list is: ", lst)
print()

lst = [1, 2, 3, 4, 5]
# Creating a list with elements inside it
print("The list is: ", lst)
print()

lst.append(6)
lst.append(7)
# Adding elements to the list
print("The updated list after adding elements is: ", lst)
print()

lst = []
print("Enter the number of elements you need in the list:")
n = int(input())
print("Enter the elements:")
for i in range(n):
    lst.append(int(input()))
# User input
print("The lst after user inputs is: ", lst)
print()

lst.remove(2)
# Removing element in the list
print("The list after removing an element is: ", lst)
print()

lst[2] = 14
# Updating elements in the list
print("The list after updating an element is: ", lst)
print()

lst.extend([16, 17, 18])
# Extending the elements in the list
print("The list after extending is: ", lst)
print()

lst.sort()
# Sorting the elements in the list
print("The sorted list is: ", lst)
print()

lst.reverse()
# Reversing the elements in the list
print("The reversed list is: ", lst)
print()

print("The count of 17 in list is: ", lst.count(17))
# Counting the elements in the list
print()

# Searching the elements in the list
if 14 in lst:
    print("Element found!")
else:
    print("Element not found.")
print()

lst.clear()
# Clearing the elements in the list
print("The list after clearing is: ", lst)
