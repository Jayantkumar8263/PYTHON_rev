''' Write a Python script to sort (ascending and descending) a dictionary by value '''

a = {
    'a': 1, 
    'b': 2, 
    'c': 3, 
    'd': 4
    }
print('dictionary:', a)
print('sorted dictionary:',sorted(a))
print('sorted reverse dictionary:')
print(sorted(a, reverse=True, ))