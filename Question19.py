"""
Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
"""


class Solutions:

   def validity_str_parentheses(self, a):
        stack_in_list, p_char = [], {"(": ")", "{": "}", "[": "]"}
        for p in a:   # p stands for parentheses.
            if p in p_char:
                stack_in_list.append(p)
            elif len(stack_in_list) == 0 or p_char[stack_in_list.pop()] != p:
                return False
        return len(stack_in_list) == 0


x = input("Enter a string of parentheses:")     # You can enter '()', '()[]{}', '[)', '({[)]' and '{{{'.
print(Solutions().validity_str_parentheses(x))
