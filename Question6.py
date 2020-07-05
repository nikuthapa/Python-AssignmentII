"""
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""

friend_names = ['Mohit', 'John', 'Harry', 'Anuska', 'Dikshya', 'Pramod']


def search_name(friend_names):
    for i in friend_names:
        if i == 'John':
            return i

    return "Not found!!!"


print(search_name(friend_names))
