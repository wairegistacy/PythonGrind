data = {"a": "apple", "b": "banana", "c": "apple", "d": "orange", "e": "apple"}
counts = {}
for value in data.values():
    counts[value] = counts.get(value, 0)+ 1

max_value = max(counts, key=counts.get)
print(max_value)


def most_frequent_value(data):
    for value in data.values():
        # check if we have counted this value before
        if value in counts:
            # increase count
            counts[value] += 1
        # if not seen before, then start its count at 1
        else:
            counts[value]= 1

    max_count = 0
    most_frequent = None

    for value, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent = value

    return most_frequent

print(most_frequent_value(data))
