'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.'''
try:
    a = int(input( 'Enter a number :'))
    print(a,'is an intiger')
except:
    print('it is a valueError')