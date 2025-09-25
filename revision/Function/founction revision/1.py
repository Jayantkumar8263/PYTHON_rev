'''Write a function `max_of_three(a, b, c)` that takes three numbers as arguments and returns the largest of them'''

def max_of_three(a, b, c):
    d = max(a, b, c)
    print('maximum number betweem a, b, c is : ', d)
x = int(input('Enter the number :'))
y = int(input('Enter the number :'))
z = int(input('Enter the number :'))
max_of_three(x, y, z)