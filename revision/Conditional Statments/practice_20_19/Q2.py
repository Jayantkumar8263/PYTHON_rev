level = 5
power = 10

level += 1 # This updates level first!
power *= level # This uses the *new* value of level
print(power, 'power')
print(level, 'level')

is_strong = (power > 50)
print(is_strong)