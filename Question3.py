"""
Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""


p = """ The act of the cat is so annoying. 
    It was an inch far away from me but I got hurt my chin then saw a rat. """

paragraph = p.split()


def find_anagrams(paragraph):
    dict1 = {}
    for words in paragraph:
        key = ''.join(sorted(words))

        if key in dict1.keys():
            dict1[key].append(words)
        else:
            dict1[key] = []
            dict1[key].append(words)
        result = ""
        for key, value in dict1.items():
            if len(value) > 1:
                result = result + ' '.join(value) + ' '

    return result


print("Anagrams words from paragraph are:", find_anagrams(paragraph))