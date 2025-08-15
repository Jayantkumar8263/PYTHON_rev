'''Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.'''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = set(x)
print(max(x))
print(sorted(x)[-3])
