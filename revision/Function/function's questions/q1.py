'''Write a function `max_of_three(a, b, c)` that takes three numbers as arguments and returns the largest of them.'''

def maximum(a, b, c):
    x = max(a, b, c)
    print("maximum of these three is :", x)
num1 = int(input('enter the number : '))
num2 = int(input('enter the number : '))
num3 = int(input('enter the number : '))
maximum(num1, num2, num3)