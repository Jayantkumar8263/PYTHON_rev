'''Write a Python program to find elements in a given set that are not in another set.'''
x = {10, 12, 15, 17}
y = {11, 13, 16, 10}
z = x.intersection(y)
a = x.union(y)
print(a-z)