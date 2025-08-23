'''Write a Python program to extract year, month, date and time using Lambda.'''

import datetime
now = datetime.datetime.now()
x_year = lambda x : x.year
x_month = lambda x : x.month
x_day = lambda x : x.day

print(x_year(now))
print(x_month(now))
print(x_day(now))