'''Write a Python program to find the intersection of two given arrays using Lambda.'''

a = input('Enter an array :')
b = input('Enter an array :')
x = list(filter(lambda x : x in a and b ))
print(x(a,b))