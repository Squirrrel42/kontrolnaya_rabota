#задача 4 из tasks.pdf

import pandas as pd
import numpy as np

arr = np.random.randint(0, 1000000, 1000)

def func(arr, threshold, width):
    ind = np.arange(0, len(arr))

    df = pd.DataFrame({"data": arr, "ind": ind})

    df2 = df[df.data >= threshold]

    n = len(df2)

    res = []

    if(df2.ind.iloc[1] - df2.ind.iloc[0] > width):
        res.append(df2.ind.iloc[0])

    for i in range(1, n - 1):
        ind_i = df2.ind.iloc[i]
        ind_i_prev = df2.ind.iloc[i - 1]
        ind_i_next = df2.ind.iloc[i + 1]
        if(ind_i - ind_i_prev > width and ind_i_next - ind_i > width):
            res.append(df2.ind.iloc[i])

    if (df2.ind.iloc[-1] - df2.ind.iloc[-2] > width):
        res.append(df2.ind.iloc[-1])

    return res

print(func(arr, 900000, 10))