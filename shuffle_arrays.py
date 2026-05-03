# SHUFFLING AN ARRAY
# Iterative method: 
# Time Complexity: 0 (n^2) -> 0(n * n)
# Space Complexity: 0(n)
import random
def shuffle(arr):
    shuffled = []
    for i in range(len(arr)): # Time Complexity -> 0(n)
        rand_index = random.randrange(len(arr)) # Time Complexity -> 0(1)
        shuffled.append(arr.pop(rand_index)) # Time Complexity -> 0(n) if pop was at the end of the array, it would be 0(n), but it pops randomly from any index of the array so time complexity will be 0(n)
    return shuffled

x = [5, 6, 9, 3, 1, 4, 2, 7]
print(shuffle(x))

# Sorting method: generate random float values using random.random() and iterate through the array assigning these values to each element in the array. Sort the array based on these values
# Time complexity: 0 (n log n)
# Space Complexity: 0 (n): using extra space for rand_values and rand_indexes
def shuffle(arr):
    rand_values = [random.random() for i in range(len(arr))] # generates random values between 0 and 1
    rand_index = list(range(len(arr)))
    rand_index.sort(key = lambda i : rand_values[i])
    return [arr [i] for i in rand_index]


# FISHER YATES ALGORITHM: swaps elements on the same array, generating a random index for array and swaps with the last index of the array
# Time Complexity: 0(n) 
# Space Complexity: 0(1) since it swaps elements and does this on the same array, no popping one element from one array to the other
def shuffle(arr):
    n = len(arr)
    last_index = n - 1
    while last_index > 0: # Time Complexity -> 0(n)
        rand_index = random.randint(0, n) # Time Complexity -> 0(1)
        arr[rand_index], arr[last_index] = arr[last_index], arr[rand_index] # Time Complexity -> 0(1)
        last_index -= 1
    return arr # Time Complexity -> 0(n)

# SATTOLO'S ALGORITHM: different from Fisher Yates as it excludes the last index hence uses randrange instead of randint, and removes the possibility of an element shuffled to its original position
# Time complexity: 0(n)
# Space complexity: 0(1)
def shuffle(arr):
    n = len(arr)
    last_index = n - 1
    while last_index > 0:
        rand_index = random.randrange(n)
        arr[rand_index], arr[last_index] = arr[last_index], arr[rand_index]
        last_index -= 1
    return arr
