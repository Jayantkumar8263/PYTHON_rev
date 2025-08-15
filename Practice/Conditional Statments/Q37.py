'''Write a Python program that reads two integers representing a month and day and prints the season for that month and day.'''
'''January, February, March, April, May, June, July, August, September, October, November, December'''

x = int(input('Enter the date : '))
y = input('Enter the month : ')

#if x>1 and x<31 :
print(x)
    
if y in ('March', 'April'):
    print('Spring')
    
elif y in ('May', 'June'):
    print('Summer')
    
elif y in ('July', 'August'):
    print('Monsoon')
    
elif y in ('September', 'October'):
    print('Autumn')
    
elif y in ('November', 'December'):
    print('pre winter')
    
elif y in ('December', 'January', 'February'):
    print('winter')

else:
    print('Invalid')