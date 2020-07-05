"""
Write an if statement to determine whether a variable holding a year
is a leap year.
"""


def check_leap_year(y):  # y stands for year.
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


y = int(input("Enter a year:"))

if (check_leap_year(y)):
    print("This is a leap year.")
else:
    print("This is not a leap year.")
