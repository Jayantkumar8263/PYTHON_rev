'''Write a Python program to find the intersection of two given arrays using Lambda.'''

a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]
result = list(filter(lambda x: x in a, b))
print('intersections are : ', result)