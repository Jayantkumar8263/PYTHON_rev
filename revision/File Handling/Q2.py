'''Write a Python program to read first n lines of a file.'''

a = open('read.txt', 'w+')
b = a.readlines()
print(b)
a.close()
