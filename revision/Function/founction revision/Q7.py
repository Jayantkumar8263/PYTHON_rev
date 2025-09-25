'''
Write a function `fibonacci_recursive(n)` that returns the nth Fibonacci number using recursion.'''

def fibonacci(n):
    if n <= 1:
        return n
    a = 0  
    b = 1  
    for _ in range(n - 1):
        a, b = b, a + b
        
    return b
print(f"fibonacci_simple(7) = {fibonacci(7)}")   
print(f"fibonacci_simple(10) = {fibonacci(10)}") 