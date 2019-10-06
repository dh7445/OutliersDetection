import pandas as pd
import scipy.spatial.distance as sp

feature_space = pd.read_csv("../Support Files/test_dataset.csv", header=None, engine='python')
dimensions = 8
data = feature_space.iloc[:, 0:dimensions].values
k = 35
N = data.__len__()
LOF_array = []
position = 0
neighbors_distances = []


def calculate_k_nearest_distances(p):
    index = 0
    nearest_neighbors = []
    for neighbors in data:
        nearest_neighbors.append([index, sp.euclidean(p, neighbors)])
        index += 1
    sorted_neighbors = sorted(nearest_neighbors, key=lambda x: x[1])
    return sorted_neighbors[1:k + 1]


def calculate_reachability_distance(p_position):
    k_neighbors = neighbors_distances[p_position]
    reach_distance = 0
    for neighbor in k_neighbors[1]:
        layer2_neighbor__distances = neighbor[0]
        K_lowest_distance_of_neighbor = neighbors_distances[layer2_neighbor__distances][1][k-1][1]
        reach_distance = reach_distance + max(K_lowest_distance_of_neighbor, neighbor[1])
    return [reach_distance, k_neighbors]


def calculate_local_reachability_density(p_position):
    reach_distance_for_point_p = calculate_reachability_distance(p_position)
    lrd = 1 / (reach_distance_for_point_p[0] / k)
    return [lrd, reach_distance_for_point_p]


def calculate_LOF(p_position):
    holder = calculate_local_reachability_density(p_position)
    LRDp = holder[0]
    k_neighbors = holder[1][1][1]
    LRDk_neighbors_sum = 0
    for neighbor in k_neighbors:
        LRDk_holder = calculate_local_reachability_density(neighbor[0])
        LRDk_neighbors_sum = LRDk_neighbors_sum + LRDk_holder[0]
    lof = (LRDk_neighbors_sum / LRDp) / k
    return lof


for point in data:
    neighbors_distances.append([position, calculate_k_nearest_distances(point)])
    position += 1


for p in range(0, data.__len__()):
    lof_of_p = calculate_LOF(p)
    LOF_array.append([p, lof_of_p])

sorted_LOF = sorted(LOF_array, key=lambda x: x[1], reverse=True)
print(f"Sorted LOF values for all objects in the dataset: ")
print(f"For N = {N}, Dimensions = {dimensions}, k = {k}")
print(*sorted_LOF, sep="\n")

