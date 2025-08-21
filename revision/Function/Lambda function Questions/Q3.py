'''Write a Python program to sort a list of tuples using Lambda.'''

'''x = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
y = lambda x : x
print(y(sorted(x)))'''

x = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sort_x = sorted(x, key=lambda point: point[1])# Sort based on the y-coordinate
print(sort_x)