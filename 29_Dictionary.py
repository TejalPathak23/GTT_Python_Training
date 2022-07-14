# Key : Value --> Stores data
# Makes data more optimised
# Dictionary in python = dictionary in real world
# Immutable Data Type

# dict = {'Name':'Tejal', 1 : 2}
# print(dict)

# o/p :
# {'Name': 'Tejal', 1: 2}
# PS F:\Coding Practise\GTT Python Training>

# Dictionary with mixed keys
print('')
d = {'Name ': 'Arya', 'No': [1, 2, 3, 4, 5], 'dob': (
    23, 5, 13), 'Dict': {'English': 'Oxfard', 'Marathi': 'nibandha'}}
print(d)

# o/p :
# {'Name ': 'Arya', 'No': [1, 2, 3, 4, 5], 'dob': (23, 5, 13), 'Dict': {'English': 'Oxfard', 'Marathi': 'nibandha'}}

# Dictionary using constructor's
print('')
# don't use dict as a Dictionary name because it is inbuilt function
Dict = dict([(1, 'geeks'), (2, 'for')])
print(Dict)

# o/p:
# {1: 'geeks', 2: 'for'}
# PS F:\Coding Practise\GTT Python Training>

# Nested Dictionary

# dn = {{'d1': 'names'}, {'d2': [1, 2, 3, 4, 5]}} # error

# print("Nested Dictionary is :", dn)

#  o/p :
#   File "f:\Coding Practise\GTT Python Training\29_Dictionary.py", line 34, in <module>
#     dn = {{'d1': 'names'}, {'d2': [1, 2, 3, 4, 5]}}
# TypeError: unhashable type: 'dict'
# PS F:\Coding Practise\GTT Python Training> python -u "f:\Coding
# Practise\GTT Python Training\29_Dictionary.py"


# Adding elements to Dictionary
dnn = {}
dnn[0] = 'India'
dnn[1] = [1, 2, 3, 4, 5]
dnn[2] = (9, 8, 7, 6)
dnn[3] = {'d1': 'name1', 'd2': 'name2', 'd3': 'name3'}
print('')
print('Dictnionary formed is : ', dnn)

# o/p :
# Dictnionary formed is :  {0: 'India', 1: [1, 2, 3, 4, 5], 2: (9, 8, 7, 6), 3: {'d1': 'name1', 'd2': 'name2', 'd3': 'name3'}}
# PS F:\Coding Practise\GTT Python Training>

print("")
thisdict = {'brand': 'ford', 'model': 'Mustang', 'year': 1964}
print("The Dictionary is :", thisdict)
mydict = thisdict.copy()
print(mydict.values())
# print(mydict.updated({4:'nexa'}))
print(mydict.keys())
print(mydict.items())
print(len(mydict))
print(str(mydict))

# o/p:
# The Dictionary is : {'brand': 'ford', 'model': 'Mustang', 'year': 1964}
# dict_values(['ford', 'Mustang', 1964])
# dict_keys(['brand', 'model', 'year'])
# dict_items([('brand', 'ford'), ('model', 'Mustang'), ('year', 1964)])
# 3
# {'brand': 'ford', 'model': 'Mustang', 'year': 1964}
# PS F:\Coding Practise\GTT Python Training> 
