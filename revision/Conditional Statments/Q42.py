import time
timestamp = time.strftime('%H,%M,%S')
h = int(time.strftime('%H'))
print(timestamp)
# condition 
if(h >= 5 and h <=12) :
    print('good morning')
elif (h >= 12 and h <= 16):
    print('good afternoon')
elif (h >= 17 and h <= 20):
    print('good Eveaning')
elif (h >= 21 and h <= 24):
    print('good Night')
else:
    print('Invalid')