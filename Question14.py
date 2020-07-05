"""
Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""

import csv


def read_csv(f_name):
    with open(f_name, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list1 = []
        for row in csv_reader:
            list1.append(row)
        return list1


file_name = 'data.csv'
print("Output:", read_csv(file_name))