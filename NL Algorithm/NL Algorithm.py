import pandas as pd
import scipy.spatial.distance as sp


feature_space = pd.read_csv("../Support Files/test_dataset.csv", header=None, engine='python')
dimensions = 8
data = feature_space.iloc[:, 0:dimensions].values
array_size = (data.__len__() / 2).__round__()
array1 = data[0:array_size]
array2 = data[array_size:data.__len__()+1]
D = 0.82
M = 40
non_outliers_array = []

for first_set in array1:
    count_i = 0
    for second_set in array1:
        distance = sp.euclidean(first_set, second_set)
        if distance <= D:
            count_i += 1
            if count_i > M:
                non_outliers_array.append(first_set)
                break

for first_set in array1:
    count_i = 0
    v = first_set == non_outliers_array
    if v.any():
        continue
    for second_set in array2:
        distance = sp.euclidean(first_set, second_set)
        if distance <= D:
            count_i += 1
            if count_i > M:
                if not v.any():
                    non_outliers_array.append(first_set)
                break

for first_set in array2:
    count_i = 0
    for second_set in array2:
        distance = sp.euclidean(first_set, second_set)
        if distance <= D:
            count_i += 1
            if count_i > M:
                non_outliers_array.append(first_set)
                break

outliers = []
data_temp = [list(item) for item in data]
non_outliers_temp = [list(item) for item in non_outliers_array]

for row in data_temp:
    if not non_outliers_temp.__contains__(row):
        outliers.append([data_temp.index(row), row])

print("Identified Outliers using NL Algorithm: ")
print(f"With N = {data.__len__()}, Dimensions = {dimensions}, D = {D}, M = {M}")
print("Number of non-outliers: ", non_outliers_array.__len__())
print("Number of identified outliers: ", outliers.__len__())
print("Outliers: ", *outliers, sep="\n")

