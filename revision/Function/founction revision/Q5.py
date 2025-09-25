'''Write a function `is_in_range(n, start, end)` that checks if a number `n` is within a given range (inclusive).'''
def range_check(n, start, end):
    return start<=n<=end
starting_range = 1
end_of_rqnge = 100
n = int(input(f'Enter the number between {starting_range} and {end_of_rqnge}:'))
if range_check(n, starting_range, end_of_rqnge):
    print(f'the number is within the range between {starting_range} and {end_of_rqnge}')
else:
    print(f'the number is not in the range between {starting_range} and {end_of_rqnge}')
