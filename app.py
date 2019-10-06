import pandas as pd
import scipy.io.arff as loader
import arff as ar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sp

# Loading the dataset into array
data = []
data2 = [[]]
# dataset = ar.load(open('Wilt_withoutdupl_norm_02_v01.arff'))
for i in range(0, np.array(dataset['data']).shape[0]):
    data_holder = np.array(dataset['data'][i])
    data.append(data_holder[0:5])
    data2.append(data[i])

test = pd.DataFrame(data2[1])
test2 = pd.DataFrame(data[2])

buffer_size = data.__len__() / 4
# print(buffer_size)

print(data2[1])
# array1 = data[0: buffer_size.__round__()+1]
# array2 = data[buffer_size.__round__()+1: buffer_size.__round__()*2+1]
# array3 = data[(buffer_size.__round__()*2)+1: buffer_size.__round__()*3+1]
# array4 = data[(buffer_size.__round__()*3)+1: data.__len__().__round__() + 1]
#
# print()
# print(sp.euclidean(data2[1], data2[2]))
print(float(test.__array__()))
#
# count = []
# for i in array1:
#     count[i] = 0
#     for j in array1:
#         if sp.euclidean(array1[i], array1[j]) >
