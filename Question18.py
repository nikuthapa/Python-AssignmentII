"""
Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
"""

import json

dict1 = {'name': 'Anna', 'age': 21}
with open("dict_file.json", "w") as write_file:
    json.dump(dict1, write_file)


with open("dict_file.json", "r") as read_file:
    json_data = json.load(read_file)
print(json_data)