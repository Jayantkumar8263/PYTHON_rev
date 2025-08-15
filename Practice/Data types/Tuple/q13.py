''' Write a Python program to remove an item from a tuple.'''
x = ('a', 'b', 'c', 'd', 'e')
y = list(x)
y.remove('d')
print(tuple(y))