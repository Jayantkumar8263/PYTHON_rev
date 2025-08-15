'''Write a Python program to check if a specified element appears in a tuple of tuples.
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False'''

a = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
for i in a:
    if 'White' in i:
        print('True')
    else:
        print('False')
    break
for i in a:
    if 'Olive' in i:
        print('True')
    else:
        print('False')