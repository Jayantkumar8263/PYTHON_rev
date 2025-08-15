''' Write a Python program to remove an item from a set if it is present in the set.'''

x = {1,2,3,4,5,6,7,8,9,10}

if 2 in x:
    remove = x.remove(3)
    print(x, remove)
    
else:
    print("number is not present in the set")
    