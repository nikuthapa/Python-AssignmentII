"""
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

from statistics import mean


list_of_tuples = [('Niku', 'Thapa', 22), ('Dikshya', 'Shrestha', None),
            ('Nanu', 'Rana', 25), ('Sheelu', 'Sharma', None), ('Prem', 'Gurung', 24), ('Tara', 'Rana', 20)]


def avg_age(list_t):
    list_of_age = []
    for values in list_t:
        if values[2] is not None:
            list_of_age.append(values[2])
    return mean(list_of_age)


print("Average age = ", avg_age(list_of_tuples))


for i in range(len(list_of_tuples)):
    full_name = list_of_tuples[i][0] + ' ' + list_of_tuples[i][1]
    if list_of_tuples[i][2]:
        if list_of_tuples[i][2] < avg_age(list_of_tuples):
            print("^_^", full_name + " is young.")
        else:
            print("***", full_name + " is old.")
    else:
        print("#", full_name)



