''' Write a Python program to add an item to a tuple.'''

x = (1, 2, 3, 4)
x = list(x)
x.append(5)
print(x)
x = tuple(x)
print(x)