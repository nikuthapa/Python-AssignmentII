"""
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""


list1 = [{'Id': 'S2', 'Name': 'Suraj'}, {'Id': 'S1', 'Name': 'Sudarsan'}, {'Id': 'V2', 'Name': 'Vijay'}]
print("This is original list:", list1)

l_dict = {'Id': 'A1', 'Name': 'Anish'}
l_dict_copy = l_dict.copy()
list1.append(l_dict_copy)
print("This is list after adding dictionary element:", list1)


def sort_list_dict(list1):
    list1.sort(key = lambda a: a['Id'])
    return list1


print("List after sorting:", sort_list_dict(list1))

items_list = [list1[0], list1[1]]
print("The first and second items in the list:", items_list)