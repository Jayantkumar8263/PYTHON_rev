'''Write ta program to create a calculator using functions and input will be an user function, and the output will be stored in a file with the user input and the operator. 
output example : 
3+2 = 5'''
#starting function 
def calcy(a, op, b):
# appling condition
# addition
    if op == '+':
        return a + b
# substraction
    elif op == '-':
        return a - b
# multiplication
    elif op == '*':
        return a * b
# division
    elif op == '/':
        return a / b
# modulo
    elif op == '%':
        return a % b

# initilizing the inputs
a = int(input('Enter the number : '))
op = input('Enter the operator : ')
b = int(input('Enter the number : '))
result = calcy(a, op, b)
print(f"{a} {op} {b} = {result}\n")

# saving the file 
with open('calculator.txt', '+a') as file:
    file.write(f"{a} {op} {b} = {result}\n")