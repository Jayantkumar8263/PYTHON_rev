'''Write a Python program to print the numbers of a specified list after removing even numbers from it.'''
a = [1,2,3,4,5,6,67,7,8]
a = [x for x in a if x % 2 != 0]
print(a)