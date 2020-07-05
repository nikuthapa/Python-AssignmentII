"""
Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22John,54 Love Ave,21
"""

import csv


def write_csv(file_name, list_of_tuples):
    f_name = file_name + '.csv'
    with open(f_name, 'w', newline='') as output:
        csv_file = csv.writer(output)
        csv_file.writerow(['name', 'address', 'age'])
        for r in list_of_tuples:
            csv_file.writerow(r)


personal_info = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
name_of_file = 'data'
write_csv(name_of_file, personal_info)