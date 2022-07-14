# string
a = "This is python class."

# from first
print(a[0])
print(a[1])
print(a[2])
print(a[3])

# from last
print(a[-3])

# o/p:
# T
# h
# i
# s
# s
# PS F:\Coding Practise\GTT Python Training>

# Slicing Operations

print(a)
print(a[0:4:1])
print(a[:4:1])
print(a[0::])
print(a[:4:])
print(a[::1])
print(a[0:4:2])
print(a[0:4:-1])

# o/p :
# This
# This is python class.
# This
# This is python class.
# Ti

# Reverse String
str = "welcome"
print("Reverse String is : ", str[::-1])

# o/p :
# Reverse String is :  emoclew
# PS F:\Coding Practise\GTT Python Training>


# String Methords
print("")
print(len(str))
print(str.count)
print(str.find('e'))
print(str.index('w'))
print(str.split('o'))

# o/p :
# 7
# <built-in method count of str object at 0x0000018705890930>
# 1
# 0
# ['welc', 'me']

print("")
print(str.startswith('o'))
print(str.endswith('o'))
print(str.replace('w', 'W'))
print(str.upper())
print(str.lower())

# o/p:
# False
# False
# Welcome
# WELCOME
# welcome
# PS F:\Coding Practise\GTT Python Training>


word = '     hi  '
print("")
print(word.strip())
print(word.rstrip())
print(word.lstrip())
print("+".join(word))
print(word.swapcase())
print(word.title())
print(word.capitalize())

# o/p :
# hi
#      hi
# hi
#  + + + + +h+i+ +
#      HI
#      Hi
#      hi
# PS F:\Coding Practise\GTT Python Training>

# Strings are immutable
a = "Python"
print(a.upper())



