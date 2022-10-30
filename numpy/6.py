#задача 6 из task_template

import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 2.5, -2])

def angle(a, b):
    module_a = 0
    module_b = 0
    for i in range(3):
        module_a += a[i] ** 2
        module_b += b[i] ** 2

    res = np.arccos(np.dot(a, b) / np.sqrt(module_a * module_b))
    return res

print(angle(a, b))