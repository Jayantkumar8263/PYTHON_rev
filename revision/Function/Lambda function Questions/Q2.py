'''2. Function Lambda Generator

Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.'''

x = int(input('Enter the number : '))
a = int(input('Enter the number(no. of times multiplied) : '))
y = lambda x,a : x ** a
print(y(x,a))