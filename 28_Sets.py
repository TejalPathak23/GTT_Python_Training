# Unordered collection of unique items
# dosen't have any index/indices
# Elimination of duplicates

a = {1, 2, 3, 4, 8, 7, 6, 5, 1, 2, 5, 4, 6}
print("Output :", a)

b = {'Tejal', 23, 100.00, 23}
print("Output :", b)

# o/p :
# Output : {1, 2, 3, 4, 5, 6, 7, 8}
# Output : {100.0, 'Tejal', 23}
# PS F:\Coding Practise\GTT Python Training>

print(a.add(10))
print(b.update('Tejal', 'march'))
print(a)
print(b)

# o/p :
# {1, 2, 3, 4, 5, 6, 7, 8, 10}
# {'e', 'c', 100.0, 'm', 'h', 'r', 'l', 'Tejal', 'T', 23, 'j', 'a'}
# PS F:\Coding Practise\GTT Python Training>

print("")
print(a)
print("Popped Element is :", a.pop())
print(a)

# o/p :
# {1, 2, 3, 4, 5, 6, 7, 8, 10}
# Popped Element is : 1
# {2, 3, 4, 5, 6, 7, 8, 10}
# PS F:\Coding Practise\GTT Python Training>
print("")
print(a)
print("Cleared Element is :", a.clear())

# Set Operations
print("")
a = {1, 2, 3, 4, 8, 7, 6, 5, 1, 2, 5, 4, 6}
b = {'Tejal', 23, 100.00, 23}
c = a.union(b)
print('Union is :', c)
print('Intersection is : ', a.intersection(b))
print('Diffrence  is : ', a.difference(b))

# o/p :
# Union is : {1, 2, 3, 4, 5, 6, 7, 8, 100.0, 'Tejal', 23}
# Intersection is :  set()
# Diffrence  is :  {1, 2, 3, 4, 5, 6, 7, 8}
# PS F:\Coding Practise\GTT Python Training> 