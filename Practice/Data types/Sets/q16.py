'''Write a Python program to check if a given value is present in a set or not.'''

x = {234,567,890,368,934}
y = int(input("Enter a number: "))
if y in x :
    print(y,'is in the set')
else:
    print(y,'is not in the set')
