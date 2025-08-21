'''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.'''

'''x = int(input('enter the number : '))
A = lambda a, x : a + x
print(A(15,x))'''

x = int(input('Enter the number : '))
y = int(input('Enter the number : '))
M = lambda x, y : x * y
print(M(x, y))