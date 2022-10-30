# задача 2 из tasks.pdf

import numpy as np

def Levi_Civita(n):
    numbers = np.linspace(0, n ** n - 1, n ** n)
    index = np.zeros((n ** n, n))

    for i in range(n ** n):
        for j in range(n - 1, -1, -1):
            index[i, j] = numbers[i] % n
            numbers[i] = numbers[i] // n

    Levi_Civita_symbol = np.zeros((n ** n))

    def sign(arr):
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] == arr[j]):
                    return 0
                if (arr[i] > arr[j]):
                    count += 1
        res = (-1) ** count
        return res

    for i in range(n ** n):
        Levi_Civita_symbol[i] = sign(index[i])

    new_shape = np.array([n] * n)

    Levi_Civita_symbol = Levi_Civita_symbol.reshape(new_shape)

    return Levi_Civita_symbol