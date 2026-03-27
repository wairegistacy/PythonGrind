def max_value(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
    else:
        return 'Invalid'

a=12
b=25
c=18
assert max_value(24, 53, 48) == 53
assert max_value(98, 55, 79) == 98
print(max_value(a, b, c))
