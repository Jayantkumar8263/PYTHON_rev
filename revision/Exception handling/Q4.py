'''Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.'''
try:
    a = int(input( 'Enter a number :'))
    b =int(input( 'Enter a number :'))
    print(a,b)
except:
    print('TypeError')