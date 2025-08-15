'''Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
'''

a = {
    1: 10,
    2: 20
}
b = {
    3: 30,
    4: 40
}
c = {
    5: 50,
    6: 60
}
d = {}
for x in (a, b, c):
    d.update(x)
print('dictionary 1:', a)
print('dictionary 2:', b)
print('dictionary 3:', c)
print('concatenated dictionary:', d)
