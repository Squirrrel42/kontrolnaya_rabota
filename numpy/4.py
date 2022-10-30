# задача 4 из tasks.pdf

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

def factorial(x):
    res = 1
    while(x > 0):
        res *= x
        x -= 1
    return res

def n_step(n, a):
    res = 0
    for i in range(0, n+1):
        res += (-1) ** i / factorial(2*i) * np.linalg.matrix_power(a,2 * i)
    return res



def cos_matrix(a, epsilon=0.01):
    n = len(a)
    cos1 = n_step(0,a)
    cos2 = n_step(1,a)
    c = 0
    step = 2
    while(c != 1):
        c = 1
        for i in range(n):
            for j in range(n):
                if(np.abs(cos1[i, j] - cos2[i, j]) >= epsilon):
                    c = 0
                    break
        if(c == 0):
            cos1 = cos2
            cos2 = n_step(step,a)
            step += 1
    return cos2

print(cos_matrix(a,0.000000001))