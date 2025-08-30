'''Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''
try:
    a = int(input('enter a number :'))
    print(a/0)
except:
    print(f'{a} cannot be devide by zero (ZERODIVISIONERROR)')