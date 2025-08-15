''' Write a Python program to check if a triangle is equilateral, isosceles or scalene. '''

x = input('Input lengths of the triangle sides:')
y = input('Input lengths of the triangle sides:')
z = input('Input lengths of the triangle sides:')

if x == y == z :
    print('it is an equilateral triangle')
    
elif x == y != z :
    print('it is an isosceles triangle')
    
elif x != y != z :
    print('it is an scalene triangle')