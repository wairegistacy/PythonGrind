text = "hello"
count = {}
for char in text:
    count[char] = count.get(char, 0)+1

print(count)
