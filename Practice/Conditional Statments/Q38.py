'''Write a Python program to display the astrological sign for a given date of birth.'''

x = int(input('Enter the date : '))
y = input('Enter the month : ')

print(x)
if y == 'january':
    print('your zodiak sign is :  Capricorn and Aquarius')

elif y == 'February':
    print('your zodiak sign is :  Aquarius and Pisces')
    
elif y == ' March':
    print('your zodiak sign is :  Pisces and Aries')
    
elif y == 'April':
    print('your zodiak sign is :  Aries and Taurus')
    
elif y == 'May':
    print('your zodiak sign is :  Taurus and Gemini')
    
elif y == 'June':
    print('your zodiak sign is :  Gemini and Cancer')
    
elif y == ' July':
    print('your zodiak sign is :  Cancer and Leo')

elif y == 'August':
    print('your zodiak sign is :  Leo and Virgo')
    
elif y == 'September':
    print('your zodiak sign is :  Virgo and Libra')
    
elif y == 'October':
    print('your zodiak sign is :  Libra and Scorpio')
    
elif y == 'November':
    print('your zodiak sign is :  Scorpio and Sagittarius')
    
elif y == ' December':
    print('your zodiak sign is :  Sagittarius and Capricorn')
else:
    print('you ar e an aliean')