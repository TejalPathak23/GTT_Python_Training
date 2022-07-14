# List

list = ['apple', 'banana', 'cheery ', 'mango']
print(list[0])
print(list[1])
print(list[-1])
print(list[2])
print(list[3])
list[3] = "chikoo"
print(list[3])

# o/p :
# apple
# banana
# mango
# cheery
# mango
# chikoo
# PS F:\Coding Practise\GTT Python Training>

list.append("Sitafal")
print(list)

# o/p :
# ['apple', 'banana', 'cheery ', 'chikoo', 'Sitafal']
# PS F:\Coding Practise\GTT Python Training>


print("")
a = ['fruit', 'tree']
list.append(a)
print(list)

# o/p :
# ['apple', 'banana', 'cheery ', 'chikoo', 'Sitafal', ['fruit', 'tree']]
# PS F:\Coding Practise\GTT Python Training>

# Remove elements from the list

print("---------")
list.remove('apple')
print(list)
list.pop()
print(list)
list.clear()
print(list)

# o/p :
# ['banana', 'cheery ', 'chikoo', 'Sitafal', ['fruit', 'tree']]
# ['banana', 'cheery ', 'chikoo', 'Sitafal']
# []

# Diffrence between append and extend
print("------------------")
list = ['apple', 'banana', 'cheery ', 'mango']
print(list)
list.append('tejal')
print(list)
list.extend(['sejal, arya'])
print(list)
print(list.reverse())
print(list)

# o/p :
# ------------------
# ['apple', 'banana', 'cheery ', 'mango']
# ['apple', 'banana', 'cheery ', 'mango', 'tejal']
# ['apple', 'banana', 'cheery ', 'mango', 'tejal', 'sejal, arya']
# None
# ['sejal, arya', 'tejal', 'mango', 'cheery ', 'banana', 'apple']
# PS F:\Coding Practise\GTT Python Training>
