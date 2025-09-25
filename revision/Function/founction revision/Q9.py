'''Write a function that uses `**kwargs` to create and return a dictionary of user profile information.'''

def profile_info(**profile):
    return profile
a = profile_info( name = 'bob', age = 17, city = 'bhilai')
print(f'profile of bob is : {a}')
b = profile_info( name = 'kenny', age = 18, city = 'bhilai')
print(f'profile of kenny is : {b}')
