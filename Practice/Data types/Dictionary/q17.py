'''Write a Python program to remove duplicates from the dictionary.'''

a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 1,
    'e': 2,
    'a': 1,
    'e': 2
}

b = set(a.items())
print(b)