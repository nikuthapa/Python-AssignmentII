"""
Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""


def is_palindrome(w):
    w = w.lower()
    if w == w[::-1]:
        print(w, "is a palindrome.")
    else:
        print(w, "is not a palindrome.")


word = input("Enter a word to check palindrome: ")
is_palindrome(word)
