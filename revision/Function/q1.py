'''Write a Python function to find the maximum of three numbers.'''

def maximum(a, b, c):
    x = max(a, b, c)
    print("maximum of these three is :", x)
num1 = int(input('enter the number : '))
num2 = int(input('enter the number : '))
num3 = int(input('enter the number : '))
maximum(num1, num2, num3)