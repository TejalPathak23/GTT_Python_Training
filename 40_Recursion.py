# Function Calling Function

def tri_rec(k):
    if(k>0):
        result = k + tri_rec(k-1)
        print(result)
    else:
        result = 0
    return result

print('Recursion Example')
tri_rec(6)

# o/p:
# Recursion Example
# 1 
# 3 
# 6 
# 10
# 15
# 21
# PS F:\Coding Practise\GTT Python Training> 