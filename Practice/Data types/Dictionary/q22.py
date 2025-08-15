'''Write a Python program to find the highest 3 values of corresponding keys in a dictionary .'''

x = {
    'a': 100,
    'b': 200,
    'c': 300,
    'd': 400,
    'e': 500
}

print(x)
print(set(x.values())) 
print(sorted(set(x.values())[:3]))