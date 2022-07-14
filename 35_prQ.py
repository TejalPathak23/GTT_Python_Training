# Python Function to sum all the number's in the list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("Sum is :",sum((8, 2, 3, 0, 7)))