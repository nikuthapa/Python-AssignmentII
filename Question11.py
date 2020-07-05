"""
Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?
"""

# Finding extension.
filename = "data.csv"
extension = filename[-3:]
print("The extension of a file:", extension)


# Getting filename without extension.
f_name = 'README.txt'
file_name = f_name[:-4]
print("The name of the file :", file_name)