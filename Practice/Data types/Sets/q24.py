'''Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.'''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = set(x)
y = set(y)
print(max(x)*max(y))