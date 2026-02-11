def reverse_list(input_list):
    reversed_list = []
    for item in input_list:
        # insert value at the given index position and shifts everything to the right
        reversed_list.insert(0, item)
    return reversed_list

numbers = [10, 20, 30, 40, 50]
print(reverse_list(numbers))
    

