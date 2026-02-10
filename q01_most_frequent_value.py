data = {"a": "apple", "b": "banana", "c": "apple", "d": "orange", "e": "apple"}
counts = {}
for value in data.values():
    counts[value] = counts.get(value, 0)+ 1

max_value = max(counts, key=counts.get)
print(max_value)
