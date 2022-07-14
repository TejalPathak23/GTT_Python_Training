# Pyhton program to change first and last elements in the list

list = [1, 2, 3, 4, 5]
size=5
print(list)
temp = list[0]
list[0] = list[size - 1]
list[size - 1] = temp
print(list)

# o/p :
# [1, 2, 3, 4, 5]
# [5, 2, 3, 4, 1]
# PS F:\Coding Practise\GTT Python Training> 
