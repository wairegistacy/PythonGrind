# check if a value is even or odd
def even(x):
    if x%2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
number = 8
assert even(2) == 'Even'
assert even(7) == 'Odd'
print(even(number))
