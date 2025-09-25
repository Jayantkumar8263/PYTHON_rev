'''Create a simple calculator using functions for each operation (`add`, `subtract`, `multiply`, `divide`)'''

def calculator(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a + b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '%':
        return a % b
a = int(input('Enter the number :'))
op = input('Enter the operator :')
b = int(input('Enter the number :'))
d = calculator(a, op, b)
print(f"{a} {op} {b} = {d}")