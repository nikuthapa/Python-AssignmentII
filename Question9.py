"""
Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""


def binary_search(sequence_number, item):
    sequence_number = sorted(sequence_number)
    low_value = 0
    mid_value = 0
    high_value = len(sequence_number) - 1

    while low_value <= high_value:
        mid_value = (high_value + low_value) // 2
        if sequence_number[mid_value] < item:
            low_value = mid_value + 1
        elif sequence_number[mid_value] > item:
            high_value = mid_value - 1
        else:
            return "The index of the item : %d" % mid_value
    return "Item not found: %d" % -1


list_of_sequence = [2, 9, 7, 3, 12, 10, 4, 13, 15, 20, 40, 36]
list_of_sequence.sort()
print("Sorted Sequence:", list_of_sequence)

a = int(input("Enter the number, a value:"))
b = int(input("Enter the number, b value:"))

print(binary_search(list_of_sequence, a))
print(binary_search(list_of_sequence, b))