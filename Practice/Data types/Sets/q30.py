'''Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.'''

x = ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
x = set(x)
print(sorted(list(x)))