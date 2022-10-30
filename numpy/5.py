#зачада 5 из task_template

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

def product(a, b):
    return np.dot(a, b)

print(product(a, b))