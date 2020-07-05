"""
Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""


class Solutions:
    def sum_three_elem(self, x):
        x, r, i = sorted(x), [], 0         # x stands for number and r stands for result.
        while i < len(x) - 2:
            a, k = i + 1, len(x) - 1
            while a < k:
                if x[i] + x[a] + x[k] < 0:
                    a += 1
                elif x[i] + x[a] + x[k] > 0:
                    k -= 1
                else:
                    r.append([x[i], x[a], x[k]])
                    a, k = a + 1, k - 1
                    while a < k and x[a] == x[a - 1]:
                        a += 1
                    while a < k and x[k] == x[k + 1]:
                        k -= 1
            i += 1
            while i < len(x) - 2 and x[i] == x[i - 1]:
                i += 1
        return r


print("Output:", Solutions().sum_three_elem([-25, -10, -7, -3, 2, 4, 8, 10]))