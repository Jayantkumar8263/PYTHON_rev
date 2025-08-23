'''Write a Python program to check whether a given string is a number or not using Lambda.'''

x = int(input('enter the string : '))

y = lambda a : True if a.isdigit() else False
print(y(x))