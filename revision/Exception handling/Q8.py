'''Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.'''

try : 
    a = int(input('Enter the number :'))
    b = int(input('Enter the number :'))
    c = input('Enter the number :')
    if c == '+' :
        print(a + c)
    elif c == '-':
        print(a - c)
    elif c == '*':
        print(a * c)
        
    elif c == '/':
        print(a / c)
        
    elif c == '//':
        print(a//c)
        
except : 
    print('ArithmeticError')