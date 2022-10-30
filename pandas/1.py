#задача 1 из tasks.pdf

import pandas as pd
import numpy as np

f = pd.read_csv("use.csv")

print(f.head())

number_of_students = len(f[(f.Математика != None) | (f.Физика != None) | (f["Русский язык"] != None)])

mean_math = f.Математика.mean()

mean_russian_for_physicists = f[f.Физика == 100]["Русский язык"].mean()

math_unique = f.Математика.unique()

temp = np.empty((len(math_unique), 2))

for i in range(len(f)):
    for j in range(len(math_unique)):
        temp[j, 0] = f[f.Математика == math_unique[j]].Физика.max()
        temp[j, 1] = f[f.Математика == math_unique[j]]["Русский язык"].min()

agg_math = pd.DataFrame({"Математика": math_unique, "Физика": temp[:, 0], "Русский язык": temp[:, 1]})

count = np.zeros(len(math_unique))

for i in range(len(f.Математика)):
    for j in range(len(math_unique)):
        if(f.Математика.iloc[i] == math_unique[j]):
            count[j] += 1

agg_math_count = pd.DataFrame({"Математика": math_unique, "Count": count})

number_coincidences = 0
for i in range(len(f)):
    if(f.Математика.iloc[i] == f.Физика.iloc[i] and f.Физика.iloc[i] == f["Русский язык"].iloc[i]):
        number_coincidences += 1

sum = np.empty(len(f))

for i in range(len(f)):
    sum[i] = f.Математика.iloc[i] + f.Физика.iloc[i] + f["Русский язык"].iloc[i]

sum = pd.Series(sum).sort_values()

sum_unique = sum.unique()

count_sum = np.zeros(len(sum_unique))

for i in range(len(sum_unique)):
    for j in range(len(sum)):
        if(sum_unique[i] == sum[j]):
            count_sum[i] += 1

sum_once = np.empty(0)

for i in range(len(count_sum)):
    if(count_sum[i] == 1):
        sum_once = np.append(sum_once, sum_unique[i])

max_number_coincidence = sum_once.max()

dictionary = {"number_of_students": number_of_students, "mean_math": mean_math, "mean_russian_for_physicists": mean_russian_for_physicists, "agg_math": agg_math, "agg_math_count": agg_math_count, "number_coincidences":number_coincidences, "sum": sum, "max_number_coincidence": max_number_coincidence}