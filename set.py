a = {1, 2, 3, 4, 5}
# Creating a set
print(a)
print()

a.add(6)
# Adding elements into a set
print(a)
print()

a.remove(5)
# Removing element from the set
print(a)
print()

a.discard(1)
# Updating the elements in a set
print(a)
print()

print("Set before popping an element:", a)
# pop() function
deel = a.pop()
print("Element popped from the set:", deel)
print("Set after popping an element:", a)
print()

a.clear()
# Clearing the set
print("Set after clearing:", a)
print()

a = {1, 2, 3, 4}
b = {2, 3, 8, 9}
# Set operations
print("Union of sets a and b:", a.union(b))
print()
print("Intersection of sets a and b:", a.intersection(b))
print()
print("Difference of sets a and b:", a.difference(b))
print()