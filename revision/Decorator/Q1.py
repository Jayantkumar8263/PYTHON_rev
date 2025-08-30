'''1. Create a Decorator to Log Function Arguments and Return Value

Write a Python program to create a decorator that logs the arguments and return value of a function.'''

def dec_fun(dec):
    def wrapper(a, b):
        print('the sum of and b is :', a+b)
    wrapper(5, 6)
@dec_fun 
def if_even(c, d):
   return c + d
if_even(8,9)