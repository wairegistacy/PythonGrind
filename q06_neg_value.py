def neg_value(data):
    results = []
    for x in data:
        if x<0:
            continue
        print(x)
        results.append(x)
    return results
    
numbers = [-2, 4, -1, 6, 0, -3, 8]
assert neg_value([2, 4, -6, 8]) == [2,4,8]
neg_value(numbers)

