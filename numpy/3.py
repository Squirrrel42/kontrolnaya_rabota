# задача 3 из tasks.pdf

import numpy as np
import Levi_Civita as lc

matrix = np.random.random_sample((4, 4))
#matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

def determinant(matrix):
    n = len(matrix)

    symbol = lc.Levi_Civita(n).reshape(n ** n)

    numbers = np.linspace(0, n ** n - 1, n ** n)
    index = np.zeros((n ** n, n))

    for i in range(n ** n):
        for j in range(n - 1, -1, -1):
            index[i, j] = numbers[i] % n
            numbers[i] = numbers[i] // n

    res = 0

    for i in range(n ** n):
        product = symbol[i]
        for j in range(n):
            product *= matrix[j,int(index[i, j])]
        res += product

    return res

print(determinant(matrix))
print(np.linalg.det(matrix))