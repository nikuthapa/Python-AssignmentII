"""
Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""

tuple1 = ('Niku', 'Thapa', 22) # Create a tuple with your first name, last name, and age.
print("This is tuple:", tuple1)

# Create a list,people, and append your tuple to it.
list2 = [('Anna', 'Sharma', 21),('Dipesh', 'Koirala',22), ('Nilej', 'Sthapit',23)]
print("List of people:", list2)

list2.append(tuple(tuple1))
print("list of people after adding tuple:",list2)


# Make more tuples with the corresponding information from your friends and append them to the list.
tuple2 = (('Sanish', 'Gurung', 21), ('Bibek', 'Gupta', 20))
list2. append(tuple(tuple2))
print("List of people after adding more tuples:", list2)


def sort_list_tup (list2):
    list2.sort(key = lambda x : str(x[1]))
    return list2


print("List of tuples after sorting out:", sort_list_tup(list2))