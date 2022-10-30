#задача 2 из tasks.pdf

import pandas as pd
import numpy as np

f = pd.read_csv("date.csv")
n = len(f)

date = np.empty((n,3))
for i in range(n):
    temp = f.date.iloc[i]
    date[i] = temp.split(".")

days_count = np.empty((n), dtype=int)

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(n):
    days_count[i] = date[i, 0] * 365
    days_count[i] += date[i, 0] // 4
    for j in range(int(date[i, 1])):
        days_count[i] += days[j]
    days_count[i] += date[i, 2]

f["days_count"] = days_count

print(f)