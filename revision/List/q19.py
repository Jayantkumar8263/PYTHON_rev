'''Write a Python program to calculate the difference between the two lists.'''

x = [1, 2, 3, 4, 5, 6]
y = [5, 6, 7, 8, 9, 10]

z = list(set(x)-set(y))
a = list(set(y)-set(x))
b = a + z
print(z, a)
print(b)
