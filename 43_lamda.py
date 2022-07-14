# one liner code
def x(n): return n*5


print(x(4))

# o/p:
# 20
# PS F:\Coding Practise\GTT Python Training>


def x(n1, n2, n3): return n1*n2*n3


print(x(4, 5, 6))

# o/p:
# 120
# PS F:\Coding Practise\GTT Python Training>

# lamda in function


def func(n):
    return lambda a: a*n

x = func(11)
print(x(2))

# 22
# PS F:\Coding Practise\GTT Python Training> 