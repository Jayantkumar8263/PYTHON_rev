''' Write a Python program to convert a month name to a number of days.
January, February, March, April, May, June, July, August
, September, October, November, December'''

x = input('Enter the month :')

if x in ('January', 'March', 'May', 'July', 'august', 'octuber', 'December'):
    print("no. of days is 31",)
    
elif x == 'February':
    print('no. of days is 28/29', )
    
elif x in ('April', 'June', 'September', 'November'):
    print('no. of days is 30', )
    
else:
    print('Invalid')