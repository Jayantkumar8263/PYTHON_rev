'''Write a function that uses `*args` to accept any number of arguments and returns their average.'''

def avg_of_n(*num):
    if not num:
        return 0 
    
    return sum(num)/len(num)
n = avg_of_n(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Average of these numbers are :{n}')