'''Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.'''

try : 
    a = [1,2,3,4,5]
    print(a[6])
except:
    print('IndexError,theindex is out of range')