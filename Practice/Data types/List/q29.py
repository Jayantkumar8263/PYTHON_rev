'''Write a Python program to get the frequency of elements in a list.'''

import collections
x = [1,1,1,1,1,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
print(collections.Counter(x))
"collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'x'"
