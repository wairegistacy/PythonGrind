Program slow/fast 

BIG O NOTATION
- TIME COMPLEXITY
- SPACE COMPLEXITY

It measures the above metrics as the input grows


[1] - 1s
[1, 2] - 1s
[1, 2, 3] - 1s
[1, 2, 3, 4] - 1s
10items - 1s

constant time complexity O(1)

---

[1] - 1s
[1, 2] - 2s
[1, 2, 3] - 3s
[1, 2, 3, 4] - 4s
10items - 10s

linear time complexity O(n)

---

[1, 2] - 1s
[1, 2, 3, 4] - 2s
[1...8] - 3s
[1...16] - 4s
[1...32] - 5s

logarithmic time complexity O(logn)
input - sorted

>> Binary Search

---

[1] - 1s
[1, 2] - 2s
[1, 2, 3] - 4s
[1, 2, 3, 4] - 8s

Quadratic time complexity O(n^2)

---

'''
Data structure >> a collection-representation of similar type of data
- list / array
- tuple
- set
- dictionary
- linkedlist
- graph

LIST - TIME COMPLEXITY

inbuilt operations
https://cs.stanford.edu/people/nick/py/python-list.html
list -> [1, 2, 3, 4, 5]
- append >> O(1)
    > 3 > O(1)
    > 7 > O(1)
- insert >> O(n) - we are shifting all items to the right and getting new indexes in memory
- extend
    > [6, 7, 8] > O(3)
    > [6, 7, 8, 9, 10] > O(5)
- pop - remove last index >> O(1)
- pop(3) - remove index 3 >> O(n)
- len >> O(n)
    > [2, 3] - O(2)
    > [4, 5, 6, 7, 8] - O(5)
- remove
- lookup > item in list >> O(n)

# a list of people's height, find the tallest person
heights = [45, 23, 98, 5, 23]
def find_tallest(heights):
    tallest = 0 # O(1)
    for height in heights: # O(n)
        if height > tallest: # O(1)
            tallest = height # O(1)
    return tallest # O(1)

# time complexity - O(1) + O(n)[O(1), O(1)] + O(1) - O(n)

---

range(0, 5) - 0, 1, 2, 3, 4
range(0, 5 + 1) - 0, 1, 2, 3, 4, 5

# a list of people's height, find if there duplicates
heights = [45, 23, 98, 5, 45, 27]
def find_my_height(heights, my_height):
    for i, height in enumerate(heights): # O(n)
        for j in range(i + 1, len(heights)): # O(n)
            if heights[i] == heights[j]: # O(1)
                return True # O(1)
    return False # O(1)

# time complexity - O(n)[O(n) + O(1) + O(1)] - O(n ^ 2) >> Quadratic

def find_my_height(heights, my_height):
    seen_heights = [] # O(1)
    for height in heights: # O(n)
        if height in seen_heights: # O(n)
            return True  # O(1)
        else:
            seen_heights.append(height)  # O(1)

    return False # O(1)

---

SET(hashset) - TIME COMPLEXITY
- no duplicates
- items not ordered, no indices
- lookup > item in list >> O(1) (why - hashing)

# Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

def find_common(a, b):
    common = [] # O(1)
    for item_a in a: # O(n)
        if item_a in b: # O(n)
            common.append(item_a) # O(1)
    return common # O(1)

time complexity >> O(n ^ 2) >> Quadratic

--- 
def find_common_using_set(a, b):
    common = [] # O(1)
    b_set = set(b) # O(n)

    for item_a in a: # O(n)
        if item_a in b_set: # O(1)
            common.append(item_a) # O(1)
    return common # O(1)

time complexity - O(1) + O(n) + O(n)[O(1), O(1)] - O(1) + O(n) + O(n) + O(n)
>> O(n) >> Linear

def find_my_height(heights, my_height):
    seen_heights = set()
    for height in heights: # O(n)
        if height in seen_heights: # O(1)
            return True  # O(1)
        else:
            seen_heights.add(height)  # O(1)

    return False # O(1)
'''