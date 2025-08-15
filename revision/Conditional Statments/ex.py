n = int(input('Enter the no. :'))
if n % 2 != 0 or  n % 2 == 0 in range(6, 20):
    print('Weird')
elif n % 2 == 0 in range(2, 5) or n > 20:
    print('Not Weird')