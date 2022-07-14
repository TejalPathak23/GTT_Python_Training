def greet():
    print('How are you ?')


greet()

# How are you ?
# How are you ?
# PS F:\Coding Practise\GTT Python Training>


def greet1(name):
    print('How are you', name, '?')


n = input('Enter the name :')
greet1(n)

# o/p:
# How are you ?
# Enter the name :Tejal
# How are you Tejal ?
# PS F:\Coding Practise\GTT Python Training> python -u "f:\Coding
# Practise\GTT Python Training\34_functions.py"
# How are you ?
# Enter the name :Sejal
# How are you Sejal ?
# PS F:\Coding Practise\GTT Python Training>

# Default Parameters


def myfunc(country="india"):
    print("I am from " + country)


myfunc('Sweden')
myfunc('Norway')
myfunc()
myfunc('Brazil')

# o/p:
# I am from Sweden
# I am from Norway
# I am from india
# I am from Brazil
# PS F:\Coding Practise\GTT Python Training>

# Even or Odd


def eoo():
    n = int(input('Enter a number :'))
    if(n % 2 == 0):
        print('It is even number')
    else:
        print('It is odd number')


eoo()

# o/p:
# Enter a number :7
# It is odd number
# PS F:\Coding Practise\GTT Python Training>

# Passig list as a parameter to the function


print('')


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# o/p:
# apple
# banana
# cherry
# PS F:\Coding Practise\GTT Python Training>

print('')
def number(no):
    for num in no:
        print(num)


no1 = [1, 2, 3, 4, 5]

number(no1)

# o/p:
# 1
# 2
# 3
# 4
# 5
# PS F:\Coding Practise\GTT Python Training>


# Return Values
def fun(x):
    return 5*x

x = fun(2)
print('The Number is :',x)

# o/p :
# The Number is : 10
# PS F:\Coding Practise\GTT Python Training> 
