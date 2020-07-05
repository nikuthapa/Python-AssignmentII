"""
Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""


def is_prime(num1):
    if num1 == 1:
        return False
    elif num1 == 2:
        return True
    else:
        if num1>1:
            for x in range(2, num1):
                if (num1 % x) == 0:
                    return False
            return True
        else:
            return False


number = int(input("Enter a number:"))
print(is_prime(number))