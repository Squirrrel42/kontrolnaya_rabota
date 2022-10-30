#задача 7 из task_templated

import numpy as np

a = np.array([[2, 3, 4, 5], [3, 3, 4, 5], [4, 4, 4, 5], [1, 1, 1, 1]])
b = np.array([[30],[34],[41], [10]])

def solve(a, b):
    return np.linalg.solve(a, b)

print(solve(a, b))